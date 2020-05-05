# Created by rapid at 5/4/2020
Feature: Lingocard_albanian_hungarian_are_here
  # Just practice with lingocard.com

  Scenario: Verify albanian and hungarian are here
    Given Loginpage
    Then Verify Albanian is here
    Then Verify Hungarian is here