import uuid
from datetime import datetime

from behave import given, when, then

from src.main.shared.database.sqlalchemy.models import AccountEntity
from faker import Faker


fake = Faker()

@given('I have a valid account creation request')
def step_impl(context):
    context.request_data = {
        "account_number": fake.credit_card_number(),
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@given('I have an invalid account creation request')
def step_impl(context):
    context.request_data = {
        "account_number": "1",  # Invalid account number
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@given('I have an account creation request with an existing account number')
def step_impl(context):
    existing_account = AccountEntity(id=uuid.uuid4(), account_number=fake.credit_card_number(), created_at=datetime.now())
    context.db.add(existing_account)
    context.db.commit()

    context.request_data = {
        "account_number": existing_account.account_number,
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@when('I send the request to create a new account')
def step_impl(context):
    context.response = context.client.post('/accounts', json=context.request_data, headers=context.headers)

@then('I should receive a response with status code 201')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"

@then('I should receive a response with status code 400')
def step_impl(context):
    assert context.response.status_code == 400, f"Expected status code 400, but got {context.response.status_code}"

@then('the response should contain the account details')
def step_impl(context):
    response_data = context.response.json()
    assert 'account_number' in response_data, "Response does not contain 'account_number'"
    assert response_data['account_number'] == context.request_data['account_number'], \
        f"Expected account number {context.request_data['account_number']}, but got {response_data['account_number']}"
    assert 'account_id' in response_data, "Response does not contain 'account_id'"

@then('the account should be created in the system')
def step_impl(context):
    response_data = context.response.json()
    account_id = response_data['account_id']

    account = context.db.query(AccountEntity).filter(AccountEntity.id == account_id).first()
    assert account is not None, "Account was not created in the system"
    assert account.account_number == context.request_data['account_number'], \
        f"Expected account number {context.request_data['account_number']}, but got {account.account_number}"

@then('the response should contain an error message indicating the validation failure')
def step_impl(context):
    response_data = context.response.json()
    assert 'detail' in response_data, "Response does not contain 'error'"
    assert response_data['detail'] == "Invalid account number", \
        f"Expected error message 'Invalid account number', but got {response_data['detail']}"

@then('I should receive a response with status code 409')
def step_impl(context):
    assert context.response.status_code == 409, f"Expected status code 409, but got {context.response.status_code}"

@then('the response should contain an error message indicating that the account already exists')
def step_impl(context):
    response_data = context.response.json()
    assert 'detail' in response_data, "Response does not contain 'error'"
    assert response_data['detail'] == "Account already exists", \
        f"Expected error message 'Account already exists', but got {response_data['detail']}"