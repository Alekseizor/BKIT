# -- FILE: features/example.feature
Feature: Showing off behave

  Scenario: Function return message about creation
    Given Bot
    When test_a_equal_zero return OK
    And test_result_bikvadrat return OK
    Then good job