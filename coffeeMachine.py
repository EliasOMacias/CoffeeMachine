


#todo  6: deduct resources


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,

}

till = 0

def coffeeMachine():

    prompt = input('What would you like?\n')

    if prompt == 'report'.lower():
        print(resources, f'Till: ${till}')

    elif prompt == 'espresso'.lower():
        if MENU['espresso']['ingredients']['water'] > resources['water'] and MENU['espresso']['ingredients']['coffee'] >= resources['coffee']:
            print('insufficient beans and coffee')
        elif MENU['espresso']['ingredients']['water'] > resources['water']:
            print("insufficient water")
        elif MENU['espresso']['ingredients']['coffee'] > resources['coffee']:
            print('insufficient coffee')
        else:
            transactionValidator('espresso')
            resources['water'] -= MENU['espresso']['ingredients']['water']
            resources['coffee'] -= MENU['espresso']['ingredients']['coffee']


    elif prompt == 'latte'.lower():
        if MENU['latte']['ingredients']['water'] > resources['water'] and MENU['latte']['ingredients']['coffee'] >= resources['coffee']:
                print('insufficient beans and coffee')
        elif MENU['latte']['ingredients']['water'] > resources['water']:
            print("insufficient water")
        elif MENU['latte']['ingredients']['coffee'] > resources['coffee']:
            print('insufficient coffee')
        elif MENU['latte']['ingredients']['milk'] > resources['milk']:
            print('insufficient milk')
        else:
            transactionValidator('latte')
            resources['water'] -= MENU['latte']['ingredients']['water']
            resources['milk'] -= MENU['latte']['ingredients']['milk']
            resources['coffee'] -= MENU['latte']['ingredients']['coffee']



    elif prompt == 'cappuccino'.lower():
        if MENU['cappuccino']['ingredients']['water'] > resources['water'] and MENU['cappuccino']['ingredients']['coffee'] >= resources['coffee']:
            print('insufficient beans and coffee')
        elif MENU['cappuccino']['ingredients']['water'] > resources['water']:
            print("insufficient water")
        elif MENU['cappuccino']['ingredients']['coffee'] > resources['coffee']:
            print('insufficient coffee')
        elif MENU['cappuccino']['ingredients']['milk'] > resources['milk']:
            print('insufficient milk')
        else:
            transactionValidator('cappuccino')
            resources['water'] -= MENU['cappuccino']['ingredients']['water']
            resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
            resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']

    orderAgain = input('Would you like another drink?\n Yes or no?\n')

    if orderAgain == 'yes'.lower():
        coffeeMachine()
    else:
        print('Thank you pharoah')



#coffeeMachine()




def transactionValidator(item):
    total = 0.0
    global till
    till = 0
    itemCost = MENU[item]['cost']
    print(f'the total is: {itemCost}')



    while total < itemCost:
        quarters = int(input('How many quarters?\n'))
        total += (0.25 * quarters)
        till += (0.25 * quarters)
        if total >= itemCost:
            break

        dimes = int(input(f'total: ${total}. How many dimes?\n'))
        total += (0.10 * dimes)
        till += (0.25 * dimes)
        if total >= itemCost:
            break

        nickels = int(input(f'total:$  {total}How many nickels\n'))
        total += (0.05 * nickels)
        till += (0.05 * nickels)
        if total >= itemCost:
            break

        pennies = int(input('How many pennies\n'))
        till += (0.01 * pennies)
        total += (0.01 * pennies)


    if total == itemCost:
        print(f'Thank you! Here is your {item}')
    elif total > itemCost:
        print(f'Thank you! your change is ${total - itemCost}')
    else:
        print('insufficient funds broke boy')





coffeeMachine()


