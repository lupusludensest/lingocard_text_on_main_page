# Created by rapid at 5/3/2020
Feature: Lingocard_partnership_request_form
  # Just practice with lingocard.com

  Scenario: User fill the partnership request form by first name, last name, e-mail, test
    Given Loginpage
    Then User enters first name Vic
    Then User enters last name Gurov
    Then User enters e-mail gurovvic@gmail.com
    Then User enters request Test request
    Then User clicks on send button
    Then Verify that field Your message has no text at all
