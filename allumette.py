nbMatch = 50

#Fonction qui boucle sur le nombre d'allumettes qu'il reste au fur et à mesure de la partie, qui permet lorsque 
# la condition n'est pas vérifié de lancer la fonction givingTheNbOfRemovingMatches(). Lorsque condition est 
#vérifiée, fin du jeu.
def game():
    nbPlayer = numberPlayer()
    global nbMatch
    while nbMatch > 1 :
        for i in range(1, nbPlayer + 1) :
            nbMatchRemoved = givingTheNbOfRemovingMatches(i, nbMatch)
            nbMatch -= nbMatchRemoved
            if nbMatch == 1 :
                break
    print(f'Bravo Joueur {i} ! Vous avez gagné !')


#Fonction qui demande le nombre d'allumettes à enlever + vérifie que les conditions sur le nombre d'allumettes à 
#enlever est bien respecté.
#Paramètres :
# - i : correspond au nombre de joueur récupéré dans la fonction game() ù la fonction est appelé
# - nbMatchRemaining : nombre d'allumettes à enlever
def givingTheNbOfRemovingMatches(i, nbMatchRemaining):
        nbMatchRemoved = int(input(f'Joueur {i}, il reste {nbMatchRemaining}  allumettes, combien voulez-vous en enlever ?'))
        while nbMatchRemoved > 6 or nbMatchRemoved <= 0 or (nbMatchRemoved > nbMatch - 1 and nbMatch <= 6):
            if nbMatchRemoved > 6 :
                print('Vous devez enlever maximum 6 allumettes')
            elif nbMatchRemoved <= 0 :
                print('Vous devez enlever au minimum 1 allumette')
            elif (nbMatchRemoved > nbMatch - 1 and nbMatch <= 6) :
                print(f'On peut retirer que {nbMatch -1} ou moins allumettes')
            nbMatchRemoved = int(input(f'Joueur {i}, il reste {nbMatchRemaining}  allumettes, combien voulez-vous en enlever ?'))
        return nbMatchRemoved


#Demande à l'utilisateur le nombre de joueur et retourne la valeur
def numberPlayer():
    nbPlayer = int(input('Combien de joureur êtes-vous ? '))
    return nbPlayer

game()
