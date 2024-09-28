def make_pizza (*toppings, base):
    print(toppings,base)

amit = make_pizza("Mushroom","Tomato","Cheese",base = "Thin crust")


def make_pizza2(base, *toping):
    print(base,toping)

make_pizza2(base="crust", "fywbd")

