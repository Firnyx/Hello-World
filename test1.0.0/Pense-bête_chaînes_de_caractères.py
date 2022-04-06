x = "strings, ou chaîne de caractères"

"""
Text Type:   	    str
Numeric Types: 	    int, float, complex
Sequence Types:     list, tuple, range
Mapping Type: 	    dict
Set Types: 	   set, frozenset
Boolean Type:     bool
Binary Types: 	  bytes, bytearray, memoryview
"""
#s'appliquent aux chaînes de caractères :

print(len(x))                  # pour connaitre la longuer de la châine
x = x.upper()                  # mettre en majuscules tous les caractères de la chaîne de caractères
x = x.lower()                  # mettre en minuscule //
x = x.strip()                  # retire les espaces au début et à la fin de la chaîne
x = x.replace("s","r")         #remplace une lettre par une autre (dans toute la chaîne)
x = x.split(",")               #renvoie une liste qui comporte les parties séparés par le caractère désigné (celui-ci disparait)
# la méthode  .format :
age = 18.2
strings_x = "J'ai {} ans"
a = strings_x.format(age)      # permet de combiner une chaîne de caractère avec un nombre => on peut spécifier  un ordre avec {0} s'il y en a plusieurs


"""
Code 	 Result 	
\' 	     Single Quote 	
\\ 	     Backslash 	
\n 	     New Line 	
\r 	     Carriage Return 	
\t       Tab 	
\b 	     Backspace 	
\f 	     Form Feed 	
\ooo 	 Octal value 	
\xhh 	 Hex value
"""



"""
Method 	              Description
capitalize()	      Converts the first character to upper case
casefold()	          Converts string into lower case
center()	          Returns a centered string
count()               Returns the number of times a specified value occurs in a string
encode()	          Returns an encoded version of the string
endswith()	          Returns true if the string ends with the specified value
expandtabs()	      Sets the tab size of the string
find()	              Searches the string for a specified value and returns the position of where it was found
format()	          Formats specified values in a string
format_map()	      Formats specified values in a string
index()	              Searches the string for a specified value and returns the position of where it was found
isalnum()	          Returns True if all characters in the string are alphanumeric
isalpha()	          Returns True if all characters in the string are in the alphabet
isdecimal()	          Returns True if all characters in the string are decimals
isdigit()	          Returns True if all characters in the string are digits
isidentifier()	      Returns True if the string is an identifier
islower()	          Returns True if all characters in the string are lower case
isnumeric()	          Returns True if all characters in the string are numeric
isprintable()	      Returns True if all characters in the string are printable
isspace()	          Returns True if all characters in the string are whitespaces
istitle() 	          Returns True if the string follows the rules of a title
isupper()	          Returns True if all characters in the string are upper case
join()	              Joins the elements of an iterable to the end of the string
ljust()	              Returns a left justified version of the string
lower()	              Converts a string into lower case
lstrip()	          Returns a left trim version of the string
maketrans()	          Returns a translation table to be used in translations
partition()           Returns a tuple where the string is parted into three parts
replace()	          Returns a string where a specified value is replaced with a specified value
rfind()	              Searches the string for a specified value and returns the last position of where it was found
rindex()	          Searches the string for a specified value and returns the last position of where it was found
rjust()	              Returns a right justified version of the string
rpartition()	      Returns a tuple where the string is parted into three parts
rsplit()	          Splits the string at the specified separator, and returns a list
rstrip()	          Returns a right trim version of the string
split()	              Splits the string at the specified separator, and returns a list
splitlines()	      Splits the string at line breaks and returns a list
startswith()	      Returns true if the string starts with the specified value
strip()	              Returns a trimmed version of the string
swapcase()	          Swaps cases, lower case becomes upper case and vice versa
title()	              Converts the first character of each word to upper case
translate()           Returns a translated string
upper()	              Converts a string into upper case
zfill()	              Fills the string with a specified number of 0 values at the beginning
"""


