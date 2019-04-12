Feature: Google search Feature
  In order to ensure Google search works I want to run a search for BrowserStack

  Scenario: Search for Software Testing
  Given I'm on Google
  When I search for BrowserStack
  Then the browser title should have BrowserStack - Google Search
