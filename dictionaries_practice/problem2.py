def average(d):
    prices = []
    
    [prices.append(d[key]) for key in d.keys()]

    return sum(prices) / len(prices)
    
def main():
    combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}

    print(f"The average price in {combined} is {average(combined)}")

main()
