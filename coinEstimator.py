"""Estimate value, wraps needed, total coins from weight info."""


def infoInGrams():
    print('Please enter the weight for each in grams:\n')
    penny = float(input('Enter the weight of pennies: '))
    nickel = float(input('Enter the weight of nickels: '))
    dime = float(input('Enter the weight of dimes: '))
    quarter = float(input('Enter the weight of quarters: '))

    # The total amount of each coin.
    total_pennies = int(round(penny/2.5))
    total_nickels = int(round(nickel/5.0))
    total_dimes = int(round(dime/2.268))
    total_quarters = int(round(quarter/5.67))
    total_coins = {
                    'Penny': total_pennies, 'Nickel': total_nickels,
                    'Dime': total_dimes, 'Quarter': total_quarters
                    }
    print('\nApproximate Coin totals:')
    for coin, total in total_coins.items():
        print('Total ' + coin + ' count is: ' + str(total))

    # The amount of rolls needed for each coin.
    pennies_roll = int(round(total_pennies/50))
    nickels_roll = int(round(total_nickels/40))
    dimes_roll = int(round(total_dimes/50))
    quarters_roll = int(round(total_quarters/40))
    rolls_needed = {
                    'Penny': pennies_roll, 'Nickel': nickels_roll,
                    'Dime': dimes_roll, 'Quarter': quarters_roll
                    }
    print('\nRoll totals:')
    for coin, rolls in rolls_needed.items():
        print('The amount of ' + coin + ' rolls needed is: ' + str(rolls))

    # The dollar value of each set of coins.
    value_pennies = pennies_roll * .50
    value_nickels = nickels_roll * 2
    value_dimes = dimes_roll * 5
    value_quarters = quarters_roll * 10
    total_value = {
                    'Penny': value_pennies, 'Nickel': value_nickels,
                    'Dime': value_dimes, 'Quarter': value_quarters
                    }
    print('\nValue totals:')
    for coin, value in total_value.items():
        print('Total ' + coin + ' value is: $' + str(value))


infoInGrams()

# Add option for weight in pounds
