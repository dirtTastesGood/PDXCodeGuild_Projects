
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

def dollars_to_pennies(dollars):
    pennies = dollars * 100

    return pennies

def print_result(total, pennies, result):
    output = f"${total} converts to {pennies} pennies which converts to: \n\n"
    for coin in result:
        output += f"{coin}: {result[coin]}\n"

    print(output)

def main():
    while True:    
        total = float(input("\nPlease enter number of dollars and cents ('q' to quit): $"))
        pennies = int(dollars_to_pennies(total))
        result = coins_per_denom(pennies) # returns a dict

        print_result(total, pennies, result)
        if str(total).lower == "q":
            break
main()