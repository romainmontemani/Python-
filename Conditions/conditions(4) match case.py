fruits = "ananas"
match fruits:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes !")
    case "orange":
        print("Les oranges sont bonnes pour la santé !")
    case _: 
        print("Je ne connais pas ce fruit !")