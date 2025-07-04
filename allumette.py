nbMatchStart = 50

def matchGame():
    nbMatchRemoved = int(input('Il y a 50 allumettes, combien voulez-vous en enlever ?'))
    nbMatchRemaining = nbMatchStart - nbMatchRemoved
    while nbMatchRemaining > 1 :
        nbMatchRemoved = int(input(f'Il reste {nbMatchRemaining} allumettres. Combien voulez-vous en enlever ?'))
        nbMatchRemaining = nbMatchRemaining - nbMatchRemoved
        if nbMatchRemaining == 1 :
            print('Bravo ! Vous avez gagné !')

matchGame()
