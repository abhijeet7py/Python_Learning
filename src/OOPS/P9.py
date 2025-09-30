class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    # Greater than
    def __gt__(self, other):
        return self.price > other.price

    # Less than
    def __lt__(self, other):
        return self.price < other.price

    # Equal to
    def __eq__(self, other):
        return self.price == other.price

    # Not equal to
    def __ne__(self, other):
        return self.price != other.price

    # Greater than or equal
    def __ge__(self, other):
        return self.price >= other.price

    # Less than or equal
    def __le__(self, other):
        return self.price <= other.price

    def __str__(self):
        return f"{self.item} (₹{self.price})"


# --- Taking input from user ---
item1 = input("Enter first item: ")
price1 = int(input("Enter price of first item: "))

item2 = input("Enter second item: ")
price2 = int(input("Enter price of second item: "))

odr1 = Order(item1, price1)
odr2 = Order(item2, price2)

# --- Comparisons ---
print("\nComparisons:")
print(f"{odr1} > {odr2}  ➝  {odr1 > odr2}")
print(f"{odr1} < {odr2}  ➝  {odr1 < odr2}")
print(f"{odr1} == {odr2} ➝  {odr1 == odr2}")
print(f"{odr1} != {odr2} ➝  {odr1 != odr2}")
print(f"{odr1} >= {odr2} ➝  {odr1 >= odr2}")
print(f"{odr1} <= {odr2} ➝  {odr1 <= odr2}")
