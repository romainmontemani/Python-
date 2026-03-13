mot_de_passe = input("Entrez votre mot de passe : ")
if len(mot_de_passe) < 8:
    print("Mot de passe trop court, il doit contenir au moins 8 caractères ! ")
elif not any(char.isdigit() for char in mot_de_passe):
    print("Mot de passe doit contenir au moins un chiffre ! ")
elif not any(char.isalpha() for char in mot_de_passe):
    print("Mot de passe doit contenir au moins une lettre ! ")
elif not any(char.isupper() for char in mot_de_passe):
    print ("Mot de passe doit contenir au moins une lettre majuscule ! ")
else:
    print("Mot de passe valide ! ")