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