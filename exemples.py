# def remove_first_last(my_list):
#     if len(my_list) < 1:
#         raise ValueError("Votre liste doit avoir au moins 2 éléments")
#     my_list2 = my_list[1:-1]
#     return my_list2


# my_list = [1,2,3,4,5]

# print(remove_first_last(my_list))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def count_words(phrase):
#     mots=[]
#     for i in phrase.split():
#         if i[0].isalpha():
#             mots.append(i)
#     print('Votre phrase comporte',len(mots),'mots')
#     print(mots)

# phrase = "Bonjour je suis M122233"

# count_words(phrase)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def divide(x,y):
#     try:
#         print(int(x)/int(y))
#     except ValueError:
#         print("Vous devez entrer un nombre !")
#     except ZeroDivisionError:
#         print("Vous ne pouvez pas diviser un nombre par 0 !")

# x = input("Entrez un nombre : ")
# y = input("Entrez un deuxieme nombre : ")

# divide(x,y)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def get_max(list1, list2):
#     return max(list(set(list1).intersection(list2)))


# number = [2, 3, 10, 39, 49, 99]
# number2 = [44, 20, 49, 100, 304, 193]

# print(get_max(number, number2))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# from random import randint


# def get_password(length):
#     pswd = []
#     for i in range(length):
#         pswd.append(randint(1,100))
#     print(*pswd)

# get_password(20)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# def get_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# celsius = int(input("Saisissez un degrés celsius : "))

# print(get_fahrenheit(celsius))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def tri_bulle(tableau):
#     n = len(tableau)
#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if tableau[j] > tableau[j + 1] :
#                 tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]

# tableau = [64, 34, 25, 12, 22, 11, 90]

# tri_bulle(tableau)

# print(tableau)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def pyramide(height):
#     spaces = height - 1
#     for x in range(0, height):
#         for y in range(0, spaces):
#             print(end=" ")
#         spaces = spaces - 1
#         for z in range(0, x+1):
#             print("* ", end="")
#         print("\r")

# height = 10
# pyramide(height)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def num_min(pswd):
#     lower_case=[]
#     for i in list(pswd):
#         if i.islower():
#             lower_case.append(i)
#     return len(lower_case)

# def num_maj(pswd):
#     upper_case = []
#     for i in list(pswd):
#         if i.isupper():
#             upper_case.append(i)
#     return len(upper_case)

# def num_non_alpha(pswd):
#     non_alpha = []
#     for i in list(pswd):
#         if i.isalpha() == False:
#             non_alpha.append(i)
#     return len(non_alpha)

# def len_maj(pswd):
#     upper=''
#     a=''
#     for x in pswd.split('_'):
#         for y in range(len(x)):
#             if x[y].isupper():
#                 a=a+x[y]
#                 if a in x:
#                     upper=upper+x[y]
#     return len(upper)

# def len_min(pswd):
#     lower=''
#     a=''
#     for x in pswd.split('_'):
#         for y in range(len(x)):
#             if x[y].islower():
#                 a=a+x[y]
#                 if a in x:
#                     lower=lower+x[y]
#     return len(lower)

# def score(pswd):
#     numberOfChar = len(pswd)
#     numberOfUpLet = num_maj(pswd)
#     numberOfLowLet = num_min(pswd)
#     numberOfNonAlphaLet = num_non_alpha(pswd)
#     numberOfLenMin = len_min(pswd)
#     numberOfLenMaj = len_maj(pswd)
#     sumOfPenalities = (numberOfLenMin*2) + (numberOfLenMaj*3)
#     sumOfBonus = (numberOfChar*4)+(numberOfChar-numberOfUpLet)*2+(numberOfChar-numberOfLowLet)*3+(numberOfNonAlphaLet*5)
#     sumOfAll = sumOfBonus - sumOfPenalities

#     return sumOfAll

# def get_strength(pswd):
#     if score(pswd) < 20:
#         return f"Votre mot de passe est très faible {score(pswd)}"
#     elif score(pswd) < 40:
#         return f"Votre mot de passe est faible {score(pswd)}"
#     elif score(pswd) < 80:
#         return f"Votre mot de passe est fort {score(pswd)}"
#     else:
#         return f"Votre mot de passe est très fort {score(pswd)}"


# pswd = input("Tapez un mot de passe : \n")

# print(get_strength(pswd))

# --------------------------------------------------------------PYTHON FILE READING----------------------------------------------------------------------------------------------

# PYTHON FILE READING
# import os
# def write_numbers(file_name, max_numbers=10):
#     lists = []
#     for i in range(max_numbers+1):
#         lists.append(f"{i}")
#     my_str = "\n".join(lists)
#     with open(f"{file_name}", "w+") as f:
#         if os.stat(file_name).st_size == 0: 
#             f.write(my_str)
#         return f.read()


# print(write_numbers('test.txt'))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def get_line(file_name, line_number):
#     num_lines = sum(1 for line in open('test.txt'))
#     if num_lines >= line_number and line_number>=0:
#         try:
#             with open(f"{file_name}","r+") as f:
#                 for position, line in enumerate(f):
#                     if position+1 == line_number:
#                         print(line.strip())
#                 f.close()
#         except FileNotFoundError:
#             print("Ce fichier n'existe pas")
#     else:
#         raise EOFError("Ce fichier n'a pas autant de lignes")

# get_line("test.txt", 11)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def is_in_dico(word):
#     with open("dictionnaire.txt","r+") as f:
#         for line in f:
#             if line.strip()==word.upper():
#                 print(True)
#                 exit()
#         print(False)
        
# word = input("Entrez un mot qui pourrait être dans le dictionnaire : ")
# is_in_dico(word)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import random

# def get_random_word():
#     num_lines = sum(1 for line in open('dictionnaire.txt'))
#     rnd = random.randint(1,num_lines)
#     with open("dictionnaire.txt","r+") as f:
#         for position, line in enumerate(f):
#             if position+1 == rnd:
#                 print(line.strip())
#         f.close()
        
# get_random_word()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import os

# def create_in_file(file_name,dir_name):
#     dir = os.path.join("C:\\","Users","yasin","Documents","Cfitech","python",f"{dir_name}")
    
#     if not os.path.exists(dir):
#         os.mkdir(dir)
    
#     with open(f"{dir}/{file_name}","w+") as f:
#         f.read()
#         f.close()

# create_in_file("test.txt","createdDir")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

