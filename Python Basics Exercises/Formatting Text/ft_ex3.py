#Write a function that will count the number of vowels in a given string
from collections import Counter


def num_vowels(string):
    vowels = ["a","e", "i", "o","u"]
    working_list = []
    for letter in string:
        if letter in vowels:
            working_list.append(letter)
    print(len(working_list))

num_vowels("how many vowels")


#using counter

def num_vowels_counter(string):
    vowels = {"a", "e", "i", "o", "u"}
    c = Counter(string)
    sum = 0
    for key, item in c.items():
        if key in vowels:
            sum += 1
    print(sum)
num_vowels_counter("hahahahaha lol")

#TODO: Dawid explain counter.
