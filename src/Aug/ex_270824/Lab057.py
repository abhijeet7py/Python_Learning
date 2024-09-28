def outer_func():
    var1 = 30
    def inner_func():
        print(var1)

    def inner_func2():
        print(var1)

    inner_func()
    inner_func2()

outer_func()