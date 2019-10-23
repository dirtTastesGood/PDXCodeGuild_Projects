class ATM:
    def __init__(self):
        self.interest_rate = 0.1
        # self.accounts = self.__load_accounts()
        self.accounts = {'0001':{'accnt_num':'0001', 'owner':'Keegan', 'balance':0, 'interest_rate': 0.1, 'transactions':{'date':'10-22-2019', 'type':'deposit', 'amount':200}},
                         '0002':{'accnt_num':'0002', 'owner':'Ringo', 'balance':0, 'interest_rate': 0.1, 'transactions':{'date':'10-22-2019', 'type':'deposit', 'amount':500}}   
                        }       
        return 

    def create_account(self, name):
        accnt_num = self.__gen_accnt_num()
        
        self.accounts[accnt_num] = {'accnt_num': accnt_num, 
                                    'owner': name, 
                                    'balance':0, 
                                    'interest_rate':self.interest_rate, 
                                    'transactions': {'1':{'date':'10-22-2019','amount':100, 'type':'deposit'}}
                                    }
        
        self.__save_accounts()

        return self.accounts[accnt_num]

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

    def display_account(self, account):
        print(account)
        return

    def deposit(self, account, amount):
        account['balance'] = float(account['balance'])
        account['balance'] += float(amount)
        
        #self.__update_transactions(account, "deposit", amount)

        return

    def __update_transactions(self, account, trns_type, amount=0):
        transaction_number = len(self.accounts[account]['transactions']) + 1
        new_transaction = {}
        new_transaction = {trns_type:amount}

        #self.accounts[account]['transactions'][transaction_number] = new_transaction

        print(self.accounts[account])
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

    # This method is gross. However, it just reads
    # each line of account_record.txt and splits them into
    # a dictionary for each account.
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
                print(f"value: {value}")
                value = value.split(":")

                accnts[key][value[0]] = value[1].strip()

                if value[0] == "transactions":
                    trn_list = value[1].split("&")
                    print(f"transactions: {trn_list}")
                    transactions = {}
                    for t in trn_list:
                        print(f"t: {t}")
                        t = t.split("#")
                        t_key = t[0]
                        t_values = t[1].strip()
                    
                        t_values = t_values.split("*")
                        t_dict = {}
                        for t_value in t_values:
                            t_pair = t_value.split("+")
                            t_pair_key = t_pair[0]
                            t_pair_value = t_pair[1]
                            t_dict[t_pair_key] = t_pair_value
                        transactions[t_key] = t_dict
                    
                    accnts[key][value[0]] = transactions

        return accnts # returns a dictionary of all accounts

    def __save_accounts(self):
        with open('account_record.txt', 'w') as accnt_record:
            record = ""
            for accnt in self.accounts:
                record += f"{accnt}="
                
                for key in self.accounts[accnt]:
                    pair = []
                    pair.append(key)
                    pair.append(self.accounts[accnt][key])


                    record += f"{pair[0]}:"

                    if pair[0] == "transactions":
                        transactions = pair[1]
                        final_t_key = list(transactions.keys())[-1]

                        for t_key in transactions:
                            record += f"{t_key}#"
                            record += str(transactions[t_key])

                            if t_key != final_t_key:
                                record += "&"

                    else:
                        record += f"{pair[1]}"

                    final_key = list(self.accounts[accnt].keys())[-1]
                    if key != final_key:
                        record += ","
                record += "\n"
        print(record)        
        return # breaks down self.accounts into a single line to be saved

    def display_menu(self):
        options = ['Create an Account', 'Edit an account', 'Make a deposit', 'Make a withdrawal', 'Calculate monthly interest', 'Quit']
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        return
    
    def exit(self):
        self.__save_accounts()
        
        return
        


def main():
    atm = ATM()
    
    
    # account = atm.create_account("Ringo")

    # atm.display_account(account)

    # atm.deposit(account, 100)

    atm.exit()
    return
    
main()
