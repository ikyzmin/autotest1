
Feature: Serve coffee
  Coffee should not be served until paid for
  Coffee should not be served until the button has been pressed
  If there is no coffee left then money should be refunded

Scenario: Buy last coffee
  Given There are 1 coffees left in the machine
  And I have deposited 1 dollar
  When I press the coffee button
  Then I should be served a coffee

Scenario: Empty machine
  Given There are 0 coffees left in the machine
  And I have deposited 1 dollar
  When I press the coffee button
  Then I should not be served a coffee
  And I should get 1 dollar change

Scenario: Empty machine invalid
  Given There are 0 coffees left in the machine
  And I have deposited 1 dollar
  When I press the coffee button
  Then I should not be served a coffee
  And I should get 10 dollar change

Scenario: Invalid scenario
  Given There are 0 coffees left in the machine
  And I have deposited 1 dollar
  When I press the coffee button
  Then I should be served a coffee

Scenario: Not payed
  Given There are 1 coffees left in the machine
  When I press the coffee button
  Then I should not be served a coffee
