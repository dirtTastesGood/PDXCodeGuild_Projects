class Account:
    def __init__(self, accnt_num, name, rate):
        self.accnt_num = accnt_num
        self.owner = name
        self.balance = 0
        self.interest_rate = rate

        return

class ATM:
    def __init__(self):
        self.interest_rate = 0.1
        self.accounts = self.__load_accounts()
        # print(self.accounts)
        return 

    def create_account(self):
        name = input("\nPlease enter your name: ")

        accnt_num = self.__gen_accnt_num()
        
        self.accounts[accnt_num] = {'accnt_num': accnt_num, 'owner': name, 'balance':0, 'interest_rate':0.1}
        
        self.__save_accounts()

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
        return account['balance']

    def deposit(self, account, amount):
        account['balance'] += amount
        return

    def __check_withdrawal(self, account, amount):
        return account['balance'] - amount > 0

    def withdraw(self, account, amount):
        if self.__check_withdrawal(account, amount):
            account['balance'] -= amount
            msg = "Withdrawal successful."
        else: 
            msg = "Withdrawal failed. Insufficient funds."
        return msg

    def calc_interest(self, account):
        return account['balance'] * account['interest_rate']

    def __load_accounts(self):
        accnts = {}
        f = open('account_record.txt', 'r')
        accnt_record = f.readlines()
        f.close()

        for accnt in accnt_record:
            if len(accnt) == 1:
                accnt_record.remove(accnt)
                continue
            accnt = accnt.split("=")

            key = accnt[0]
            values = accnt[1]    

            accnts[key] = {}

            values = values.split(",")
            for value in values:
                value = value.split(":")

                accnts[key][value[0]] = value[1].strip()
        
        return accnts

    def __save_accounts(self):
        with open('account_record.txt', 'w') as accnt_record:
            record = ""
            for accnt in self.accounts:
                record += f"{accnt}="
                
                for key in self.accounts[accnt]:
                    pair = []
                    pair.append(key)
                    pair.append(self.accounts[accnt][key])
                    record += f"{pair[0]}:{pair[1]}"

                    final_key = list(self.accounts[accnt].keys())[-1]
                    if key != final_key:
                        record += ","
                record = f"{record}\n"
            print(record, file=accnt_record)
        return

def main():
    atm = ATM()
    atm.create_account()
    # account = atm.accounts['0001']
    # print(f"current balance: {atm.check_balance(account)}")
    # print(f"deposit $300.")
    # atm.deposit(account, 300)
    # print(f"current balance: {atm.check_balance(account)}")
    # print(f"Withdraw $50: ")
    # msg = atm.withdraw(account, 50)
    # print(f"{msg} current balance: {atm.check_balance(account)}")

    # print(f"Withdraw $500: ")
    # msg = atm.withdraw(account, 500)
    # print(f"{msg} current balance: {atm.check_balance(account)}")

    # print(f"Your monthly interest is: ${atm.calc_interest(account)}")
    return
    
main()
