i = 1
while i > 0:
    the_box = {1: {},
            2: {}}
    # dic1 add even/odd, and dict2 the number inserted
    def picka():
        dict1 = input("odd or even: ")
        the_box[1] = dict1
        if dict1 != "even" or "odd":
            dict1 = input("odd or even: ")
        else:
            break
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
    game1 = game_on()
    def even_odd():
        the_box[2]= game1
        if (game1 % 2) == 0:
            print("{0} is even".format(game1))
            the_box[3]= "even"
        else:
            print("{0} is odd".format(game1))
            the_box[3] = "odd"
    even_odd()
    def finals():
        if the_box[1] == the_box[3]:
            print("You Won")
        else:
            print("You Lose")
    finals()
    print(the_box)
# is this correct now?