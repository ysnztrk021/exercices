
# # -------------------------------VARIABLES---------------------------------
# # Ne modifiez que les lignes commençant par ICI
# # Créez une variable nommée number et assignez-lui la valeur 10
# number = 10
# # ICI
# print("number vaut", number)

# # Décrémentez sa valeur par 2
# number -= 2
# # ICI
# print("Apres decrementation, number vaut", number)

# # Créez une autre variable nommée square valant le carré de number
# square = number**2
# # ICI
# print("square vaut", square)

# # Créez une dernière variable nommée root valant la racine carrée de number
# root = number**0.5
# # ICI
# print("root vaut", root)

# # Faites une division entière de root par 2 et affichez le résultat
# root = root//2
# # ICI
# print("root vaut",root)

# #--------------------------------------------------------------------------

# # TYPE

# # Ne modifiez que les commentaires commenÃ§ant par ICI

# # Sans utiliser la fonction type(), donnez le type des variables suivantes
# i = 7.5 * 3  # float
# j = 8.2 // 2  # float
# k = "\n"  # str
# l = False  # bool
# m = 3 * k  # str
# n = 3 > 2  # bool
# o = 0 * 10.5  # float
# p = 2 ** 5  # int
# q = str(n) * int(i)  # str
# r = i == j  # bool
# s = [1, 2, 3]  # list
# t = (1, 2, 3)  # tuple
# u = {1, 2, 3}  # set
# v = [i for i in range(10)]  # list
# w = s in v  # bool

# #--------------------------------------------------------------------------

# # PRINT

# # Ne modifiez que les lignes commençant par ICI

# # Affichez les 3 variables suivantes sur
# # 3 lignes différentes avec un seul appel à print()
# i = 1
# j = False
# l = [i, j]

# # ICI
# print(f"{i}\n{j}\n{l}")
# print(i,j,l, sep="\n")

# # Affichez les mêmes 3 variables sur la même ligne.
# # Vous devez utiliser un appel à print() par variable

# # ICI
# print(i, end=" ")
# print(j, end=" ")
# print(l)

# #--------------------------------------------------------------------------

# # F-PRINT

# # Créons quelques variables
# name = "Mounir"
# age = 25

# # Affichage classique
# print("Affichage classique : ")
# print("Bonjour, je suis", name, "et j'ai", age, "ans")
# print()

# # Affichage avec des f-strings
# print("Affichage avec f-strings :")
# print(f"Bonjour, je suis {name} et j'ai {age} ans")
# print()

# # Utilisation de len dans le f-string
# print("Utilisation de len dans le f-string")
# print(f"Mon nom {name} contient {len(name)} lettres")
# print()
# # Utilisation d'opérations dans le f-string
# print("Utilisation d'opérations dans le f-string")
# print(f"Mon nom {name} contient {3+3} lettres")
# print()

# # Créons à présent une variable float

# my_float = 3.1415196

# # Affichons cette variable avec seulement 2 chiffres décimaux

# print(f"{my_float:.2f}")

# # Affichons maintenant 3 chiffres décimaux

# print(f"{my_float:.3f}")

# # N'affichons que la partie entière

# print(f"{my_float:.0f}")

# # Créons deux dernières variables

# big_number = 10_000
# small_number = 0.000014523

# # Affichons-les en notation scientifique

# print(f"{big_number:e} est plus grand que {small_number:e}")

# # Affichons juste leur ordre de grandeur

# print(f"{big_number:.0e} est plus grand que {small_number:.0e}")
# print(f"{big_number:.0e} est plus grand que {small_number:.0e}")

# #--------------------------------------------------------------------------

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

# # -------------------------------LISTS-------------------------------------

# # 1

# a=[1,2,3,4]
# print(a[0],a[len(a)])

# # -------------------------------------------------------------------------

# # 2

# a=[0,1,2,3,4,5]

# for i in a:
#     if i>0:
#         print(i)

# # -------------------------------------------------------------------------

# # 3

# semaine = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
# week_end=[]
# for i in semaine:
#     if i == 'Samedi' or i=='Dimanche':
#         week_end.append(i)

# print(' '.join(week_end))


# # -------------------------------------------------------------------------

# # 4

# numbers = [1,2,3,4]
# n = 0
# for i in numbers:
#     n+=i
# print(n)

# # -------------------------------------------------------------------------

# # 5

# for i in range(0,101):
#     if i%3==0 and not i%2==0:
#         print(i)

# # -------------------------------------------------------------------------

# # 6

# liste=[17,38,10,25,72]

# # -------------------------------------------------------------------------

# # a

# liste.sort()

# print(liste)

# # -------------------------------------------------------------------------

# # b

# liste.append(12)

# print(liste)

# # -------------------------------------------------------------------------

# # c

# liste.reverse()

# print(liste)

# # -------------------------------------------------------------------------

# # d

# print(liste.index(17))

# # -------------------------------------------------------------------------

# # e

# liste.pop(1)

# print(liste)

# # -------------------------------------------------------------------------

# # f

# print(liste[1:3])

# # -------------------------------------------------------------------------

# # g

# print(liste[:2])

# # -------------------------------------------------------------------------

# # h

# print(liste[2:])

# # -------------------------------------------------------------------------

# # i

# print(liste[:])

# # -------------------------------------------------------------------------

# # j

# print(liste[-2])

# # -------------------------------------------------------------------------

# # 7

# liste = [1,1,2,2,3,3,4,4,'5','5','5',5]

# maxi = 0
# leChiffre=0

# for i in liste:
#     if maxi<liste.count(i):
#         maxi=liste.count(i)
#         leChiffre=i

# print(f"Voici ma liste {liste}")
# print(f"Le chiffre {leChiffre} apparait {maxi} fois")

# # -------------------------------------------------------------------------

# # 8

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# for i in range(len(my_list)-1):
#     print(my_list[i : i+2])