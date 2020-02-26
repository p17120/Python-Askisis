#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://www.contrib.andrew.cmu.edu/~gc00/reviews/pokerrules
import itertools
import random


# Ελέγχει αν όλα είναι τα ίδια
def Pairs(h):
    kinds = [c[0] for c in h]
    dublicatenum = []
    dublicatekind = []
    for element in kinds:
        if element not in dublicatekind:
            if kinds.count(element) == 5:  # βρίσκω τα pairs και τα βάζω σε 2 δυο πίνακεσ 1 για να ξέρω
                dublicatenum.append(5)  # τι kind είναι και πόσα pair έχει
                dublicatekind.append(element)
            elif kinds.count(element) == 4:
                dublicatenum.append(4)
                dublicatekind.append(element)
            elif kinds.count(element) == 3:
                dublicatenum.append(3)
                dublicatekind.append(element)
            elif kinds.count(element) == 2:
                dublicatenum.append(2)
                dublicatekind.append(element)
            elif kinds.count(element) == 1:
                dublicatenum.append(1)
                dublicatekind.append(element)
            else:
                dublicatenum.append(0)
                dublicatekind.append(element)

    return dublicatenum, dublicatekind


def print_hand(l):
    txt = ""
    for c in l:
        txt += str(c[0]) + str(c[1]) + ","
    txt = txt[:-1]
    return txt


# Για να μη γράφουμε τα χαρτιά ας
# φτιάξουμε την τράπουλα προγραμματιστικά
cards = [str(i) for i in range(1, 14)]
# cards+=["J","Q","K"] #πρόσθεσε τις φιγούρες
suits = ["S", "H", "D", "C"]  # βάλε τα χρώματα
deck = itertools.product(cards, suits)  # Φτιάξε όλα τα φύλλα
deck = list(deck)  # Ας τα έχω σε μία λίστα...
# Ας βάλουμε 2 τράπουλες
deck += deck
# Ανακάτωσε την τράπουλα
random.shuffle(deck)
user_hand = []
comp_hand = []
# Μοίρασε τα χαρτιά
for i in range(5):
    user_hand += [deck.pop()]
    comp_hand += [deck.pop()]

print("Τα χαρτιά σου είναι: ", print_hand(user_hand))
pairsuser = []
kindsuser = []
pairsuser, kindsuser = Pairs(user_hand)
pairscomp, kindscomp = Pairs(comp_hand)   # χωρίζω τις μεταβλητές
max_pairsuser = int(max(pairsuser))
diplauser=[]
diplacomp=[]
for element in pairsuser :
    if element==2:
        diplauser.append(kindsuser[pairsuser.index(element)])   #βρίσκω 2 pair
for element in pairscomp:
    if element==2:
        diplacomp.append(kindsuser[pairscomp.index(element)])


pair_number_user = int(kindsuser[pairsuser.index(max_pairsuser)])


print("Τα χαρτιά του υπολογιστή είναι: ", print_hand(comp_hand))

if pairscomp:
  max_pairscomp = max(pairscomp)
  pair_number_comp = int(kindscomp[pairscomp.index(max_pairscomp)])

kindsuser = [int(element) for element in kindsuser]
kindscomp = [int(element) for element in kindscomp]

if max_pairsuser > max_pairscomp:
    print("user wins with higher pair")
elif max_pairscomp > max_pairsuser:
    print("Computer wins with higher pair")
elif max_pairscomp == max_pairsuser:

    if pairscomp==2:
        if max(pairscomp)>max(pairsuser):                  #ifs για να τεστάρει δύναμη χεριού ελεγχει για high card,1-5pair
            print("computer wins")
        else:
            print("user wins")
    elif pair_number_comp > pair_number_user:
        print("Computer wins with higher pair number")
    elif pair_number_comp < pair_number_user:
        print("user wins with higher pair number")
    else:
        if max(kindscomp) > max(kindsuser):
            print("Computer wins with higher number")
        elif max(kindscomp) < max(kindsuser):
            print("user wins with higher number")
        else:
            print("make a second max")
elif max_pairscomp == max_pairsuser == 1:
    if max(kindscomp) > max(kindsuser):
        print("computer wins with high card")
    else:
        print("player wins with high card")
else:
    print("error")
