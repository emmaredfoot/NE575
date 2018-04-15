#Dimensions in m
Fuel = .0055
Clad_Inner = .0056
Clad_Outer = .005950
SS316 = .0092
HPi = 0.0094
gap = 3.6e-4
fuel_length = 1.10
FP_Volume = fuel_length*3.1415*Fuel**2

k_gas = 0.142
E_c = 0.90
E_f = 0.79
SB = 5.67e-8
gamma = .98

Power = 5e6
Rods = 3456

#Average Volumetric Energy Generation Rate
Volume_gen_rate = gamma*Power/(FP_Volume*Rods)
print(Volume_gen_rate/1e6)
