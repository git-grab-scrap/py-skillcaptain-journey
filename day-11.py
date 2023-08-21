class BankAccount:
    def __init__(self, acc_num, acc_name, acc_bal):
        self.acc_num = int(acc_num)
        self.acc_name = acc_name
        self.acc_bal = int(acc_bal)
    
    def bank_trx_dep(self, dep_amnt):
        self.acc_bal += dep_amnt
    
    def bank_trx_rem(self, amnt):
        if (amnt >= self.acc_bal):
            print(f"Withdraw from what you have okay? Current bal: {self.acc_bal} ")
        else:
            self.acc_bal -= amnt
    
    def bank_display(self):
        print(f"Account holder name: {self.acc_name} \n Account No: {self.acc_num} \n Currnet Balance: {self.acc_bal}")

ba_details = BankAccount(123456, "Travis", 234)
ba_details.bank_display()

ba_details.bank_trx_dep(356)
ba_details.bank_display()

ba_details.bank_trx_rem(800)
ba_details.bank_display()
