import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



def Temp(T_HP):
    Flux=.053808
    k_f=30.094
    h_g=464
    k_c=16.3
    k_HP=139
    k_ss=15

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


    FluxValue=Flux/(2*3.14159)
    FuelR1=1/(2*k_f)
    GapR1=1/(R_ci1*h_g)
    CladR1=1/16.3*np.log(R_co1/R_ci1)
    SSR1=1/k_ss*np.log(R_sso1/R_ssi1)
    CladR2=1/k_c*np.log(R_ci2/R_co2)
    GapR2=1/(h_g*R_f2)
    FuelR2=1/k_f
    GapR3=1/(h_g*R_ci3)
    CladR3=1/k_c*np.log(R_ci3/R_co3)
    SSR2=1/k_ss*np.log(R_sso2/R_ssi2)
    HPR1=1/k_HP*np.log(R_HPi1/R_HPo1)

    T_max = FluxValue*(FuelR1+GapR1+CladR1+SSR1+CladR2+GapR2+FuelR2+GapR3+CladR3+SSR2+HPR1)+T_HP+400
    T_gap1 = T_max-FluxValue*(FuelR1+GapR1)-33.3
    T_Clad1= T_max-FluxValue*(FuelR1+GapR1+CladR1)-66.6
    T_SS1= T_max-FluxValue*(FuelR1+GapR1+CladR1+SSR1)-100
    T_Clad2= T_max-FluxValue*(FuelR1+GapR1+CladR1+SSR1+CladR2)-133.3
    T_gap2=T_max-FluxValue*(FuelR1+GapR1+CladR1+SSR1+CladR2+GapR2)-166.6
    T_fuel2 = T_max-FluxValue*(FuelR1+GapR1+CladR1+SSR1+CladR2+GapR2+FuelR2)-200
    T_gap3= T_max-FluxValue*(FuelR1+GapR1+CladR1+SSR1+CladR2+GapR2+FuelR2+GapR3)-275
    T_Clad3= T_max-FluxValue*(FuelR1+GapR1+CladR1+SSR1+CladR2+GapR2+FuelR2+GapR3+CladR3)-350
    T_SSR2 = T_max-FluxValue*(FuelR1+GapR1+CladR1+SSR1+CladR2+GapR2+FuelR2+GapR3+CladR3+SSR2)-375
    T_HP = T_max-FluxValue*(FuelR1+GapR1+CladR1+SSR1+CladR2+GapR2+FuelR2+GapR3+CladR3+SSR2+HPR1)-400

    #T_HP_out = FluxValue*(FuelR1+GapR1+CladR1+SSR1+CladR2+GapR2+FuelR2+GapR3+SSR2)+T_HP+400
    #T_SS_HP = FluxValue*(FuelR1+GapR1+CladR1+SSR1+CladR2+GapR2+FuelR2+GapR3)+T_HP+400

    Temp = [T_max,T_gap1, T_Clad1,T_SS1,T_Clad2, T_gap2, T_fuel2, T_gap3, T_Clad3, T_SSR2, T_HP]
    return(Temp)

#Resistance values
T_K=760
T_Na=900
T_Ce=670
TempK=Temp(T_K)
TempNa=Temp(T_Na)
TempCe=Temp(T_Ce)

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

R=[R_f1, R_ci1, R_co1, R_ssi1, R_sso1, R_co2, R_ci2, R_f2, R_f3, R_ci3, R_co3]
green_dot=mpatches.Patch(color='green', label= "Potassium")
red_dot=mpatches.Patch(color='red', label= "Sodium")
blue_dot = mpatches.Patch(color='blue', label="Caesium")
plt.legend(handles=[green_dot, red_dot, blue_dot])
plt.plot(R,TempK,'go', R, TempNa, 'ro', R, TempCe, 'bo')
#plt.plot(R_f1, T_max, R_ci1, T_gap1, R_co1, T_Clad1, R_ssi1, T_SS1, R_sso1, T_Clad2, R_co2, T_gap2, 'ro')
plt.ylabel("Temperature (C)")
plt.xlabel("Distance (m)")
plt.title("Temperature as a Function of Distance from Fuel Centerline")
plt.show()
