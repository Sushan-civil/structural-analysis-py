
import openseespy.opensees as ops
import matplotlib.pyplot as plt
ops.wipe()
ops.model('basic','-ndm',2,'-ndf',3)

# Geometry #
ops.node(1,0,0)
ops.node(2,0,5)

ops.fix(1,1,1,1)
ops.geomTransf('Linear',1)

ops.element('elasticBeamColumn',1,1,2,10,29000,100,1)
# Loads #
ops.timeSeries('Linear',1)
ops.pattern('Plain',1,1)
ops.load(2,0,-50,0)

# Analysis #
ops.constraints('Plain')
ops.numberer('RCM')
ops.system('BandGeneral')
ops.algorithm('Linear')
ops.integrator('LoadControl',1)
ops.analysis('Static')

ops.analyze(1)

ops.reactions()
reaction_node1= ops.nodeReaction(1)  ## Returns list: [Rx, Ry, Mz]
axial_reaction= reaction_node1[1]  ## Vertical reaction force (Ry)
moment_reaction= reaction_node1[2]

print(f"Support Shear Reaction: {axial_reaction} and Support Moment: {moment_reaction}")

#drawing column
plt.figure(figsize=(5,5))
plt.plot([0,0],[0,5], color='gray',linestyle='-',linewidth=4,label='Column') #(x1,x2),[y1,y2

plt.arrow(0,7.2,0,-1.7,head_width=0.3, head_length=0.3,fc='red',ec='red',linewidth=2)
plt.text(0,7,'Applied Load\n=50 units',color='red',fontweight='bold') 

plt.arrow(0,-2.2,0,1.7,head_width=0.3,head_length=0.3,fc='blue',ec='blue',linewidth=2)  
plt.text(0.3, -1.5, f'Axial Reaction\n= {axial_reaction:.1f} units', color='blue', fontweight='bold', va='center')

#labels and plot grid characteristics#
plt.title('OpenseesPy Coloumn forces and Reactions',fontsize=11,fontweight='bold')
plt.xlim(-3,3)
plt.ylim(-4,9)
plt.grid(True,linestyle='-.',alpha=0.5)
plt.legend(loc='lower right')
plt.axhline(0,color='black',linewidth=0.5)

plt.show()








    
