Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 254
>>> type (a)
<class 'int'>
>>> data1=10
>>> data2=11
>>> print(data1, data2)
10 11
>>> age = 32
>>> name = 'Jean'
>>> print(name , 'a' , age , 'ans')
Jean a 32 ans
>>> print("{} a {} ans".format(name, age)) # méthode format() permet
... une meilleure organisation de l’affichage des variable
SyntaxError: multiple statements found while compiling a single statement
>>> print("{} a {} ans".format(name, age))
Jean a 32 ans
>>> var = (4500 + 2575) / 14800
>>> print("Le résultat du calcul est", var)
Le résultat du calcul est 0.4780405405405405
>>> print("Le résultat du calcul est {:.2f}".format(var))
Le résultat du calcul est 0.48
>>> print("Le résultat du calcul est {:.4f}".format(var))
Le résultat du calcul est 0.4780
>>> name = "Eric"
>>>  age = 20
...  
SyntaxError: unexpected indent
>>> age = 20
>>> f"Hello, {name}. vous avez {age} ans."
'Hello, Eric. vous avez 20 ans.'
>>> 
>>> int(nom, prenom, math, anglais, info; promotion)
SyntaxError: invalid syntax
>>> int(nom, prenom, math, anglais, info, promotion)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(nom, prenom, math, anglais, info, promotion)
NameError: name 'nom' is not defined
