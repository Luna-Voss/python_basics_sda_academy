# Zaprojektuj klasę Rational, reprezentującą liczby wymierne jako pary liczb całkowitych (licznik i mianownik).
#
# Klasa powinna zawierać wiele stworzonych metod magicznych i funkcjonalnie umożliwiać:
#
#     Wyświetlać liczbę 0.5 w postaci ½ - wymagana poprawna implementacja str oraz repr.
#
#     Metoda float powinna zwracać liczbę w postaci dziesiętnej, a int analogicznie do swojego odpowiednika w przypadku liczb typu float. Dodatkowo metodę invert.
#
#     Metody porównujące (eq, lt, gt, le, ge, cmp) powinny uwzględniać, że ½ = 2/4.
#
#     Operatory +,-,*,/ powinny zostać zaimplementowane prawidłowo i zwracać nowy obiekt tej klasy.
#
#     Powinna być możliwość zapisu bieżącego wyniku do pliku oraz jego wczytywania.
#
#     Klasa powinna zawsze starać się przechowywać skróconą wersję ułamka.
#


# x = 0,674  -> L/M
# jeżeli x będzie int => L = x, M = 1
#
# temp = 0
# pętla:
# temp = x*10
# M = M * 10
# jeżeli temp będzie int
# przerwij pętlę
# nie:
# kontynuuj
#
# x.is_integer()




# def into_fraction(x):
#     l = x
#     m = 1
#     while l.is_integer() == False:
#         l = l*10
#         m = m*10
#     else:
#         return print(f"{int(l)}/{m}")
#
# into_fraction(0.5)
#
# def simplify_fraction(x)
class Rational:
    #zmienne klasy
    # float_representation:float
    # fraction_numerator:int
    # fraction_denominator:int

    #konstruktor - zmienne obiektu
    def __init__(self, x:float):
        self.float_representation = x
        self.fraction_numerator = 0
        self.fraction_denominator = 0
        self.into_fraction(x)
        self.simplify_fraction()


    def into_fraction(self, x:float):
        l = x
        m = 1
        while not l.is_integer():
            l = l*10
            m = m*10
        self.fraction_numerator = int(l)
        self.fraction_denominator = int(m)


    def nwd_i(self, a, b):
        while b:
            temp = a
            a = b
            b = temp%b
        return a

    def simplify_fraction(self):
        nwd = self.nwd_i(self.fraction_numerator, self.fraction_denominator)
        self.fraction_numerator = self.fraction_numerator // nwd
        self.fraction_denominator = self.fraction_denominator // nwd


    # to string
    def to_string(self):
        pass

    #def float
    def float(self):
        pass

    #def int
    def int(self):
        pass

    #def invert:
    def invert(self):
        pass

    #def eq
    def eq(self):
        pass

    #def lt
    def lt(self):
        pass
    #def gt
    def gt(self):
        pass
    #def le
    def le(self):
        pass

    #defge
    def ge(self):
        pass

    #def cmp
    def cmp(self):
        pass

    def __add__(self, o):
        pass

   #operator -
    def __sub__(self,o):
        pass
   #operator *
    def __mul__(self, o):
        pass

#operator /
    def __truediv__(self, o):
        pass
    #zapisywanie do plików
    def to_file(self):
        pass


a = Rational(0.68)
b = Rational(0.56)




























#
# class Rational:
#     def __init__(number, decimal, fraction):
#         number.decimal = decimal
#         number.fraction = fraction
#
#     def fraction(number):
#         x = number.decimal * 10
#         y = 10/x
#         repr(str(1/y))

import json
from math import gcd
#
# class Rational:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#         self.to_irreducible_fraction()
#
#     def to_irreducible_fraction(self):
#         greatest_common_divisor = gcd(self.numerator, self.denominator)
#         while greatest_common_divisor != 1:
#             self.numerator = self.numerator // greatest_common_divisor
#             self.denominator = self.denominator // greatest_common_divisor
#             greatest_common_divisor = gcd(self.numerator, self.denominator)
#
#     def __str__(self):
#         if self.denominator == 1:
#             return str(self.numerator)
#         else:
#             return str(self.numerator) + "/" + str(self.denominator)
#
#     def __repr__(self):
#         items = (f"{k}={v}" for k, v in self.__dict__.items())
#         return f"{self.__class__.__name__}({', '.join(items)})"
#
#     def __add__(self, other):
#         numerator = self.numerator * other.denominator + self.denominator * other.numerator
#         denominator = self.denominator * other.denominator
#
#         return Rational(numerator, denominator)
#
#     def __sub__(self, other):
#         numerator = self.numerator * other.denominator - self.denominator * other.numerator
#         denominator = self.denominator * other.denominator
#
#         return Rational(numerator, denominator)
#
#     def __mul__(self, other):
#         return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
#
#     def __truediv__(self, other):
#         return self * ~other
#
#     def __lt__(self, other):
#         return self.__cmp__(other) < 0
#
#     def __le__(self, other):
#         return self.__cmp__(other) <= 0
#
#     def __gt__(self, other):
#         return self.__cmp__(other) > 0
#
#     def __ge__(self, other):
#         return self.__cmp__(other) >= 0
#
#     def __eq__(self, other):
#         return self.__cmp__(other) == 0
#
#     # Compare two numbers
#     def __cmp__(self, other):
#         temp = self - other
#         if temp.numerator > 0:
#             return 1
#         elif temp.numerator < 0:
#             return -1
#         else:
#             return 0
#
#     def __invert__(self):
#         return Rational(self.denominator, self.numerator)
#
#     def __float__(self):
#         return self.numerator/self.denominator
#
#     def __int__(self):
#         return int(float(self))
#
#     def save(self, filename):
#         with open(filename, 'w') as f:
#             json.dump(self.__dict__, f)
#
#     def load(self, filename):
#         with open(filename, 'r') as f:
#             loaded_dict = json.load(f)
#         self.numerator = loaded_dict['numerator']
#         self.denominator = loaded_dict['denominator']
#
#
