from datetime import date
today = date.today()                      #Παίρνω date από library

d0 = today.strftime("%d/%m/%Y")
todayday = d0[:2]            #Παίρνω μέρα μήνα χρόνο με string manipulation
todaymonth= d0[3:5]
todayyear = d0[6:10]
daysinmonth = (31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ); #tuple με της ημέρες κάθε μήνα ο φερβουάριος είναι κενός γιατί υπάρχουν leap years
                                                                # που έχει 29 μέρες αντί για 28 το υπολογίζω μετα
def countthedays(megali , mikri):
  delta = megali - mikri
  print(delta.days,"Ημέρες")                         #Funtion που μου βγάζει πόσες μερες,ώρες,δεύτερα απέχουν απο την μεγαλύτερη ημερομηνία
  print(delta.days * 24,"Ώρες")                      #στην μικρότερη
  print(delta.days * 24 * 3600,"Δευτερόλεπτα")


while True:                                                         # Input λούπα μέχρι το input να τηρεί βασικές
  userdate=input("Δώσε μου μία ημερομηνία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ : ")  # προυποθέσεις για ημερομηνία καθώς και παίρνω
  userday= userdate[:2]                                             #καθώς και παίρνω ξεχωριστά τα values
  usermonth=userdate[3:5]
  useryear=userdate[6:10]
  if int(userday)<=31 and int(userday)>0 and int(usermonth)>0 and int(usermonth)<=12 and int(useryear)>=0: #άμα ειναί valid ημερομηνία βγες απο λούπα
    break

  print("Κάτι έβαλες λάθος ....")


d1 = date(int(useryear), int(usermonth) , int(userday), )          #κάνω τα Input και την ημερομηνία dates
d2 = date(int(todayyear), int(todaymonth) , int(todayday), )

if int(useryear)>=int(todayyear) :
  if int(usermonth)>int(todaymonth):
   countthedays(d1,d2)
  elif int(usermonth)<int(todaymonth):             # ifs για να δω πια ημερομηνία είναι μεγαλύτερη
    countthedays(d2,d1)
  elif int(userday)>int(todayday):
    countthedays(d1,d2)
  else:
    countthedays(d2,d1)
else:
  countthedays(d2,d1)

if int(usermonth)!=2:                                                           #Κάνει print πόσες μέρες έχει ο μήνας που έβαλε ο χρήστης
  print("Ο μήνας που βάλατε περιέχει",daysinmonth[int(usermonth)-1],"Ημέρες")   #από το tuple εκτός για φεβρουάριο που υπολογίζει πρώτα
elif int(useryear)%4==0:                                                        # άμα είναι leap year η όχι
  print("Είναι leap year άρα ο φεβρουάριος περιέχει 29 ημέρες")
else:
  print("Δεν είναι leap year άρα ο φεβρουάριος περιέχει 28 ημέρες")
