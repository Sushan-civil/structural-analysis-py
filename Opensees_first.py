# Simple OpenseesPy code featuring a 2D cantilever beam#

import openseespy.opensees as ops

ops.wipe() 
ops.model('basic','-ndm',2,'-ndf',3)   ## it has 2 dimensions and 3 DOFs per node ##

## Geometry of Beam ##
##creating nodes on beam ## node(tag,x,y)
ops.node(1,0.0,0.0)      ## base of beam
ops.node(2,10.0,0)       ## free-end

## Boundary conditions ##
##fix(nodeTag,x,y,rotation)
ops.fix(1,1,1,1)    #fixed support at node 1

ops.geomTransf('Linear',1)   ## defining global coordinates for beam

## Defining the Beam element ##
## elasticBeamColumn(eleTag,iNode,jNode,Area,E,I,transfTag)
ops.element('elasticBeamColumn',1,1,2,10.0,29000.0,100.0,1)

## Defining Loads ##
ops.timeSeries('Linear',1)
ops.pattern('Plain',1,1)                       ##In OpenSees, loads are applied in patterns that follow a specific time-history

## Applying vertical load at free end ## load(nodeTag,Fx,Fy,Mz)
ops.load(2,0.0,-10.0,0.0)

## Analysis Commands ##
ops.constraints('Plain')
ops.numberer('RCM')
ops.system('BandGeneral')
ops.algorithm('Linear')
ops.integrator('LoadControl',1.0)
ops.analysis('Static')

## Execution ##
ops.analyze(1)
##get vertical displacement at node 2, DOF2
displacement=ops.nodeDisp(2,2)
print(f"Vertical displacement at the free end: {displacement} inches")

## Reactions at Support ##
ops.reactions()
node1_reaction= ops.nodeReaction(1)
print(f"Support Reaction (Fy): {node1_reaction[1]:.2f}")
print(f"Support Bending Moment (Mz): {node1_reaction[2]:.2f}")









