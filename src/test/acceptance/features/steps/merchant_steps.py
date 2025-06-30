import uuid
from datetime import datetime

from behave import given, when, then

from src.main.shared.date_util import get_utc_now
from src.main.shared.database.sqlalchemy.models import MerchantEntity, MccEntity, CategoryEntity


@given('the system has an existing category registration')
def step_impl(context):
    context.existing_category = CategoryEntity(
        code="FOOD",
        description="This is a food category",
        created_at=get_utc_now()
    )
    context.db.add(context.existing_category)
    context.db.commit()

@given('the system has an existing mcc registration for the category')
def step_impl(context):
    context.existing_mcc = MccEntity(
        id=uuid.uuid4(),
        code="5677",
        category_id=context.existing_category.id,
        created_at=datetime.now()
    )
    context.db.add(context.existing_mcc)
    context.db.commit()


@given('I have a mcc registration request with an existing mcc code')
def step_impl(context):
    context.request_data = {
        "code": context.existing_mcc.code,
        "category_id": context.existing_mcc.category_id
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@given('I have a category registration request with an existing category code')
def step_impl(context):
    context.request_data = {
        "code": context.existing_category.code,
        "description": context.existing_category.description
    }
    context.headers = {
        "Content-Type": "application/json"
    }


@given('I have a valid merchant registration request with the existing mcc code')
def step_impl(context):
    context.request_data = {
        "merchant_name": "Test Merchant",
        "mcc_id": str(context.existing_mcc.id)
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@given('I have a valid mcc registration request with the existing category code')
def step_impl(context):
    context.request_data = {
        "code": "7856",
        "category_id": context.existing_category.id
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@given('I have a valid category registration request')
def step_impl(context):
    context.request_data = {
        "code": "FOOD",
        "description": "This is a food category"
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@given('I have an invalid merchant registration request')
def step_impl(context):
    context.request_data = {
        "merchant_name": "",  # Invalid name
        "mcc_id": str(uuid.uuid4())
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@given('I have an invalid category registration request')
def step_impl(context):
    context.request_data = {
        "code": "FO",  # Invalid code
        "description": "This is a food category"
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@given('I have an invalid mcc registration request')
def step_impl(context):
    context.request_data = {
        "code": "11",  # Invalid code
        "category_id": 1234
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@given('I have a merchant registration request with an existing merchant name')
def step_impl(context):
    existing_merchant = MerchantEntity(id=uuid.uuid4(), merchant_name="Existing Merchant", mcc_id=context.existing_mcc.id, created_at=datetime.now())
    context.db.add(existing_merchant)
    context.db.commit()

    context.request_data = {
        "merchant_name": existing_merchant.merchant_name,
        "mcc_id": str(uuid.uuid4())
    }
    context.headers = {
        "Content-Type": "application/json"
    }

@when('I send the request to create a new merchant registration')
def step_impl(context):
    context.response = context.client.post('/merchants', json=context.request_data, headers=context.headers)

@when('I send the request to create a new mcc registration')
def step_impl(context):
    context.response = context.client.post('/mcc', json=context.request_data, headers=context.headers)

@when('I send the request to create a new category')
def step_impl(context):
    context.response = context.client.post('/categories', json=context.request_data, headers=context.headers)

@then('the response should contain the merchant details')
def step_impl(context):
    response_data = context.response.json()
    assert 'merchant_name' in response_data, "Response does not contain 'merchant_name'"
    assert response_data['merchant_name'] == context.request_data['merchant_name'], \
        f"Expected merchant name {context.request_data['merchant_name']}, but got {response_data['merchant_name']}"
    assert 'merchant_id' in response_data, "Response does not contain 'merchant_id'"

@then('the response should contain the mcc details')
def step_impl(context):
    response_data = context.response.json()
    assert 'code' in response_data, "Response does not contain 'code'"
    assert response_data['code'] == context.request_data['code'], \
        f"Expected MCC code {context.request_data['code']}, but got {response_data['code']}"
    assert 'category_id' in response_data, "Response does not contain 'category_id'"
    assert response_data['category_id'] == context.request_data['category_id'], \
        f"Expected category ID {context.request_data['category_id']}, but got {response_data['category_id']}"

@then('the response should contain the category details')
def step_impl(context):
    response_data = context.response.json()
    assert 'code' in response_data, "Response does not contain 'code'"
    assert response_data['code'] == context.request_data['code'], \
        f"Expected category code {context.request_data['code']}, but got {response_data['code']}"
    assert 'description' in response_data, "Response does not contain 'description'"
    assert response_data['description'] == context.request_data['description'], \
        f"Expected category description {context.request_data['description']}, but got {response_data['description']}"

@then('the merchant should be created in the system')
def step_impl(context):
    response_data = context.response.json()
    merchant_id = response_data['merchant_id']
    merchant_name = response_data['merchant_name']
    merchant = context.db.query(MerchantEntity).filter_by(id=merchant_id).first()
    assert merchant is not None, "Merchant was not created in the system"
    assert merchant.merchant_name == merchant_name, f"Expected merchant name {merchant_name}, but got {merchant.merchant_name}"
    assert merchant.id is not None, "Merchant ID should not be None"

@then('the mcc should be created in the system')
def step_impl(context):
    response_data = context.response.json()
    mcc_code = response_data['code']
    category_id = response_data['category_id']
    mcc = context.db.query(MccEntity).filter_by(code=mcc_code, category_id=category_id).first()
    assert mcc is not None, "MCC was not created in the system"
    assert mcc.code == mcc_code, f"Expected MCC code {mcc_code}, but got {mcc.code}"
    assert mcc.category_id == category_id, f"Expected category ID {category_id}, but got {mcc.category_id}"

@then('the category should be created in the system')
def step_impl(context):
    response_data = context.response.json()
    category_code = response_data['code']
    description = response_data['description']
    category = context.db.query(CategoryEntity).filter_by(code=category_code, description=description).first()
    assert category is not None, "Category was not created in the system"
    assert category.code == category_code, f"Expected category code {category_code}, but got {category.code}"
    assert category.description == description, f"Expected category description {description}, but got {category.description}"

@then('the response should contain an error message indicating the merchant validation failure')
def step_impl(context):
    response_data = context.response.json()
    assert 'detail' in response_data, "Response does not contain 'detail'"
    assert response_data['detail'] == "Invalid merchant name", \
        f"Expected error message 'Invalid merchant name', but got {response_data['detail']}"

@then('the response should contain an error message indicating that the merchant already exists')
def step_impl(context):
    response_data = context.response.json()
    assert 'detail' in response_data, "Response does not contain 'detail'"
    assert response_data['detail'] == f"Merchant with name {context.request_data["merchant_name"]} already exists.", \
        f"Expected error message 'Merchant with name {context.request_data["merchant_name"]} already exists.', but got {response_data['detail']}"

@then('the response should contain an error message indicating that the mcc already exists')
def step_impl(context):
    response_data = context.response.json()
    assert 'detail' in response_data, "Response does not contain 'detail'"
    assert response_data['detail'] == f"MCC with code {context.request_data['code']} already exists.", \
        f"Expected error message 'MCC with code {context.request_data['code']} already exists.', but got {response_data['detail']}"

@then('the response should contain an error message indicating the mcc validation failure')
def step_impl(context):
    response_data = context.response.json()
    assert 'detail' in response_data, "Response does not contain 'detail'"
    assert response_data['detail'] == "MCC code must be 4 characters long", \
        f"Expected error message 'MCC code must be 4 characters long', but got {response_data['detail']}"

@then('the response should contain an error message indicating the category validation failure')
def step_impl(context):
    response_data = context.response.json()
    assert 'detail' in response_data, "Response does not contain 'detail'"
    assert response_data['detail'] == "Category code must be between 3 and 100 characters long", \
        f"Expected error message 'Category code must be between 3 and 100 characters long', but got {response_data['detail']}"

@then('the response should contain an error message indicating that the category already exists')
def step_impl(context):
    response_data = context.response.json()
    assert 'detail' in response_data, "Response does not contain 'detail'"
    assert response_data['detail'] == f"Category with code {context.request_data['code']} already exists.", \
        f"Expected error message 'Category with code {context.request_data['code']} already exists.', but got {response_data['detail']}"