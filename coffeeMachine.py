
#todo 1: print report
#todo 2: check resources on hand: milk, water, coffee
#todo 3: process coins
#todo 4: check transaction successfuL
#todo  5: deduct resources

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
    "water": 100,
    "milk": 200,
    "coffee": 100,

}

money = 0

def coffeeMachine():

    prompt = input('What would you like?\n')

    if prompt == 'report'.lower():
        print(resources, f'Till: ${money}')

    elif prompt == 'espresso'.lower():
        if MENU['espresso']['ingredients']['water'] > resources['water'] and MENU['espresso']['ingredients']['coffee'] >resources['coffee']:
            print('insufficient beans and coffee')
        elif MENU['espresso']['ingredients']['water'] > resources['water']:
            print("insufficient water")
        elif MENU['espresso']['ingredients']['coffee'] > resources['coffee']:
            print('insufficient coffee')
        else:
            transactionValidator('espresso')


#coffeeMachine()
def coinCounter():
    total = 0.0

    quarters = int(input('How many quarters?\n'))
    total += (0.25 * quarters)

    dimes = int(input('How many dimes?\n'))
    total += (0.10 * dimes)

    nickels = int(input('How many nickels\n'))
    total += (0.05 * nickels)

    pennies = int(input('How many pennies\n'))
    total += (0.01 * pennies)

    return(total)

def transactionValidator(item):
    itemCost = MENU[item]['cost']
    print(f'the total is: {itemCost}')
    total = coinCounter()

    itemCost = MENU[item]['cost']

    if itemCost > total:
        print('insufficient funds')
    elif itemCost <= total:
        print(f'thank you!, here is your {item}')





coffeeMachine()


