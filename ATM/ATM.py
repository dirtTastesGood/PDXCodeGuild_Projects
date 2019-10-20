class Account:
    def __init__(self, accnt_num, name, rate):
        self.accnt_num = accnt_num
        self.owner = name
        self.balance = 0
        self.interest_rate = rate

        return

class ATM:
    def __init__(self):
        self.accounts = {}
        self.interest_rate = 0.1
        return 

    def create_account(self):
        name = input("\nPlease enter your name: ")
    
        accnt_num = self.__gen_accnt_num()

        self.accounts[accnt_num] = Account(accnt_num, name, self.interest_rate)

        return 

    def __gen_accnt_num(self):
        if len(self.accounts) == 0:
            accnt_num = "0001"

        else:
            keys = list(self.accounts.keys())
            num = self.accounts[keys[-1]]['accnt_num'] # grab the last account number in dictionary

            zeros_needed = 0
            i=0
            while True:
                if num[i] != '0':
                    num = num[i::]
                    break
                i += 1    
                zeros_needed = i
                
            num = int(num) + 1

            zeros = ''.join(["0" for i in range(0, zeros_needed) if len(str(num)) < 4])

            accnt_num = f"{zeros}{num}"

        return accnt_num

    def check_balance(self, account):
        return self.accounts[account].balance

    def deposit(self, account, amount):
        return

    def __check_withdrawal(self, account, amount):

        return

    def withdraw(self, account, amount):
        return

    def calc_interest(self, account):
        return

    def __save_accounts(self):
        
        pass

def main():
    atm = ATM()
    atm.create_account()
    account = atm.accounts['0001']
    print(f"current balance: {atm.check_balance(account.accnt_num)}")
    return
    
main()
