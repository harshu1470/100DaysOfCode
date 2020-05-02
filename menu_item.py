class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price 
    def info(self):
        return self.name + ' :  $' + str(self.price) 
    def get_total_price(self,count):
        total_price = self.price*count
        if count >=3:
            discount=0.9
            total_price*=discount
        return round(total_price)
