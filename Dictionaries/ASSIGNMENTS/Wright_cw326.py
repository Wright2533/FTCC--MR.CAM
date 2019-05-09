# Wright_cw326
#3/26/19
#

#1
dct = {'Monday':1,'Tuesday':2,'Wednesday':3}
print(dct['Tuesday'])
# Code prints the value for tuesday (2)

#2
dcti = {'Monday':1,'Tuesday':2,'Wednesday':3}
print(dct.get('Monday','Not found'))
# Shows the value for monday. .get shows an exception if monday is not a key.

#3
dctio = {'Monday':1,'Tuesday':2,'Wednesday':3}
print(dct.get('Friday','Not found'))
# .get shows Friday is not a key so it is not found

#4
stuff = {'aaa':111,'bbb':222,'ccc':333}
print(stuff['bbb'])
# Code prints the value from "bbb"

#5
dction = {1:[0,1],2:[2,3],3:[4,5]}
print(dction[3])
# Code prints the value from "3"

#6
dctiona = {1:[0,1],2:[2,3],3:[4,5]}
for k in dctiona:
    print(k)
# Code displays 1,2,3

#7
dctionar = {'Jenny':1,'James':2,'Johnny':3}
print(dctionar.get('James','Not found'))

#8
dctionary = {'Jenny':1,'Jim':2,'Johnny':3}
del dctionary ['Jim']


