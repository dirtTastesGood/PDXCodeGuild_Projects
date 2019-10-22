class ATM:
    def __init__(self):
        self.interest_rate = 0.1
        self.accounts = self.__load_accounts()
        
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
        account['balance'] = float(account['balance'])
        account['balance'] += float(amount)
        return

    def __check_withdrawal(self, account, amount):
        account['balance'] = float(account['balance'])
        return account['balance'] - float(amount) > 0

    def withdraw(self, account, amount):
        if self.__check_withdrawal(account, amount):
            account['balance'] = float(account['balance'])
            account['balance'] -= float(amount)
            msg = "Withdrawal successful."
        else: 
            msg = "Withdrawal failed. Insufficient funds."
        return msg

    def calc_interest(self, account):
        account['balance'] = float(account['balance'])
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

            def display_account(self, account):
                pass

            def exit(self):
                self.__save_accounts()
                
                return
                
        return

def display_menu():
    options = ['Create an Account', 'Edit an account', 'Make a deposit', 'Make a withdrawal', 'Calculate monthly interest', 'Quit']
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

def main():
    atm = ATM()
    
    print("\nHello! I am an ATM!")

    while True:
        print("\nHow can I help you?")
        
        display_menu()

        choice = input("\nPlease enter the number of one of the options listed above:")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            atm.exit()
            break

    return
    
main()
