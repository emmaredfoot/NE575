import numpy as np

#Import all of the x coordinate values
with open('flux.txt') as f:a=f.read()
a=np.array(a.split())
print(len(a))

#Find all of the y coordinate values
with open('flux2.txt') as m:b=m.read()
b=np.array(b.split())
b2=b.astype(np.float)
print("b2= ", len(b2))

y=[]
for x in b2:
    if x > .1:
        y.append(x)
        index=np.argwhere(b2==x)
        b2 = np.delete(b2,index)

y=np.sort(y)
flux_arranged = np.sort(b2)

print(len(y))
print("after ", len(flux_arranged))

print(flux_arranged)
print("Max flux= ", flux_arranged[len(b2)-1])
print("Next Max= ", flux_arranged[len(b2)-2])

#Now a is the x coordinate, y is the y coordinate, and b2 is all of the flux values
#Now I need to associate the correct flux value with the correct x and y coordinates

# y=b[0:10081:99]
# print(y)

# x_vals=open("flux.txt")
# x = np.array(np.loadtxt(x_vals, delimiter='        ',dtype=float))
# flux = open("flux2.txt")
# flux_vals = np.array(np.loadtxt(flux, delimiter=' ', dtype=float))
# print("x= ", x)
# print(x[0])
# print("flux values = ", flux_vals)
# print(len(flux_vals))
# print(flux_vals[0])
# i=x[0]
# m=i.split()
# print(m[1])
#m=[int(l) for l in m.split()]
#print(m[0])
#48.75 9.44889E-05 9.56937E-05 9.32109E-05 9.49496E-05 9.42181E-05 9.38695E-05 9.38543E-05 9.22560E-05 9.20386E-05 9.46926E-05 9.63757E-05 9.44918E-05 9.19215E-05 9.42479E-05 9.45321E-05 9.60090E-05 9.50008E-05 9.45266E-05 9.27009E-05 9.06880E-05 9.10852E-05 9.32550E-05 9.09069E-05 8.91845E-05 8.98136E-05 9.07588E-05 9.00436E-05 9.12915E-05 8.91364E-05 9.08754E-05 8.99693E-05 9.10326E-05 8.97131E-05 9.17607E-05 8.91175E-05 8.77063E-05 8.82975E-05 8.67720E-05 8.79168E-05 8.67893E-05 8.69249E-05 8.48348E-05 8.56950E-05 8.48351E-05 8.32478E-05 8.33575E-05 7.97361E-05 8.15599E-05 8.04664E-05 8.08849E-05 7.95145E-05 7.85702E-05 7.75914E-05 7.49536E-05 7.29198E-05 7.14421E-05 7.07616E-05 7.03918E-05 7.26123E-05 7.05740E-05 6.86258E-05 6.88084E-05 6.59458E-05 6.51875E-05 6.33348E-05 6.13437E-05 5.90905E-05 5.84274E-05 5.97309E-05 5.65758E-05 5.65674E-05 5.49297E-05 5.34517E-05 5.26982E-05 5.02319E-05 5.01871E-05 4.63640E-05 4.56123E-05 4.36672E-05 4.09510E-05 3.85623E-05
