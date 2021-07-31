#write a function to calculate y=0 for a quadratic equation
#y = ax**2 + bx + c
import math
def sqr_fnct(a,b,c):
    if a ==0:
        print("enter a quadratic equation")
    delta = b ** 2 - (4 * a * c)
    if delta < 0:
        print("No answer")
    if delta >0:
        x_1 = (-b - math.sqrt(delta)/2*a)
        x_2 = (-b + math.sqrt(delta)/2*a)
        print(f"Two answers, x_1 = {x_1}, x_2 = {x_2}")
    elif delta ==0:
        print(f"One answer, x = {x_1}")

sqr_fnct(1,-6,8)