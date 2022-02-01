from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_continue = True
resource = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


while is_continue:
    request = input(f"What would you like? ({menu.get_items()}): ")
    if request == 'report':
        resource.report()
        money.report()
    elif request == 'off':
        quit()
    else:
        drink = menu.find_drink(request)
        if resource.is_resource_sufficient(drink):
            price = drink.cost
            if money.make_payment(price):
                resource.make_coffee(drink)