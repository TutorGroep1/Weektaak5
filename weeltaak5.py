from random import shuffle
import random

def main():
    sequentie = inlezen()
    seq = splitten(sequentie)
    functie(seq)

    
    
def inlezen():
    bestand = open('HIV2-gp-eiwit')
    sequentie = []
    for regel in bestand:
        regel = regel.replace("\n", "")
        if not regel.startswith(">"):
            sequentie += regel
    #print(sequentie)
    return sequentie

def splitten(sequentie):
    seq = []
    for letter in sequentie:
        seq.append(letter)
    #print(seq)
    return seq

def functie(seq): 
    nieuw_bestand = ''
    for c in range(100):
        random.shuffle(seq)
        #print("> randomisate", index
        for letter in seq:
            nieuw_bestand += letter

"""

for i in range(100):
    temp = ""
    for letter in seq:
        temp += letter
    lijst.append(temP)

""""
        
    print("Dit is het nieuwe bestand", nieuw_bestand)




main()
