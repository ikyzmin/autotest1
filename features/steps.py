from freshen import *
from freshen.checks import *

import sys
sys.path.append("..")

import coffee

@Given("There are (\d+) coffees left in the machine")
def create(n):
	scc.machine = coffee.Machine(int(n))
@Given("I have deposited (\d+) dollar")
def deposite(n):
	scc.machine.pay(int(n))

@When("I press the coffee button")
def make():
	scc.machine.makeDrink()

@Then("I should be served a coffee")
def coffeMade():
	assert_equals(scc.machine.drink,"coffee")

@Then("I should not be served a coffee")
def coffeeNotMade():
	assert_equals(scc.machine.drink,"empty")

@Then("I should get (\d+) dollar change")
def machineChange(n):
	assert_equals(scc.machine.change,int(n))


