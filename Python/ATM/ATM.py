class ATM:
    def __init__(self):
        self.balance = 0
        self.transactions = {}
        self.interest_rate = 0.1

        return 

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        
        return

    def __check_withdrawal(self, amount):
        return self.balance - amount > 0

    def withdraw(self, amount):


        if self.__check_withdrawal(amount):
            print("called")

            self.balance -= amount
            msg = f"Withdrawal successful. Your new balance is ${self.balance}"
        else: 
            msg = "Withdrawal failed. Insufficient funds."
        return msg

    def calc_interest(self):
        return self.balance * self.interest_rate

    def display_menu(self):
        options = ['Check balance', 'Make a deposit', 'Make a withdrawal', 'Calculate monthly interest', 'Quit']
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        return

def main():
    atm = ATM()
    print("\nHello! I am an ATM!")
    while True:
        print("\nHow can I help you?")
        atm.display_menu()
        choice = input("\nPlease enter the number of one of the options listed above: ")

        if choice == '1':
            print(f"\nYour current balance is: ${atm.balance}")
        elif choice == '2':
            d_amount = float(input("\nHow much would you like to deposit? $"))
            atm.deposit(d_amount)
            print(f"\nThanks. Your current balance is ${atm.check_balance()}")
        elif choice == '3':
            w_amount = float(input("\nHow much would you like to withdraw? $"))
            msg = atm.withdraw(w_amount)
            print(f"\n{msg}")
        elif choice == '4':
            print(f"\nYour monthly interest is: ${atm.calc_interest()}")
        elif choice == '5':
            break
        else:
            print("\nPlease enter a valid option.")

    return

main()