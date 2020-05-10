# Created by rapid at 5/9/2020
Feature: Lingocard_contact_us_btn
  # Just practice with lingocard.com

  Scenario: Verify Contact us has and redirect to info@lingocard.com
    Given Loginpage
    Then Click on info@lingocard.com button
    Then Verify that href with e-mail is here info@lingocard.com
