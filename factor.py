#!/usr/local/bin/python3


def check_factorable(a, b):
    # start at -10 and brute force look for an answer
    for x in range(-10, abs(b), 1):
        for y in range(-10, abs(b), 1):
            xpy = x+y
            xty = x*y

            # uncomment these if you want to see the checks run...
            print("x,y=" + str(x) + "," + str(y) + ";x+y=" + str(xpy) +
                  ";x*y=" + str(xty))

            if(xpy == a and xty == b):
                return x, y
    return


def print_answer(c2, c3, val1, val2):
    print("Is following factorable: (x^2+" + str(c2) + "x + " + str(c3) + ")")
    if val1 == -1:
        print("No: not factorable")
        return

    # print the answer when the equation can be factored
    print("Yes: (x + " + str(val1) + ")(x + " + str(val2) + ")")


# main will check if this be factored?   x^2 + a*x + b
def main(a, b):
    v1, v2 = check_factorable(a, b)
    print_answer(a, b, v1, v2)


# run this program
main(-7, 12)
print("\n\nfactor.py done")
