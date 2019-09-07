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





try:
    file = open('file.txt', 'r')
    content = file.read()
    print(content)
except Exception as error:		## Exception是其他所有非系统异常的基类,能够匹配任意非系统异常
    print('[ERROR] {}'.format(error))
finally:
    print('program end')

print('continue running...')
number = [1, 2, 3, 4, 5]
for element in number:
    if element % 2 == 0:
        print(element)



#except:          ##无内容，捕捉所有异常
    print('Other error')



##自定义跑出异常
class MyInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} is invalid input'.format(self.value)


try:
    string = input('>>>Input: ')
    if 'abcd' in string:
        raise MyInputError(string) #收集异常
    else:
        print(string)
except MyInputError as error:
    print(error)