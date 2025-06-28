Feature: Merchant
  As a merchant
  I want to create a new registration
  So that I can manage my business and categories

  Scenario: Create a new merchant registration
    Given I have a valid merchant registration request
    When I send the request to create a new merchant registration
    Then I should receive a response with status code 201
    And the response should contain the merchant details
    And the merchant should be created in the system

  Scenario: Create a merchant registration with invalid data
    Given I have an invalid merchant registration request
    When I send the request to create a new merchant registration
    Then I should receive a response with status code 400
    And the response should contain an error message indicating the merchant validation failure

  Scenario: Create a merchant registration with already existing merchant name
    Given I have a merchant registration request with an existing merchant name
    When I send the request to create a new merchant registration
    Then I should receive a response with status code 409
    And the response should contain an error message indicating that the merchant already exists