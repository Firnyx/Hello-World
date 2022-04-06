a = 1
b = 2
print("oui") if a < b else print("non")                         # simplifier la syntaxe
if a > b : print("zourbg")

fruits = ["apple", "banana", "cherry"]                          # avec  continue   , le print(x) est sauté lorsque x == "banana" (mais la boucle ne s'arrête pas)
for x in fruits:
  if x == "banana":
    continue
  print(x)

fruits = ["apple", "banana", "cherry"]                           # break permet d'arrêter la boucle avant que tous les éléments n'aient été boucler
for x in fruits:
  if x == "banana":
    break
  print(x)

#continue et break fonctionnent de la même manière avec la boucle while

for x in range(6):                                               # permet de définir le nombre d'élément qui seront "bouclés"
  print(x)

for x in range(2, 30, 4):                                         # la troisième valeur permet d'implémenter un saut de chiffres (ici va de 2 à 30 en sautant de 4 en 4)
      print(x)

for x in range(6):                                                # else s'éxécute lorsque la boucle est terminée ( ne fonctionne pas si stoppée par break )
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:                                                      #la "boucle intérieure" sera exécutée une fois pour chaque itération de la "boucle extérieure"
   for y in fruits:                                                 # => red apple : red banana : red cherry : big apple... etc
    print(x, y)

# Les Fonctions

def un_essai(*légumes) :                                           # une étoile * devant l'argument de la fonction (simplifié *args) permet de ne pas préciser le nombre d'arguments
   print("moi je préfère " +légumes[2])

un_essai("PATATE","tomate","les poireaux")

def un_essai2(poisson,viande,oeuf):                                # on utilise la syntaxe  key = value
    print("je préfère manger "+ oeuf)

un_essai2(poisson = "Saumon", viande = "boeuf",oeuf = "des poules") # renvoie => je préfère manger des poules

def un_essai3(**argm):                                              # **kwargs => un mélange de * et key = value
    print ("je voilà " + argm["euh"])

un_essai3(bien = "bine", euh = "bine")

def un_essai4(pays = "France") :                                     # "France" est une valeur par défaut qui s'active si rien n'est spécifié () lorsque la commande est éxécuté
    print( "je viens de " + pays)

def un_essai5(fruits):                                               # on peut aussi utiliser des listes en tant qu'arguments
    for x in fruits:
      print(x)

légumez = ["manger","boire","dormir"]
un_essai5(légumez)

def un_essai6(x) :                                                  # la fonction renvoie une valeur
    return x * 3

print(un_essai6(3) + 1)

# la recursion : nope

# lambda

x = lambda a : a + 10                                                # On a :  lambda arguments : expression
x = lambda a, b , c : a * b + c                                      # peut avoit plusieurs arguments

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)                                                # myfunc(2) va correspondre à n
mytripler = myfunc(3)
print(mydoubler(11))                                                 # mydoubler(11) correspond à l'argument a
print(mytripler(11))
# => mydoubler(11) renvoie donc 2*11 = 22 et mytripler(3) renvoie 33

# les classes
# Les classes permettent de créer des objets
class MyClass:                                                       # permet de créer un classe ( ici nommée Myclass)
  y = 5

p1 = MyClass()
print(p1.y)                                                          # renvoie 5

class thefire():
  z = ["ookay"]
  b = 5

objet = thefire()
print(objet.z)                                                       # renvoie ["okay"]
print(objet.b)                                                       # renvoie b


class Individu:
  def __init__(self, nom, age, taille):
    self.nom = nom
    self.age = age
    self.taille = taille
  def __str__(self):
      return "je m'appelle " + self.nom

x = Individu("Robert", 36, "1 mètre 60")                            # objet créé
print(x.nom)
print(x.age)
print(x.taille)
print(x)

del x.age                                                           # supprimer un attribut de l'objet
del x                                                               # supprimer l'objet

# héritage








