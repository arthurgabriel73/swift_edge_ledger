Feature: Merchant
  As a merchant
  I want to create a new registration
  So that I can manage my business and categories

  Scenario: Create a new merchant registration
    Given the system has an existing mcc registration
    And I have a valid merchant registration request with the existing mcc code
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
    Given the system has an existing mcc registration
    And I have a merchant registration request with an existing merchant name
    When I send the request to create a new merchant registration
    Then I should receive a response with status code 409
    And the response should contain an error message indicating that the merchant already exists

  Scenario: Create a mcc
    Given I have a valid mcc registration request
    When I send the request to create a new mcc registration
    Then I should receive a response with status code 201
    And the response should contain the mcc details
    And the mcc should be created in the system

  Scenario: Create a mcc with invalid data
    Given I have an invalid mcc registration request
    When I send the request to create a new mcc registration
    Then I should receive a response with status code 400
    And the response should contain an error message indicating the mcc validation failure

  Scenario: Create a mcc with already existing mcc code
    Given the system has an existing mcc registration
    And I have a mcc registration request with an existing mcc code
    When I send the request to create a new mcc registration
    Then I should receive a response with status code 409
    And the response should contain an error message indicating that the mcc already exists
