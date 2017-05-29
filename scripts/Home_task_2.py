print('Enter number of plates, please') # - задача про тарелки и моющее средство
plates = int(input(''))
print('Enter quantity of washing agent, please')
Fairy = float(input(''))
v = 0.5 # - расход моющего средства на одну тарелку

while (plates>0) and (Fairy>0):
    plates -=1
    Fairy -=v
    print(Fairy)

if Fairy < 0.5:
       print('Number of plates ' , plates)
if plates == 0:
       print('Washing agent left' , Fairy)
