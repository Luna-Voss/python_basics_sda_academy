#Write a program which will allow you to compare the price of pizza in relation to its area.

def area_vs_price(r, price):
    return (3.142*r**2)/price

r1 = 15.2
r2 = 18
price1 = 10
price2 = 15.5

print(area_vs_price(r1,price1))
print(area_vs_price(r2,price2))