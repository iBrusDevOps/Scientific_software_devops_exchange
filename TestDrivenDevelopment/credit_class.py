class CreditCard:
    """A credit class. 
    
    The initial balance is zero. 
    Inspireation taken from Data Structure and Alogrithms in Python"""
    customer: str
    balance: float
    limit: float 

    def __init__(self, customer, balance, limit):
        self.customer = customer
        self.balance = balance
        self.limit = limit

    
    def charge(self, price):
        """Charges given price to the card, assuming succficient credit limit"""
        if price + self.balance > self.limit:
            return False
        # else:
        #     self.balance+=price 
        #     return True
        

