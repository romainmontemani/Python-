age = int(input("Quel est votre âge ? "))
if age < 0 or age > 120:
    print("Âge invalide")
elif age < 12:
    print("Tu es un enfant")
elif age < 18:
    print("Tu es un adolescent")
elif age < 65:
    print("Tu es un adulte")
else:
    print("Tu es un senior")
