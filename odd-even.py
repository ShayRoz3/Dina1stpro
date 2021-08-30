the_box = {1: {},
           2: {}}
# dic1 add even/odd, and dict2 the number inserted
def picka():
    a = input("Odd or Even: ")
    # print("You've picked: " + a)
    the_box.update({1:a})
picka()
def chu():
    import random
    r = random.randint(1, 100)
    print(r)
chu()
# def even_odd():
#     num1 = input("pick a number:")
#     num2 = input("pick a number:")
#     a = int(num1) + int(num2)
#     if (a % 2) == 0:
#         the_box.update({2:a})
#         print("{0} is even".format(a))
#     else:
#         the_box.update({2:a})
#         print("{0} is Odd".format(a))
# even_odd()
def game_on():
    num1 = input("pick a number: ")
    num2 =
game_on()
print(the_box)