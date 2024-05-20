spelerX = "X"
spelerO = "O"
varLeeg = " "

#leeg bord
bord = [[varLeeg, varLeeg, varLeeg],
         [varLeeg, varLeeg, varLeeg],
         [varLeeg, varLeeg, varLeeg]]

#geeft een nummer aan elke positie op het bord
keuzes = {1: [0, 0], 2: [0, 1], 3: [0, 2],
          4: [1, 0], 5: [1, 1], 6: [1, 2],
          7: [2, 0], 8: [2, 1], 9: [2, 2]
          }


def kiesSpeler():
    spelerKeuze = input("Kies speler X of O")
    if spelerKeuze == spelerX:
        print("Je hebt speler X gekozen")

    elif spelerKeuze == spelerO:
        print("Je hebt speler O gekozen")

    else:
        print("Je hebt een verkeerde keuze gemaakt")
        kiesSpeler()

    return spelerKeuze

#print her bord
def printBord():
    print(bord[0][0] + "|" + bord[0][1] + "|" + bord[0][2])
    print("-+-+-")
    print(bord[1][0] + "|" + bord[1][1] + "|" + bord[1][2])
    print("-+-+-")
    print(bord[2][0] + "|" + bord[2][1] + "|" + bord[2][2])

#beurt speler X
def beurtSpelerX():
    print("Speler X is aan de beurt")
    plaats = int(input("gebruik getallen 1-9:"))
    
    if plaats <= 9 and plaats >= 1: #check of het getal van 1-9 is
        coord = keuzes[plaats]
        if bord[coord[0]][coord[1]] == varLeeg: #check of het vakje leeg is
            bord[coord[0]][coord[1]] = spelerX
            printBord()
            winnaar(bord, spelerX)
        else:
            print("Die is plek al bezet, kies een leeg vakje")
            beurtSpelerX()
    else:
        print("Kies een getal van 1-9")
        beurtSpelerX()

#beurt speler O
def beurtSpelerO():
    print("Speler O is aan de beurt")
    plaats = int(input("gebruik getallen 1-9:"))

    if plaats <= 9 and plaats >= 1: #check of het getal van 1-9 is
        coord = keuzes[plaats]
        if bord[coord[0]][coord[1]] == varLeeg: #check of het vakje leeg is
            bord[coord[0]][coord[1]] = spelerO
            printBord()
            winnaar(bord, spelerO)  
        else:
            print("Die is plek al bezet, kies een leeg vakje")
            beurtSpelerO()
    else:
        print("Kies een getal van 1-9")
        beurtSpelerO()

#check winnaar
def winnaar(state, speler):
    gewonnen = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[2][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]]
    ]
    if [speler, speler, speler] in gewonnen:
        print("SPELER " + speler + " HEEFT GEWONNEN!")
        exit()

def leegVakje():
    vakjes = []
    x = 0
    for rij in bord:
        y = 0
        for vakje in rij:
            if vakje == " ":
                vakjes.append([x,y])
            y=y+1
        x=x+1
    return vakjes

#main programma
printBord()

kiesSpeler()


while (len(leegVakje()) != 0):
    beurtSpelerO()
    beurtSpelerX()

print("\n")
printBord()


