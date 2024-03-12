from nasaclass import *

adatok=[]
f=open("NASAlog.txt")
for egySor in f:
    adatok.append(nasa(egySor))
f.close()