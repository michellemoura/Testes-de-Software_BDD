Feature: LEAD Platform

   @login
Scenario: Effect login (1a)
  Given that the user is on the login page
  When the user provides a login with valid data
  Then the system directs the user to the home page

  @conceptBDD
Scenario: Look for concept BDD (2a)
  Given that the user is logged in to the system
  When the user clicks on the glossary module
    And the user click the search field and enter the BDD name
    And the user click the search button1
  Then the system returns the concept of BDD

  @myNotes
Scenario: Go to my notes module (3a)
Given that the user is logged in to the system2
When the user clicks on my notes module
Then the system returns the user notes

  @helpCenter
Scenario: Go to help option (4a)
Given that the user is logged in to the system3
When the user clicks on the help option in the accessibility bar
    And the user enters what he wants to search
    And the user click the search button
Then the system returns the search result


  @videosinPounds
Scenario: Enable system pounds videos (5a)
  Given that the user is logged in to the system5
  When user click on Enable video pounds option in accessibility bar
  Then the system returns the enabled option

  @exit
Scenario: Sair da página (6a)
  Given that the user is logged in to the system4
  When the user click on user information
      And the user click the exit button and confirm that he wishes to quit
  Then the system returns the login page