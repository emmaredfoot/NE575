import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



def Temp(T_HP, FValue, HighF):
    FluxValue=1341.73
    HighF=Flux(HighF)
    k_f=30.094
    h_g=464
    k_c=16.3
    k_HP=139
    k_ss=15

    HPR=(.002)/(k_HP*.002*1.10)
    SSR2=(.01423)/(k_ss*1.10*.01423)
    CladR=(.00035)/(.00035*1.10*k_c)
    GapR=1/(h_g*.0001)
    SSR1=(.00926)/(k_ss*1.10*.00926)
    FuelR1=.0055/(k_f*1.10*.0055)
    FuelR2=.011/(k_f*1.10*.011)

    THP=T_HP+FluxValue*HPR
    T_SSR2=THP+FluxValue*SSR2
    TClad3=T_SSR2+FluxValue*CladR
    print("clad: ", TClad3)
    TFuel2=TClad3+FluxValue*FuelR2
    print("check: ", FluxValue*FuelR2)
    TClad2=TFuel2+FluxValue*CladR
    TSSR1=TClad2+FluxValue*SSR1
    TClad1=TSSR1+FluxValue*CladR
    TFuel1=TClad1+FluxValue*FuelR1
    print("Temperatures = ", THP, T_SSR2, TClad3, TFuel2, TClad2, TSSR1, TClad1, TFuel1)

    #Temp = [T_max,T_gap1, T_Clad1,T_SS1,T_Clad2, T_gap2, T_fuel2, T_gap3, T_Clad3, T_SSR2, T_HP2]

    #print(HPR, SSR2, CladR, GapR, SSR1, FuelR1, FuelR2)
    # T_other = 2847-FluxValue*(FuelR1+CladR+SSR1+CladR+FuelR2+CladR+SSR2+HPR+3*GapR)
    # print("Melting Conditions = ", T_other)
    # T_gap1 = T_max-FluxValue*(FuelR1+GapR)
    # T_Clad1= T_max-FluxValue*(FuelR1+GapR+CladR)
    # T_SS1= T_max-FluxValue*(FuelR1+GapR+CladR+SSR1)
    # T_Clad2= T_max-FluxValue*(FuelR1+GapR+CladR+SSR1+CladR)
    # T_gap2=T_max-FluxValue*(FuelR1+GapR+CladR+SSR1+CladR+GapR)
    # T_fuel2 = T_max-FluxValue*(FuelR1+GapR+CladR+SSR1+CladR+GapR+FuelR2)
    # T_gap3= T_max-FluxValue*(FuelR1+GapR+CladR+SSR1+CladR+GapR+FuelR2+GapR)
    # T_Clad3= T_max-FluxValue*(FuelR1+GapR+CladR+SSR1+CladR+GapR+FuelR2+GapR+CladR)
    # T_SSR2 = T_max-FluxValue*(FuelR1+GapR+CladR+SSR1+CladR+GapR+FuelR2+GapR+CladR+SSR2)
    # T_HP2 = T_max-FluxValue*(FuelR1+GapR+CladR+SSR1+CladR+GapR+FuelR2+GapR+CladR+SSR2+HPR)

    #T_HP_out = FluxValue*(FuelR1+GapR+CladR+SSR1+CladR+GapR+FuelR2+GapR+SSR2)+T_HP+400
    #T_SS_HP = FluxValue*(FuelR1+GapR+CladR+SSR1+CladR+GapR+FuelR2+GapR)+T_HP+400

    #Temp = [T_max,T_gap1, T_Clad1,T_SS1,T_Clad2, T_gap2, T_fuel2, T_gap3, T_Clad3, T_SSR2, T_HP2]
    #return(Temp)
    return(0)

def Flux(flux):
    v=flux*190E6*.3733*1.60217E-19
    q_double=v*.55**2/(2*.595)
    q_prime=q_double*.595*100*2*3.14159
    #print(v, q_double, q_prime)
    return(q_prime)

def AvgFlux(DFlux):
    Avg = Flux(DFlux)*.0055**2
    #print(Avg)
    return(Avg)

MaxFlux=3.84323e13
SecondFlux=3.832e13
#print("A= ",AvgFlux(MaxFlux))


M=Flux(MaxFlux)
print("M= ", M)
S=Flux(SecondFlux)
print("S= ", S)

#Resistance values
T_K=760
T_Na=900
T_Ce=670
TempK=Temp(T_K, S, M)
TempNa=Temp(T_Na,S, M)
TempCe=Temp(T_Ce,S, M)

#print('TempK= ', TempK)

#Distances
R_f1=0.0055
R_ci1=0.0056
R_co1=0.00595
R_ssi1=.00595
R_sso1=.01521
R_co2=.01521
R_ci2=.01556
R_f2=.01566
R_f3=.02666
R_ci3=.02676
R_co3=.02711
R_ssi2=.02711
R_sso2=0.04134
R_HPo1=.04134
R_HPi1=.04514

#print("Max = ", Temp[0])
# print("Gap min = ", T_gap1)
# print("Clad1 = ", T_Clad1)
# print("Stainless 1= ", T_SS1)
# print("Clad2= ", T_Clad2)
# print("Gap 2= ", T_gap2)
# print("Fuel 2= ", T_fuel2)
# print("Gap 3=", T_gap3)
# print("Clad 3= ", T_Clad3)
# print("Stainless 2= ", T_SSR2)
# print("Heat Pipe= ", T_HP)

# R=[R_f1, R_ci1, R_co1, R_ssi1, R_sso1, R_co2, R_ci2, R_f2, R_f3, R_ci3, R_co3]
# green_dot=mpatches.Patch(color='green', label= "Potassium")
# red_dot=mpatches.Patch(color='red', label= "Sodium")
# blue_dot = mpatches.Patch(color='blue', label="Caesium")
# plt.legend(handles=[green_dot, red_dot, blue_dot])
# plt.plot(R,TempK,'go', R, TempNa, 'ro', R, TempCe, 'bo')
# #plt.plot(R,TempK,'go')
# #plt.plot(R_f1, T_max, R_ci1, T_gap1, R_co1, T_Clad1, R_ssi1, T_SS1, R_sso1, T_Clad2, R_co2, T_gap2, 'ro')
# plt.ylabel("Temperature (C)")
# plt.xlabel("Distance (m)")
# #plt.title("Temperature as a Function of Distance from Fuel Centerline")
# plt.show()
