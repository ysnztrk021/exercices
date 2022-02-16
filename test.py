# import random
# # Exercices

# # 1
# num = 0

# for i in range(101):
#     num += i
#     print(num)

# #--------------------------------------------------------------------------

# # 2

# age = int(input("Introduisez votre âge : "))

# if age < 18:
#     print("Vous êtes mineur")
# else:
#     print("Vous êtes majeur")

# #--------------------------------------------------------------------------

# # 3

# bj = ""

# while bj != "Bonjour" :
#     bj = input("Entrez le mot Bonjour : ")

# #--------------------------------------------------------------------------

# # 4

# chance = 2
# bj = input("Entrez Bonjour : ")

# while chance > 0:
#     if bj == "Bonjour":
#         break
#     else:
#         bj = input("Entrez le mot Bonjour : ")
#         chance -= 1

# print("J'abandonne !")

# #--------------------------------------------------------------------------

# # 5

# bcl = "Boucle"

# for i in range(len(bcl)):
#     print(bcl[i],end=" ")

# #--------------------------------------------------------------------------

# # 6

# for i in range(random.randint(1,6)):
#     print('python')

# #--------------------------------------------------------------------------

# # 7

# while True:

#     ask = input("Voulez-vous lancer le dé ? (Oui / Non) : ")

#     if ask == "Oui":
#         de = random.randint(1,6)
#         print(f"Vous avez lancé le dé et vous avez {de}")
#     else :
#         break

# #--------------------------------------------------------------------------

# # 8

# for i in range(random.randint(1,10)):
#     n = random.randint(1,10)
#     print(n)

# #--------------------------------------------------------------------------

# # 9

# for i in range(101):
#     if i%2 == 0:
#         print(i)    

# #--------------------------------------------------------------------------

# # 10

# mdp = ""

# while len(mdp) < 12:
#     mdp = input("Entrez un mot de passe à 12 charactère : ")

# #--------------------------------------------------------------------------

# # 11

# for i in range(random.randint(10,15)):
#     n = random.randint(0,9)
#     print(n,end="")

# #--------------------------------------------------------------------------

# # 12

# ask = input("""
#             Entrez 'dice' pour lancer un dé,\n
#             'sum' pour afficher la somme des nombres compris entre 1 et 100,\n
#             'password' pour afficher entre 10 et 15 aléatoires les nombres compris entre 0 et 9,\n
#             'quit' pour quitter
#             """)
    
# while True: 
    
#     if ask == "dice":
#         de = random.randint(1,6)
#         print(f"Vous avez lancé le dé et vous avez {de}")

#     elif ask == "sum":
#         num = 0

#         for i in range(101):
#             num += i    
#         print(num)

#     elif ask == "password":
#         for i in range(random.randint(10,15)):
#             n = random.randint(0,9)
#             print(n)
            
#     elif ask == "quit":
#         break
            
#     else :
#         ask = input("""
#                 Entrez 'dice' pour lancer un dé,\n
#                 'sum' pour afficher la somme des nombres compris entre 1 et 100,\n
#                 'password' pour afficher entre 10 et 15 aléatoires compris entre 0 et 9,\n
#                 'quit' pour quitter
#                 """)

# # -------------------------------------------------------------------------

# # 13

# a = []

# for i in range(11):
#     a.append(i)
#     for n in a:
#         print(n, end=" ")
#     print("\n")
