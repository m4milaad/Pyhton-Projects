from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

dispense = True
while dispense:
    order = input(f"What would you like to have? ({menu.get_items()}): ")
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        dispense = False
    elif menu.find_drink(order):
        if coffee_maker.is_resource_sufficient(menu.find_drink(order)):
            print(f"{order} costs ${menu.find_drink(order).cost}")
            if money_machine.make_payment(menu.find_drink(order).cost):
                coffee_maker.make_coffee(menu.find_drink(order))
