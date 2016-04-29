ratio = open('ratio.txt','r')
print (ratio.read())
amount = 0
distance = float(input('Enter Distance : '))
amount += 35
if distance <= 1:
    amount = amount 
elif distance <= 5:
    distance -= 1
    amount += distance*2
elif distance <= 10:
    distance -= 5
    amount += 8
    amount += distance*2.5
elif distance <= 20:
    distance -= 10
    amount = 55.5
    amount += distance*3
elif distance <= 50:
    distance -= 20
    amount = 85.5
    amount += distance*3.5
else:
    distance -= 50
    amount = 190.5 
    amount += distance*5
print ('amount = %.2f Bath\n'%(amount))
print ('Thank you for services')
