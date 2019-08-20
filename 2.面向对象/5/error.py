#!/usr/bin/env python3

#usage:error study
#date:190819
#author:Distantskyline


import random


def verificationCode(number):
    """
    product verification code of user input number
    :param number: verification code's number
    :return: verification code
    """
    vCode = ''
    for n in range(number):
        nums = random.randint(0, 9)
        word = chr(random.randint(65, 90))
        middle = random.choice([nums, word])
        vCode += str(middle)
    return vCode


verCode = verificationCode(4)
print(verCode)
userInput = input('Please input verification code: ')
if userInput.lower() != verCode.lower():
    print('your Stupid !')
else:
    print('please load...')