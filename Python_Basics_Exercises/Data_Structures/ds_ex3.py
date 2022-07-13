# Napisz funkcję (lub program), która sprawdzi czy podany Pesel posiada poprawną sumę kontrolną.

def check_pesel():
    y = input("Enter PESEL:")
    list = []
    for i in y:
        list.append(i)

    if len(list) != 10:
        print(f"Incorrect PESEL")


    else:
        print("Thank you")


check_pesel()

def check_pesel_correctness(pesel):
    pesel_list = [int(number) for number in str(pesel)]

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    if len(pesel_list) != 11:
        return False

    control_sum = sum([a*b for a, b in zip(pesel_list[:-1], weights)])

    control_number = 10 - [int(number) for number in str(control_sum)][-1]

    print(control_number)

    if pesel_list[-1] != control_number:
        return False

    return True



pesel = '02070803628'
print(check_pesel_correctness(pesel))
#
# TODO: check method and alternatives with Dawid


