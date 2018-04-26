import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



def Temp(T_HP, FValue, HighF):

    #1341.73 is the average heat flux assuming core power of 5 MWth
    Gen_FuelHP=14.118E6*.011
    Gen_Fuel_C=14.118E6*.0055
    Gen2=Gen_FuelHP+Gen_Fuel_C
    print("Gen2= ", Gen2)
    print("HF=", HighF)
    #k values in W/mK
    k_f=30.094
    h_g=464
    k_c=16.3
    k_HP=138
    k_ss=15

    HPR=(.002)/(k_HP)
    SSR2=(.01423)/(k_ss)
    CladR=(.00035)/(k_c)
    GapR=1/(h_g*.0001)
    SSR1=(.00926)/(k_ss)
    FuelR1=.0055/(k_f)
    FuelR2=.011/(k_f)

    THP=T_HP+HighF*HPR
    T_SSR2=THP+Gen2*SSR2
    TClad3=T_SSR2+Gen2*CladR
    print("clad: ", TClad3)
    TFuel2=TClad3+Gen2*FuelR2
    print("check: ", TFuel2)
    TClad2=TFuel2+Gen_Fuel_C*CladR
    TSSR1=TClad2+Gen_Fuel_C*SSR1
    TClad1=TSSR1+Gen_Fuel_C*CladR
    TFuel1=TClad1+Gen_Fuel_C*FuelR1
    print("Temperatures = ", THP, T_SSR2, TClad3, TFuel2, TClad2, TSSR1, TClad1, TFuel1)
    Temp = [T_HP, THP, T_SSR2, TClad3, TFuel2, TClad2, TSSR1, TClad1, TFuel1]
    return(Temp)

def Flux(flux):
    macro = .3733
    v=flux*190E6*macro*1.60217E-19
    q_double=v*.55
    q_prime=q_double*.595*100*2*3.14159
    #print(v, q_double, q_prime)
    return(q_double)

def AvgFlux(DFlux):
    Avg = Flux(DFlux)*.0055**2
    #print(Avg)
    return(Avg)

MaxFlux=3.84323e13
SecondFlux=3.832e13
#print("A= ",AvgFlux(MaxFlux))


M=Flux(MaxFlux)
S=Flux(SecondFlux)

#Resistance values
T_K=760
T_Na=890
T_Ce=670
TempK=Temp(T_K, S, M)
print("T= ", len(TempK))
TempNa=Temp(T_Na,S, M)
TempCe=Temp(T_Ce,S, M)

#print('TempK= ', TempK)

#Distances
RHP=.002
RSS1=.01623
RCladI=.01658
RFuel1=.02758
RClad2=.02793
RSS2=.03719
RClad3=.03754
RFinal=.04304



R=[0, RHP, RSS1, RCladI, RFuel1, RClad2, RSS2, RClad3, RFinal]
print("R= ", len(R))
green_dot=mpatches.Patch(color='green', label= "Potassium")
red_dot=mpatches.Patch(color='red', label= "Sodium")
blue_dot = mpatches.Patch(color='blue', label="Caesium")
plt.legend(handles=[green_dot, red_dot, blue_dot])
plt.plot(R,TempK,'go', R, TempNa, 'ro', R, TempCe, 'bo')
#plt.plot(R,TempK)
#plt.plot(R_f1, T_max, R_ci1, T_gap1, R_co1, T_Clad1, R_ssi1, T_SS1, R_sso1, T_Clad2, R_co2, T_gap2, 'ro')
plt.ylabel("Temperature (C)")
plt.xlabel("Distance (m)")
plt.title("Temperature as a Function of Distance from Heat Pipe")
plt.show()
