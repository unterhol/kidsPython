#!/usr/local/bin/python3


def check_factorable(a, b):
    # start at -10 and brute force look for an answer
    for x in range(-abs(b), abs(b), 1):
        for y in range(-abs(b), abs(b), 1):
            xpy = x+y
            xty = x*y

            # uncomment these if you want to see the checks run...
            # print("x,y=" + str(x) + "," + str(y) + ";x+y=" + str(xpy) +
            #       ";x*y=" + str(xty))

            if(xpy == a and xty == b):
                return x, y
    return


def get_term(value):
    if value < 0:
        return "- "+str(abs(value))

    return "+ " + str(value)


def print_answer(c2, c3, val1, val2):
    print("Is following factorable: (x^2 " + get_term(c2) + "x " + get_term(c3) + ")")
    if val1 is None:
        print("No: not factorable")
        return

    # print the answer when the equation can be factored
    print("Yes: (x " + get_term(val1) + ")(x " + get_term(val2) + ")")


# main will check if this be factored?   x^2 + a*x + b
def main(a, b):
    answer = check_factorable(a, b)

    if answer is None:
        n1 = None
        n2 = None
    else:
        n1 = answer[0]
        n2 = answer[1]
    
    print_answer(a, b, n1, n2)


# run this program
main(-9, -22)

print("\n\nfactor.py done")
