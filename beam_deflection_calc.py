# Program to calculate Shear force, Bending Moment and Deflection of a Beam #
# For Triangularly distributed load #

## Load Calculation ##
Dead_Load= float(input("Dead load= "))
Imposed_load= float(input("Imposed load= "))
Total_load= Dead_Load+Imposed_load
print("Total_load= ",Total_load)

## Physical Properties
L_span= float(input("length of span= "))           ### in m
Youngs_modulus= float(input("Young's Modulus= "))  ### in N/mm2
MOI= float(input("Moment of inertia= "))              ###in cm4

## CALCULATION ##
### Convert Triangular load to UDL? ###
Equivalent_UDL= input("convert triangular Load To Equivalent UDL? (Y/N): ")

if Equivalent_UDL == "Y":                    ### using formulas of UDL with load= 2*total_load/3 ###
    
    SF= round(L_span*Total_load/3,2)
    BM= round(Total_load*L_span**2/12,2)
    D=  "%.2F"%(5e12*Total_load*L_span**4/(5760000*Youngs_modulus*MOI))   ### 5e12= 5*10**12 ###
    
else:                                        ### using formulas for triangular load ###
    SF= "%.2f"%(L_span*Total_load/4)
    BM= round(Total_load*L_span**2/12,2)
    D=  "%.3F"%(1e12*Total_load*L_span**4/(1200000*Youngs_modulus*MOI))
    
##  OUTPUT  ##
print("Maximum Shear force= ", SF)       ## in KN
print("Maximum Bending Moment= ", BM)    ## in KN.m
print("Maximum vertical deflection= ",D) ## in mm

