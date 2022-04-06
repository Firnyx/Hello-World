nv_tuple = tuple(("saloute","saluut","Guten Tag"))                  # créer un tuple (doubles parenthèses (( ))  )
tuple2 = ("Konitchiwa",)
nv_tuple += tuple2                                                  # on peut additionner deux tuples ensemble pour ajouter des valeurs ( pas de .append)

(français, français2, allemand, japonais) = nv_tuple                # extrait les éléments des tuples, => français correspond à "saloute" etc
(*français,allemand,japonais) = nv_tuple                            # s'il y a moins de valeurs que d'éléments, ajouter un astérix à l'un d'eux va regrouper les éléments en excès (dans l'ordre)
for x in nv_tuple :                                                 # créer une boucle avec un tuple
    print(x)

tuple3 = tuple2 * 2                                                 # on peut multiplier le contenu d'un tuple

"""
Method 	        Description
count()	        Returns the number of times a specified value occurs in a tuple
index()	        Searches the tuple for a specified value and returns the position of where it was found
"""

# les sets ou ensembles
un_set = {"truaille","bilouage","mondrin"}

nv_set = set(("iris","rose","margerite"))                            # créer un nouveau set
for x in un_set :                                                    # créer une boucle pour "étudier" l'ensemble
    print(x)
nv_set.add("orchidée")                                               # ajouter un élément au set
un_set.update(nv_set)                                                # ajouter un set à un autre, on peut aussi ajouter à ce set une liste, un tuple, dictionnaire...
un_set2 = un_set.union(nv_set)                                       # ajouter un set à un autre
un_set.remove("bilouage")                                            # retirer un élément du set
un_set.discard("bilouage")                                           # retirer un élément du set. A la différence de .remove , cette méthode ne mettra pas d'erreur s'il n'y pas d'éléments à supprimer
y = un_set.pop()                                                     # retire un élément au hasard du set (aucun ordre)
print(y)                                                             # renvoie l'élément retiré par .pop
un_set.clear()                                                       # même fonction que pour les listes
del un_set                                                           # //

"""
Method         	       Description
add()	               Adds an element to the set
clear()	               Removes all the elements from the set
copy()	               Returns a copy of the set
difference()	       Returns a set containing the difference between two or more sets
difference_update()	   Removes the items in this set that are also included in another, specified set
discard()	           Remove the specified item
intersection()	       Returns a set, that is the intersection of two other sets
intersection_update()  Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	       Returns whether two sets have a intersection or not
issubset()	           Returns whether another set contains this set or not
issuperset()	       Returns whether this set contains another set or not-
pop()	               Removes an element from the set
remove()	                      Removes the specified element
symmetric_difference()            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	  inserts the symmetric differences from this set and another
union()	                          Return a set containing the union of sets
update()	                      Update the set with the union of this set and others
"""


# Les Dictionnaires

un_dict = {"un":"a_indéfini","le":"a_défini","quel":"je_sais_plus"}  # on a key : value pair =>  ici "un" est la clé et "a_indéfini" est la valeur du dictionnaire
un_dict["quelle"] = "oui"                                            # ajouter une clé et sa valeur à un dictionnaire

print(len(un_dict))                                                  # renvoie le nombre de valeurs dans le dictionnaire (ici 3)
un_dict2 = {"un": 1, "deux":True,"trois":[1,2,3]}                    # les valeurs des dictionnaire peuvent être de n'importe quel type de donnée
Yd = un_dict["un"]                                                   # on entre une clé et sa valeur nous est retournée
Cd = un_dict.get("le")                                               # même fonction
Zd = un_dict.keys()                                                  # accéder aux clés du dictionnaire
Gd = un_dict.values()                                                # accéder aux valeurs du dictionnaire
Vd = un_dict.items()                                                 # renvoie tous les éléments du dictionnaire en tant que tuples dans une liste
# = > print(Vd)  renvoie :  dict_items([('un,'a_indéfini'), ('le', 'a_défini')]) etc
# note : si un_dict change alors Zd Gd Vd changent aussi

if "alors" in un_dict:                                               # vérifier si une clé est présente dans une dictionnaire
    print("ok")
un_dict["quel"] = "toujours pas"                                     # modifie la valeur de la clé
un_dict2.update({"deux":False})                                      # même fonction
un_dict.pop("un")                                                    # retire l'élément ainsi que la clé spécifié
del un_dict2["trois"]                                                # même fonction, si rien n'est spécifié (pas de []) alors la méthode supprime le dictionnaire
un_dict.popitem()                                                    # retire le dernier élément spécifié (clé et valeur)
un_dict2.clear()                                                     # efface le contenu du dictionnaire

for x in un_dict :                                                   # renvoie les clés
    print(x)
for x in un_dict.values():                                           # même fonction
    print(x)
for x in un_dict :                                                   # renvoie les valeurs des clés
    print(un_dict[x])
for x in un_dict.values() :                                          # même fonction
    print(x)
for x,y in un_dict.items():                                          # renvoie les clés et leurs valeurs
    print(x,y)

un_dict3 = un_dict2.copy()                                           # copier un dictionnaire
Saisons = {                                                           # dictionnaires imbriqués
    "Hiver" : {
        "mois" : ["janvier","février","décembre"],
        "climat" : "froid"
    },
    "Printemps" : {
        "mois" : ["mars","avril","mai"],
        "climat" : "doux"
    },
    "Eté" : {
        "mois" : ["juin","juillet","août"],
        "climat": "chaud",
    }
}

un_dict4 = {
    "test": un_dict,
    "test2": un_dict2
}

'''
Method                 	Description
clear()	                Removes all the elements from the dictionary
copy()	                Returns a copy of the dictionary
fromkeys()	            Returns a dictionary with the specified keys and value
get()	                Returns the value of the specified key
items()	                Returns a list containing a tuple for each key value pair
keys()	                Returns a list containing the dictionary's keys
pop()	                Removes the element with the specified key
popitem()	            Removes the last inserted key-value pair
setdefault()	        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	            Updates the dictionary with the specified key-value pairs
values()	            Returns a list of all the values in the dictionary
'''







