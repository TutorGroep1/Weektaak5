#Weektaak 5
from random import shuffle
import random

def main():
    #bestand_lezen()
    #randomizer()
    #fasta_maker()
    bestand_maker()
    
def bestand_lezen():
    try:
        seq = []
        
        #bestand = input(open('Geef een bestandsnaam op: '))
        bestand = open('SIVmnd2-gp.txt')
        
        for line in bestand:
            if '>' not in line:
                for ami in line:
                    if ami != '\n':
                        seq.append(ami)
                    
                    
        return seq
        
    except FileNotFoundError:
        print('Geef aub de goede bestandsnaam.')
        bestand_lezen()


def randomizer():

    seq = bestand_lezen()
    sequenties = []
    index = 0
    
    sequenties.append(seq)
    
    while index < 100:
        
        random.shuffle(seq)
        sequenties.append(seq)

        
        index += 1

    return sequenties

def fasta_maker():
    fasta = ""
    seqs = randomizer()
    teller = 0
    
    og_seq = bestand_lezen()
    fasta += ">Originele sequentie:\n"
    for teken in og_seq:
        fasta += teken
    fasta += '\n\n'
        
    
    for seq in seqs:
        string = ">SIVmnd2_sequentie_V:{}\n".format(teller)
        for teken in seq:
            string += teken
        string += '\n\n'
        fasta += string
        teller += 1
        
    return fasta
        
def bestand_maker():

    tekst = fasta_maker()

    file = open('Omega3 sequenties', 'w')

    file.write(tekst)
    file.close()
    
    
main()
