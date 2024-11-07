import time
import datetime
class Store:
    def __init__(self,products):
        self.products=products
    def buy(self):
        b=input("what produc do you buy?")
        self.products.append(b)
        print(self.products)
    def sell(self):
        s=input("what produc you want to sell?")
        self.products.remove(s)
        print(self.products)
    def changing(self):
        c=input("what produc do remove ?")
        g=input("what produc do you replace?")
        self.products.remove(c)
        self.products.append(g)
        print(self.products)
    def show(self):
        print(self.products)
    def now_time(self):
        print(time.ctime())
    def now_date(self):
        print(datetime.datetime.today())


p0=Store([])
while True:
    i=int(input("Enter a number 0 of 6:"))
    if i==0:
        print("closed!")
        break

    elif i==1:
        p0.buy()

    elif i==2:
        p0.sell()

    elif i==3:
        p0.changing()

    elif i==4:
        p0.show()

    elif i==5:
        p0.now_time()

    elif i==6:
        p0.now_date()

    else:
        print("unvalid!")


