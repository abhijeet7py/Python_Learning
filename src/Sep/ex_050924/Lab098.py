# Multilevel inheritance

class GrandFther:
    gold = "2 Kg"
    def BHK1(self):
        print("1 BHK")

class Father(GrandFther):
    diamond = "22 k"
    def BHK2(self):
        print("2 BHK")

class Father2(GrandFther):
    car = "Alto"

class Son(Father):
    btc = "1 BTC"
    def BHK3(self):
        print("3 BHK")

s = Son()
f = Father()
f2 = Father2()
print(f2.gold,f2.car,f2.BHK1())
gf = GrandFther()
