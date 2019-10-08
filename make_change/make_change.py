
def coins_per_denom(total):
    coins = {
            "quarters":25,
            "dimes":10, 
            "nickels":5, 
            "pennies":1
            }
    coin_totals = {}

    for coin in coins:
        denom = coins[coin]
        coin_total = total // denom
        coin_totals[coin] = coin_total 

        total -= coin_totals[coin] * denom

    return coin_totals

def print_result(total, result):
    output = f"{total} pennies converts to: \n\n"
    for coin in result:
        output += f"{coin}: {result[coin]}\n"

    print(output)

def main():
    while True:    
        total = int(input("\nPlease enter an amount of pennies ('q' to quit): "))
        result = coins_per_denom(total) # returns a dict

        print_result(total, result)
        if str(total).lower == "q":
            break
main()