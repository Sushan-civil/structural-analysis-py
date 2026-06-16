import openseespy.opensees as ops
import matplotlib.pyplot as plt
import numpy as np

ops.wipe()
ops.model('basic','-ndm',2,'-ndf',3)

ops.node(1,0,0)
ops.node(2,10,0)

ops.fix(1,1,1,1)
ops.geomTransf('Linear',1)
ops.element('elasticBeamColumn',1,1,2,10,29000,100,1)

ops.timeSeries('Linear',1)
ops.pattern('Plain',1,1)

ops.eleLoad('-ele',1,'-type','-beamUniform',-10,0)   # wy,wx

ops.constraints('Plain')
ops.numberer('RCM')
ops.system('BandGeneral')
ops.algorithm('Linear')
ops.integrator('LoadControl',1)
ops.analysis('Static')

ops.analyze(1)
ops.reactions()
print(f"Vertical deflection:{ops.nodeDisp(2,2):.4f}units")
print(f"At Support\n Shear force={ops.nodeReaction(1)[1]:.1f}")
print(f" Bending moment={ops.nodeReaction(1)[2]:.2f}")

#plot
w=-10
L=10
x=np.linspace(0,L,100)
V=-w*(L-x)
M=-w*(L-x)**2/2

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))

## SFD
ax1.plot(x,V,color='purple',linewidth=2)
ax1.fill_between(x,V,color='purple',alpha=0.15)
ax1.axhline(0,color='black',linewidth=1)
ax1.set_title('Shear Force Diagram',fontsize=12,fontweight='bold')
ax1.set_xlabel('Beam Length(L)',fontsize=10)
ax1.set_ylabel('Shear Force(V)',fontsize=10)
ax1.set_ylim(0,max(V)+10)
ax1.grid(True,linestyle=':',alpha=0.5)
ax1.text(0,max(V)+5,f"V={ops.nodeReaction(1)[1]:.1f})",color='purple',fontweight='bold',ha='left')


ax2.plot(x,M,color='green',linewidth=2)
ax2.fill_between(x,M,color='green',alpha=0.15)
ax2.axhline(0,color='black',linewidth=1)
ax2.set_title('Bending Moment Diagram',fontsize=12,fontweight='bold')
ax2.set_xlabel('Beam Length(L)',fontsize=10)
ax2.set_ylabel('Bending Moment(M)',fontsize=10)
ax2.set_ylim(0,max(M)+100)
ax2.grid(True,linestyle=':',alpha=0.5)
ax2.text(0,max(M)+20,f"M={ops.nodeReaction(1)[2]:.1f})",color='green',fontweight='bold',ha='left')

plt.tight_layout()
plt.show()






























