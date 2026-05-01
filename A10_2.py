var1 = int(input("Enter a number: "))
var2 = int(input("Enter a number: "))
def divisible_by(numerator, denominator):
    if numerator % denominator == 0:
        print("True")
    else:
        print("False")
divisible_by(var1, var2)
