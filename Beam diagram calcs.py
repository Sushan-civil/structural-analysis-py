import numpy as np
import matplotlib.pyplot as plt

print("Analysis of Simply supported beam with triangluar Tent-type loading")

##INPUT##
Peak_load=float(input("Peak load (w0)= "))
w0=Peak_load
L= float(input("length of span(m)= "))
E= float(input("Young's Modulus(N/mm2)= "))
I= float(input("Moment of Inertia(cm4)= "))    ### using different units for learning purposes###

##Converting units##
E_Pa= E*1e6                                    ### N/mm2 to N/m2
I_m4= I*1e-8                                   ### cm4 to m4

## Reactions at Supports ##
Ra= w0*L/4
Rb= w0*L/4

## Maximum calculations ##
SF_max= w0*L/4    
BM_max= w0*L**2/12
D_max= w0*1e3*L**4/(120*E_Pa*I_m4)*1e3   ### in mm
print()
print("RESULTS")
print(f"Reactions at ends={Ra:.2f}kN and {Rb:.2f}kN")
print(f"Maximum Shear Force= {SF_max:.2f}kN at Supports")
print(f"Maximum Bending Moment= {BM_max:.3f} kN.m at midspan")
print(f"Maximum deflection= {D_max:.1f} mm at midspan")

## For Plots ##
x=np.linspace(0,L,500)            ### defining x as a no. of positions throughout L ###

### Defining value of loads at different positions of x ###
### Left half of peak load: w=2*w0*x/L
### Right half of peak load: w=2*w0*(L-x)/L

w=np.where(x<=L/2,
           2*w0*x/L,
           2*w0*(L-x)/L)

### Shear force at x ###
### Left half: V=Ra-w0*x^2/L
### Right half: V=-Ra+w0*(L-x)^2/L
V= np.where(x<=L/2,
            Ra-w0*x**2/L,
            -Ra+w0*(L-x)**2/L)

### Bending Moment at x ###
### Left half: M= Ra*x-w0*x^3/3L
### Right half: M= Ra*(L-x)-w0*(L-x)^3/3L
M= np.where(x<=L/2,
            Ra*x-w0*x**3/(3*L),
            Ra*(L-x)-w0*(L-x)**3/(3*L))

fig,axes= plt.subplots(3,1, figsize=(10,10))

### Load Diagram ###
axes[0].plot(x,w, color="orange")       ### line color
axes[0].set_title("Load Diagram")       ### Title of diagram
axes[0].set_xlabel("Span (m)")          ### x-axis as span length
axes[0].set_ylabel("Load (kN/m)")       ### y-axis as Load
axes[0].axhline(0, color="black", linewidth=0.8)  ### drawing horizontal line as x-axis

### Shear force Diagram ###
axes[1].plot(x,V, color="blue")       
axes[1].set_title("Shear Force Diagram")      
axes[1].set_xlabel("Span (m)")         
axes[1].set_ylabel("Shear Force (kN)")       
axes[1].axhline(0, color="black", linewidth=0.8)

### Bending moment Diagram ###
axes[2].plot(x,M, color="green")       
axes[2].set_title("Bending Moment Diagram")      
axes[2].set_xlabel("Span (m)")         
axes[2].set_ylabel("Bending Moment (kN.m)")       
axes[2].axhline(0, color="black", linewidth=0.8)

plt.tight_layout()
plt.show()



