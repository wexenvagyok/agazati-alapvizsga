from nasaclass import *

adatok=[]
f=open("NASAlog.txt")
for egySor in f:
    adatok.append(nasa(egySor))
f.close()

print("5. feladat: formázott kiiratás: {}",format(len(adatok)))

osszeg=0
for egyAdat in adatok:
    osszeg+=egyAdat.ByteMeret
print(osszeg)