Feature: Activity
  As a user of the system
  I want to authorize and manage credit card activities
  So that I can ensure secure transactions and manage user activities

  Scenario: Authorize a credit card activity
    Given the system has an existing category registration with code "FOOD" and description "Food and Dining"
    And the system has an existing mcc registration with code "4213" and category "FOOD"
    And the system has and existing merchant registration with name merchant name "Supermarket XYZ" with mcc code "4213"
    And the system has an existing user account with account number "987677421"
    And the user account "987677421" has an existing account balance for the category "FOOD" with amount in cents "100000"
    When I send an activity request with the user account "987677421" authorizes a credit card activity with amount in cents "10000" for merchant "Supermarket XYZ" with mcc code "4213", with fallback "False" and merchant priority "False"
    Then I should receive a response with status code 201
    And the response should contain a field code with the value "00"
    And the system should record the activity with amount in cents "10000" and category "FOOD" with the status "00"
    And the account balance amount in cents should be "90000" for the user account "987677421" and category "FOOD"

  Scenario: Authorize a credit card activity with insufficient balance
    Given the system has an existing category registration with code "FOOD" and description "Food and Dining"
    And the system has an existing mcc registration with code "4213" and category "FOOD"
    And the system has and existing merchant registration with name merchant name "Supermarket XYZ" with mcc code "4213"
    And the system has an existing user account with account number "987677421"
    And the user account "987677421" has an existing account balance for the category "FOOD" with amount in cents "5000"
    When I send an activity request with the user account "987677421" authorizes a credit card activity with amount in cents "10000" for merchant "Supermarket XYZ" with mcc code "4213", with fallback "False" and merchant priority "False"
    Then I should receive a response with status code 201
    And the response should contain a field code with the value "51"
    And the system should record the activity with amount in cents "10000" and category "FOOD" with the status "51"
    And the account balance amount in cents should be "5000" for the user account "987677421" and category "FOOD"

  Scenario: Authorize a credit card activity with fallback
  Given the system has an existing category registration with code "CASH" and description "Cash Category"
  And the system has an existing category registration with code "FOOD" and description "Food and Dining"
  And the system has an existing mcc registration with code "4213" and category "FOOD"
  And the system has an existing mcc registration with code "6443" and category "CASH"
  And the system has and existing merchant registration with name merchant name "Supermarket XYZ" with mcc code "4213"
  And the system has an existing user account with account number "987677421"
  And the user account "987677421" has an existing account balance for the category "FOOD" with amount in cents "100"
  And the user account "987677421" has an existing account balance for the category "CASH" with amount in cents "100000"
  When I send an activity request with the user account "987677421" authorizes a credit card activity with amount in cents "10000" for merchant "Supermarket XYZ" with mcc code "4213", with fallback "True" and merchant priority "False"
  Then I should receive a response with status code 201
  And the response should contain a field code with the value "00"
  And the system should record the activity with amount in cents "10000" and category "CASH" with the status "00"
  And the account balance amount in cents should be "100" for the user account "987677421" and category "FOOD"
  And the account balance amount in cents should be "90000" for the user account "987677421" and category "CASH"
#
#  Scenario: Authorize a credit card activity with merchant priority
#
#  Scenario: Authorize a credit card activity with merchant priority and fallback