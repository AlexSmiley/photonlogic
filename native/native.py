"""UNEXECUTED Meep workflow. Run with conda-forge pymeep. Length units: um, c=1."""
import argparse,json
from pathlib import Path
import numpy as np
from analysis import volumes

def main():
 import meep as mp
 p=argparse.ArgumentParser()
 p.add_argument('--resolution',type=int,default=30)
 p.add_argument('--period',type=float,default=.35)
 p.add_argument('--pml',type=float,default=1)
 p.add_argument('--time',type=float,default=3000)
 p.add_argument('--out',default='run')
 p.add_argument('--mode-index',type=int,default=None)
 p.add_argument('--width',type=float,default=.6)
 p.add_argument('--thickness',type=float,default=.35)
 p.add_argument('--defect',type=float,default=.3)
 a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=True,parents=True)
 f=1/1.55
 geom=[mp.Block(size=mp.Vector3(7,a.width,a.thickness),material=mp.Medium(index=3.28))]
 for s in [-1,1]:
  for j in range(1,9):
   geom.append(mp.Cylinder(radius=a.period*(.22+.08*min(j/5,1)),height=a.thickness,center=mp.Vector3(s*(j+a.defect)*a.period),material=mp.air))
 def make(freq,width):
  return mp.Simulation(cell_size=mp.Vector3(9+2*a.pml,2+2*a.pml,2+2*a.pml),geometry=geom,boundary_layers=[mp.PML(a.pml)],sources=[mp.Source(mp.GaussianSource(freq,fwidth=width),component=mp.Ey,center=mp.Vector3())],resolution=a.resolution)
 sim=make(f,.2*f)
 h=mp.Harminv(mp.Ey,mp.Vector3(),f,.2*f)
 sim.run(mp.after_sources(h),until_after_sources=a.time)
 modes=[dict(freq=float(m.freq),Q=float(m.Q),err=float(m.err)) for m in h.modes]
 (out/'modes.json').write_text(json.dumps(modes,indent=2))
 valid=[m for m in modes if m['Q']>0 and m['freq']>0]
 if not valid: raise RuntimeError('No positive-Q mode detected')
 valid.sort(key=lambda m:abs(m['freq']-f))
 m=valid[0 if a.mode_index is None else a.mode_index]
 sim.reset_meep()
 sim=make(m['freq'],min(.02*f,m['freq']/max(m['Q'],1)*5))
 comps=[mp.Ex,mp.Ey,mp.Ez,mp.Hx,mp.Hy,mp.Hz]
 region=mp.Volume(center=mp.Vector3(),size=mp.Vector3(8,1.8,1.8))
 mon=sim.add_dft_fields(comps,m['freq'],0,1,where=region)
 sim.run(until_after_sources=a.time)
 fields=[sim.get_dft_array(mon,c,0) for c in comps]
 x,y,z,weights=sim.get_array_metadata(dft_cell=mon)
 eps=sim.get_array(center=region.center,size=region.size,component=mp.Dielectric)
 np.savez_compressed(out/'fields.npz',eps=eps,x=x,y=y,z=z,weights=weights,**dict(zip(['Ex','Ey','Ez','Hx','Hy','Hz'],fields)))
 if any(v.shape!=eps.shape for v in fields) or np.shape(weights)!=eps.shape: raise RuntimeError('Grid alignment requires inspection')
 result=volumes(eps,fields[:3],eps>1.01,weights)
 result.update(m,wavelength_nm=1000/m['freq'])
 (out/'diagnostics.json').write_text(json.dumps({k:float(v) for k,v in result.items()},indent=2))
if __name__=='__main__': main()
