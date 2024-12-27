import datetime
# import pytz

class Account:
    """ Simple account class with __balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.now()
        return utc_time


    def __init__(self, name, balance):
        self.name = name
        self.__balance = 0
        self.transaction_list = []
        print("Account created for " + self.name)
        self.deposit(balance)
        self.show_balance()

    def deposit(self, ammount):
        if ammount > 0:
            self.__balance += ammount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), ammount))
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transaction_list.append((Account._current_time(), amount))
        else:
            print("The amount must be positive and less than your total money")
        self.show_balance()

    def show_balance(self):
        print(f'Balance is {self.__balance}')

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = "withdrawn"
                amount *= -1
            print('{:6} {} on ({})'.format(amount, tran_type, datetime.datetime.now()))

if __name__ == '__main__':
    # Here to test the program
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)
    # tim.withdraw(60)
    tim.show_balance()