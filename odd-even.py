i = 1
while i > 0:
    the_box = {1: {},
            2: {}}
    # dic1 add even/odd, and dict2 the number inserted
    def picka():
        a = input("odd or even: ")
        the_box[1]= a
        # print("You've picked: " + a)
    picka()
    def rand():
        import random
        return random.randint(1, 100)
    rand()
    def game_on():
        num1 = int(input("pick a number: "))
        num2 = rand()
        return num1 + num2
    s = game_on()
    def even_odd():
        the_box[2]= s
        if (s % 2) == 0:
            print("{0} is even".format(s))
            the_box[3]= "even"
        else:
            print("{0} is odd".format(s))
            the_box[3] = "odd"
    even_odd()
    def finals():
        if the_box[1] == the_box[3]:
            print("You Won")
        else:
            print("You Lose")
    finals()
    print(the_box)