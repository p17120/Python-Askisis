
number = int(input("Δώσε μου έναν αριθμό: "))

while True:

    number = number*3
    number = number+1
    numberlist = [digit for digit in str(number)]
    newnumber=0
    for digit in numberlist:
       newnumber = newnumber+int(digit)

    number=newnumber
    if number<10:
      print(number)
      break



