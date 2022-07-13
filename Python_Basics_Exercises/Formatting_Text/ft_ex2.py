# Napisz program, który będzie wyświetlał zadane zdanie, co trzecie będzie napisane wielkimi literami,
# a co 4 będzie posiadało wykrzyknik na swoim końcu. (Tylko nie opowiadaj kłamstw! ;)
# Write a program which will repeat the input sentence - every third sentence will be written in big letters
# and every fourth will have an exclamation mark.


def snake_talk(x, number_repetitions):
    for i in range(number_repetitions):
        current_sentence = x
        while i > 0:
            if i == 1:
                print(x)
            if i == 2:
                print(current_sentence * 2)
            if i % 3 == 0:
                print(current_sentence.upper())
            if i % 4 == 0:
                print(current_sentence + "!")
            print(current_sentence)
            break
        else:
            print("input correct number of repetitions.")


# TODO: Dawid - how to bring up error messages when a) a non integer put in, b) an impossible number of repetiotions made.


x = str(input("Input text:"))
y = int(input("Write amount of repetitions:"))

snake_talk(x, y)
