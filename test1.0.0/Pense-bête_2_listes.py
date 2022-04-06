x = "valeur (pas forcément une chaîne de caractères)"

bool(x)                     #détermine si la valeur/variable ou autre est Vraie ou Fausse (True/False
print(bool(x))

# l'opérateur is est différent de == :
a = 5
b = 5
# avec 'a is b' la console renvoie False alors qu'avec ' a == b' elle renvoie True


# listes
liste = ["oui","non","peut-être"]                      # avec des crochets
thislist = list(("test1","test2","test3"))             # permet de créer une liste ( double parenthèses (()) )
liste.insert(1, "certainement")                        # ajouter un nouvel élément à la liste sans remplacer un autre existant (la liste s'allonge)
liste.append("probablement")                           # ajouter une nouvel élément à la fin de la liste
liste_2 = [" je ne sais pas "," on verra"]
liste.extend(thislist)                                 # permet de concaténer deux listes , ou une liste avec un tuple par exemple
liste.remove("non")                                    # retire l'élément spécifié
liste.pop(2)                                           # retire l'élément de l'index spécifié (si rien n'est spécifié, retire le dernier élément de la liste)
del liste [0]                                          # même utilité que  .pop  mais peut aussi supprimer la liste en ne spécifiant pas d'index
liste.clear()                                          # la liste reste, mais son contenu est effacé

fruits = ["apple", "Banana", "cherry", "Kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]              # crée une nouvelle liste qui n'ajoute que les éléments contenant la lettre a de la liste fruits (une boucle)
# liste comprehension : newlist = [expression for item in iterable if condition == True] => = [ x for x in new_list if condition is True]

liste.sort()                                           # trier la liste alphanumériquement (nombres et chaînes de caractères) de manière ascendante
liste.sort(reverse = True)                             # trier de manière descendante
sorted(fruits)                                         # renvoie la liste d'éléments triée sans changer la liste
fruits.sort(key = str.lower)                           # trier la liste sans tenir compte des majuscules et minuscules
liste.reverse()                                        # inverser la liste des éléments d'une liste (premier/dernier etc )
liste_3 = liste.copy()                                 # copier une liste sans que la nouvelle soit liée à l'originale
list_3 = list(liste)                                   # copier une liste //