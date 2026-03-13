#Demandez à l'utilisateur de fournir deux nombres avec la fonction input. Stockez ces valeurs dans  nombre1et  nombre2.
nombre1 = input("Entrez un nombre entier: ")
nombre2 = input("Entrez un nombre entier: ")

#nombre1 et nombre2 sont des chaînes de caractères (str). Utilisez la méthode isnumeric  (explication de la méthode) pour vérifier que ce sont des nombres.
# isnumeric() permet de vérifier si la chaîne de caractères est un nombre
if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Erreur: les deux nombres doivent être des nombres entiers")
    #Si ce n'est pas le cas, sortez du programme en générant une exception avec le mot cléraise:raise SystemExit("Fin du programme")
    raise SystemExit("Fin du programme")

#Sinon, convertissez les deux nombres en nombres entiers avec la fonction  int.
nombre1 = int(nombre1)
nombre2 = int(nombre2)

#Créez une variable operation et utilisez input pour obtenir l'opération souhaitée par l'utilisateur.
operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/']: ")

#Vérifiez que l'opération est valide (+, -, * ou /). Sinon, quittez le programme.
if operation not in ["+", "-", "*", "/"]:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")

#Effectuez le calcul en fonction de la valeur de operation(par exemple en utilisant if - elif - else) et stockez le résultat dans la variable resultat.
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":

#Attention, il est impossible de diviser un nombre par 0, il faut donc prévoir une structure conditionnelle supplémentaire pour quitter le programme si le deuxième nombre est 0.
    if nombre2 == 0:
        print("Erreur: impossible de diviser par zéro.")
        raise SystemExit("Fin du programme")
    
#Astuce : lors de la division, utilisez la fonctionroundpour arrondir le résultat et le rendre plus lisible !
    resultat = round(nombre1 / nombre2, 2)

# Afficher le résultat
print(f"Le résultat de l'opération est: {round(resultat, 2)}")