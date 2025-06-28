from behave import given, when, then

@then('I should receive a response with status code 201')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"

@then('I should receive a response with status code 400')
def step_impl(context):
    assert context.response.status_code == 400, f"Expected status code 400, but got {context.response.status_code}"

@then('I should receive a response with status code 409')
def step_impl(context):
    assert context.response.status_code == 409, f"Expected status code 409, but got {context.response.status_code}"