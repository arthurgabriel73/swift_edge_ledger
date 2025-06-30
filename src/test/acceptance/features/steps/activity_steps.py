import uuid

from behave import given, when, then

from src.main.activity.domain.activity_status import ActivityStatus
from src.main.shared.database.sqlalchemy.models import CategoryEntity, MccEntity, MerchantEntity, AccountEntity, \
    AccountBalanceEntity, ActivityEntity
from src.main.shared.date_util import get_utc_now


@given('the system has an existing category registration with code "{code}" and description "{description}"')
def step_impl(context, code, description):
    context.existing_category = CategoryEntity(
        code=code,
        description=description,
        created_at=get_utc_now(),
    )
    context.db.add(context.existing_category)
    context.db.commit()


@given('the system has an existing mcc registration with code "{code}" and category "{category}"')
def step_impl(context, code, category):
    context.existing_mcc = MccEntity(
        id=uuid.uuid4(),
        code=code,
        category_id=context.existing_category.id,
        created_at=get_utc_now(),
    )
    context.db.add(context.existing_mcc)
    context.db.commit()

@given('the system has and existing merchant registration with name merchant name "{merchant_name}" with mcc code "{mcc_code}"')
def step_impl(context, merchant_name, mcc_code):
    context.existing_merchant = MerchantEntity(
        id=uuid.uuid4(),
        merchant_name=merchant_name,
        mcc_id=context.existing_mcc.id,
        created_at=get_utc_now(),
    )
    context.db.add(context.existing_merchant)
    context.db.commit()

@given('the system has an existing user account with account number "{account_number}"')
def step_impl(context, account_number):
    context.existing_account = AccountEntity(id=uuid.uuid4(), account_number=account_number, created_at=get_utc_now())
    context.db.add(context.existing_account)
    context.db.commit()

@given('the user account "{account_number}" has an existing account balance for the category "{category}" with amount in cents "{amount}"')
def step_impl(context, account_number, category, amount):
    context.existing_account_balance = AccountBalanceEntity(
        account_id=context.existing_account.id,
        category_id=context.existing_category.id,
        amount_in_cents=amount
    )
    context.db.add(context.existing_account_balance)
    context.db.commit()

@when('I send an activity request with the user account "{account}" authorizes a credit card activity with amount in cents "{amount}" for merchant "{merchant_name}" with mcc code "{mcc_code}"')
def step_impl(context, account, amount, merchant_name, mcc_code):
    context.request_data = {
        "account": account,
        "amount_in_cents": amount,
        "mcc": mcc_code,
        "merchant": merchant_name,
    }

    context.headers = {
        "Content-Type": "application/json"
    }

    context.response = context.client.post('/activities', json=context.request_data, headers=context.headers)

@then('the response should contain a field code with the value "{code}"')
def step_impl(context, code):
    response_data = context.response.json()
    assert 'code' in response_data, "Response does not contain 'code'"
    assert 'activity_id' in response_data, "Response does not contain 'activity_id'"
    assert response_data['code'] == code, f"Expected code {code}, but got {response_data['code']}"

@then('the system should record the activity with amount in cents "{amount}" and category "{category}" with the status "{status}"')
def step_impl(context, amount, category, status):
    response_data = context.response.json()
    query = context.db.query(ActivityEntity).where(ActivityEntity.id == response_data['activity_id'])
    activity = context.db.execute(query).scalars().unique().one_or_none()
    assert activity is not None, "Activity was not recorded in the system"
    assert activity.timestamp is not None, "Activity was not recorded in the system"
    assert activity.account_id == context.existing_account.id, \
        f"Expected account {context.existing_account.id}, but got {activity.account_id}"
    assert activity.amount_in_cents == int(amount), f"Expected amount {amount}, but got {activity.amount_in_cents}"
    assert activity.category_id == context.existing_category.id, \
        f"Expected category {context.existing_category.id}, but got {activity.category_id}"
    assert activity.merchant_id == context.existing_merchant.id, \
        f"Expected merchant {context.existing_merchant.id}, but got {activity.merchant_id}"
    assert activity.status == status, f"Expected status {status}, but got {activity.status}"


@then('the account balance amount in cents should be "{amount}" for the user account "{account_number}" and category "{category}"')
def step_impl(context, amount, account_number, category):
    account_balance = context.db.query(AccountBalanceEntity).filter(
        AccountBalanceEntity.account_id == context.existing_account.id,
        AccountBalanceEntity.category_id == context.existing_category.id
    ).first()

    assert account_balance is not None, "Account balance was not updated in the system"
    assert account_balance.amount_in_cents == int(amount), \
        f"Expected account balance {amount}, but got {account_balance.amount_in_cents}"
