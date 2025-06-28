Feature: Account
  As a user
  I want to create an new account
  So that I can manage my account balance and transactions

  Scenario: Create a new account
    Given I have a valid account creation request
    When I send the request to create a new account
    Then I should receive a response with status code 201
    And the response should contain the account details
    And the account should be created in the system

  Scenario: Create an account with invalid data
    Given I have an invalid account creation request
    When I send the request to create a new account
    Then I should receive a response with status code 400
    And the response should contain an error message indicating the account validation failure

  Scenario: Create an account with already existing account number
    Given I have an account creation request with an existing account number
    When I send the request to create a new account
    Then I should receive a response with status code 409
    And the response should contain an error message indicating that the account already exists