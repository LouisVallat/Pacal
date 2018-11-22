
def ask():
    start, stop = input("Rang d'affichage de départ : "), input("Rang d'affichage de fin : ")
    return correct(start, stop)

def correct(start, stop):
    try:
        start, stop = int(start), int(stop)
    except ValueError:
        print("\nVisiblement vous n'avez pas entré des nombres.\nVeuillez réessayer.")
        ask()
    else:
        calcul(start, stop)    

def calcul(start, stop):
    print("\nLe Triangle de Pascal sera fait du rang " + str(start) + " jusqu'à " + str(stop) + ".\nDémarrage du calcul.")
    Pascal = {1:[1,0]}
    if start > stop or start < 1:
        print("\nLe rang de départ doit être supérieur à 1 et inférieur au rang de fin.\nVeuillez réessayer.")
        ask()
    for i in range(2, (stop+1)):
        Pascal[i] = []
        for x in range(i+1):
            Pascal[i].append(0)
            elementPos = 0
        while elementPos < len(Pascal[i-1]):
            if elementPos != 0:
                Pascal[i][elementPos] = Pascal[i-1][elementPos-1] + Pascal[i-1][elementPos]
            else:
                Pascal[i][elementPos] = 1
            elementPos+=1
    for pos in range(int(start), int(stop)+1):
        print(pos, end=' : ')
        for element in Pascal.get(pos):
            if element != 0:
                print(element, end=' ')
        print()

ask()