# -- FILE: features/example.feature
Feature: Showing off behave

  Scenario: Function return message about creation
    Given Factory
    When test_receiving_sneakers return OK
    And test_style_slates return OK
    Then good job