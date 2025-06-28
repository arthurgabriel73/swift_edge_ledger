import uuid
from datetime import datetime

from behave import given, when, then

from src.main.shared.database.sqlalchemy.models import MerchantEntity


@given('I have a valid merchant registration request')
def step_impl(context):
    context.request_data = {
        "merchant_name": "Test Merchant",
        "mcc_id": str(uuid.uuid4())
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

@given('I have a merchant registration request with an existing merchant name')
def step_impl(context):
    existing_merchant = MerchantEntity(id=uuid.uuid4(), merchant_name="Existing Merchant", mcc_id=uuid.uuid4(), created_at=datetime.now())
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

@then('the response should contain the merchant details')
def step_impl(context):
    response_data = context.response.json()
    assert 'merchant_name' in response_data, "Response does not contain 'merchant_name'"
    assert response_data['merchant_name'] == context.request_data['merchant_name'], \
        f"Expected merchant name {context.request_data['merchant_name']}, but got {response_data['merchant_name']}"
    assert 'merchant_id' in response_data, "Response does not contain 'merchant_id'"

@then('the merchant should be created in the system')
def step_impl(context):
    response_data = context.response.json()
    merchant_id = response_data['merchant_id']
    merchant_name = response_data['merchant_name']
    merchant = context.db.query(MerchantEntity).filter_by(id=merchant_id).first()
    assert merchant is not None, "Merchant was not created in the system"
    assert merchant.merchant_name == merchant_name, f"Expected merchant name {merchant_name}, but got {merchant.merchant_name}"
    assert merchant.id is not None, "Merchant ID should not be None"

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