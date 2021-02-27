#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# greet user
userName = input("Comment tu t'appelle? : ")
print('Bonjour '+userName)

# gauge how user is feeling (requiring answer between 0 & 10)
while True:
    try:
        userFeeling = int(input("Comment ca va? (1-10): "))
        if userFeeling == 10:
            print('trés bien')
        elif userFeeling >= 7:
            print('bien')
        elif userFeeling >= 5:
            print('bof')
        elif userFeeling >= 3:
            print('pas trés bien')
        elif userFeeling >= 0:
            print('pas bien')
        break
    except: 
        print('je veux un réponse entre 0 et 10')

# offer to multiply numbers
if userFeeling <= 6:
    multiplyQuestion = "puis-je multiplier deux chiffres pour vous élever l' humeur " + userName +"?"  
else:
    multiplyQuestion = "tu veux multiplier des nombres " + userName +"?"  
multiplying = input(multiplyQuestion + " (o/n): ")
if multiplying == 'o':
    while True:
        try:
            multiple1 = float(input("apport un nombre sil vous plais: "))
            break
        except:
            print('je veux un nombre (1, 5, 7.28, etc)')
    while True:
        try:
            multiple2 = float(input("apport un deuxiéme nombre sil vous plais: "))
            break
        except:
            print('je veux un nombre (1, 5, 7.28, etc)')
    print(str(multiple1) + " x " + str(multiple2) + " = " + str(multiple1*multiple2))
