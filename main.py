from math import *
import useful
import time

# Quadratic Calculator Version 1.5
# supports discriminant values up to 1 trillion


print("ax^2 + bx + c = 0\n")

a = input("Value of a: ")
b = input("Value of b: ")
c = input("Value of c: ")

start = time.time()

print("")

if a == "-0" or b == "-0" or c == "-0":
    print("Why would you ever use -0?\nTry again.")
    quit()

# checking for non-floats
try:
    a = float(a)
    b = float(b)
    c = float(c)
except ValueError:
    print("Try again with numbers.")
    quit()


# converting decimals to integers
if useful.check_int(a) == 1 or useful.check_int(b) == 1 or useful.check_int(c) == 1:
    while useful.check_int(a) == 1 or useful.check_int(b) == 1 or useful.check_int(c) == 1:
      a = round(a * 10, 8)
      b = round(b * 10, 8)
      c = round(c * 10, 8)

# simplifying a, b, and c by dividing out the gcf
a = useful.convert_int(a)
b = useful.convert_int(b)
c = useful.convert_int(c)
gcf = useful.simplify(a, b, c)

a = a // gcf
b = b // gcf
c = c // gcf

if a < 0:
    a = -a
    b = -b
    c = -c

# checking unique cases
if a == 0:
    if b == 0 and c != 0:
        c = useful.convert_int(c)
        print("No solution.\nHow do you expect " + str(c) + " to equal 0?")
    elif b == 0 and c == 0:
        print("Infinite solutions.\n0 = 0.")
    elif c == 0:
        print("x = 0")
    else:
        fraction_ans = -c / b
        useful.one_root(fraction_ans)
    quit()

if b == 0:
    fraction = -c / a
    if fraction > 0:
        root_fraction = sqrt(fraction)
        root_fraction = useful.convert_int(root_fraction)
        if floor(sqrt(abs(fraction))) != sqrt(abs(fraction)):
            print("x = ± √" + str(fraction))
            print("x = ± " + str(root_fraction))
        else:
            print("x = ± " + str(root_fraction))
    elif c == 0:
        print("x = 0")
    else:
        fraction = useful.convert_int(fraction)
        abs_fraction = sqrt(abs(fraction))
        abs_fraction = useful.convert_int(abs_fraction)
        if type(fraction) == int:
            print("x = ± i√" + str(abs(fraction)))
            print("x = ± " + str(abs_fraction) + "i")
        else:
            print("x = ± " + str(abs_fraction) + "i")
    quit()

# defining variables
discriminant = (-(4 * a * c) + pow(b, 2))
denominator = 2 * a
root_ans = ""
in_root = 1
out_root = 1
real = (-b / denominator)
imaginary = (sqrt(abs(discriminant)) / denominator)
real = useful.convert_int(real)
imaginary = useful.convert_int(imaginary)
number = abs(discriminant)

if discriminant >= 0:
    ans1 = str((-b + sqrt(discriminant)) / denominator)
    ans2 = str((-b - sqrt(discriminant)) / denominator)


# simplifying the radical and fraction
if discriminant != 0:
    number = useful.convert_int(number)
    answers = []
    index = 0

    # finding the prime factorization of the discriminant
    try:
      while number != 1:
        count = 0
        while number % useful.prime[index] == 0:
          number = number / (useful.prime[index])
          if count == 0:
            answers.append(1)
          else:
            answers[index] += 1
          count += 1
        if count == 0:
          answers.append(0)
        index += 1
    except IndexError:
          if discriminant > 0:
            useful.dec_only(ans1, ans2)
          else:
            useful.complex_num(real, imaginary)
          quit()

    # finding the values of in_root and out_root
    index = 0
    for index in range(len(answers)):
        if answers[index] == 1:
            in_root = in_root * useful.prime[index]
        elif answers[index] > 1:
            if answers[index] % 2 == 0:
                out_root = out_root * (pow(useful.prime[index], answers[index] / 2))
            elif answers[index] % 2 == 1:
                in_root = in_root * useful.prime[index]
                out_root = out_root * (pow(useful.prime[index], (answers[index] - 1) / 2))
  
    # converting from a float to an integer
    b = useful.convert_int(b)
    in_root = useful.convert_int(in_root)
    out_root = useful.convert_int(out_root)
    denominator = useful.convert_int(denominator)
    
    gcf = useful.simplify_fraction(b, out_root, denominator)
    
    b = int(b / gcf)
    out_root = int(out_root / gcf)
    denominator = int(denominator / gcf)
    
# two real solutions
if discriminant > 0:
    if denominator == 1 and out_root == 1:
        root_ans = ("(" + str(-b) + " ± √" + str(in_root) + ")")
    elif denominator == 1:
        root_ans = ("(" + str(-b) + " ± " + str(out_root) + "√" + str(in_root) + ")")
    elif out_root == 1:
        root_ans = ("(" + str(-b) + " ± √" + str(in_root) + ")" + " / " + str(denominator))
    else:
        root_ans = ("(" + str(-b) + " ± " + str(out_root) + "√" + str(in_root) + ")" + " / " + str(denominator))
    if floor(sqrt(discriminant)) != sqrt(discriminant):
        print("x = " + str(root_ans))
        print("x = " + str(ans2) + ", " + str(ans1))
    else:
        useful.dec_only(ans2, ans1)

# one solution
elif discriminant == 0:
    useful.one_root(ans1)

# two imaginary solutions
else:
    if denominator == 1 and out_root == 1:
        root_ans = ("(" + str(-b) + " ± i√" + str(in_root) + ")")
    elif denominator == 1:
        root_ans = ("(" + str(-b) + " ± i" + str(out_root) + "√" + str(in_root) + ")")
    elif out_root == 1:
        root_ans = ("(" + str(-b) + " ± i√" + str(in_root) + ")" + " / " + str(denominator))
    else:
        root_ans = ("(" + str(-b) + " ± " + str(out_root) + "i√" + str(in_root) + ")" + " / " + str(denominator))

    if floor(sqrt(abs(discriminant))) != sqrt(abs(discriminant)):
        useful.one_root(root_ans)
    useful.complex_num(real, imaginary)

end = time.time()
print("")
tatty = round(1000 * float(end - start), 5)
print("This took " + str(tatty) + " milliseconds.")
