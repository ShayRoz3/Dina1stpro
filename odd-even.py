i = 1
while i > 0:
    the_box = {1: {},
            2: {}}
    # dic1 add even/odd, and dict2 the number inserted
    def picka():
        a = input("odd or even: ")
        # print("You've picked: " + a)
        the_box.update({1: a})
    picka()
    def rand():
        import random
        r = random.randint(1, 100)
        return r
    x = rand()
    def game_on():
        num1 = int(input("pick a number: "))
        num2 = x
        return num1 + num2
    s = game_on()
    def even_odd():
        if (s % 2) == 0:
            the_box.update({2: s})
            print("{0} is even".format(s))
        else:
            the_box.update({2: s})
            print("{0} is odd".format(s))
    even_odd()
    def finals():
        if ({1: s} == {2: s}):
            print("You Won")
        else:
            print("You Lose")
    finals()
    print(the_box)
    # odd == odd => says i lost, y?