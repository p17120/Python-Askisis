cardelements=[]
while True:
 cardnumber = input("Δωσε μου τον αριθμό της κάρτας(16 στοιχεία): ")
 cardelements=[number for number in cardnumber]                          #input Τη κάρτα με έλεγχο οτι τα στοιχεία είναι 16
 if len(cardelements)==16 :
     break
 elif len(cardelements)<16:
     print("Δεν έβαλεσ αρκετούς χαρακτήρες")
 else:
     print("Έβαλες παραπάνω χαρακτήρες")

keyelements = cardelements[-2::-2]
restelements = cardelements[-1::-2]                      # Παίρνω ξεχωριστά τα στοιχεία που πρέπει να διπλασιαστούν με αυτά που δεν θέλουν
restelements= [int(element) for element in restelements] #Τα κάνω int για να μπορώ να τα διπλασιάσω/προσθέσω
keytelements= [int(element) for element in keyelements]
finalsum= 0
finalsum += sum(restelements)        #προσθέτω το πρώτο πίνακα
for element in keyelements:
    double = int(element)*2
    if double<=9:
        finalsum=finalsum+double     #άμα ο διπλάσιασμός του στοιχείου είναι μονοψήφιος πρόσθεσε το
    else:                            #άμα είναι δυψήφιος
        for number in str(double):   #για κάθε στοιχείο του (το κάνω string για να είναι iterable)
            finalsum=finalsum+int(number) #προσθέτω το κάθε ψηφίο
if finalsum%10==0:
    print("Η κάρτα είναι έγκυρη")
else:
    print("Η κάρτα δεν είναι έγκυρη")

