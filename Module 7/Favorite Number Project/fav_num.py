#! python3

import os

favnum_file = open('fav_num.txt', 'w')

print('Hello! What is your name?')
name = input()

print('Nice to meet you ' + name + '! \nWhat is your favorite number?')
fav_num = input()

favnum_file.write(name + "'s favorite number is: " + fav_num)

favnum_file.close()
