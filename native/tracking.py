"""Finite-domain electric-field overlap, not QNM normalization."""
import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.optimize import linear_sum_assignment

def overlap(a,b):
    axes=[np.asarray(a[k]) for k in 'xyz']; other=[np.asarray(b[k]) for k in 'xyz']
    if any(x.ndim!=1 or len(x)<2 or np.any(np.diff(x)<=0) for x in axes+other): raise ValueError('invalid axes')
    if any(x[0]<y[0]-1e-10 or x[-1]>y[-1]+1e-10 for x,y in zip(axes,other)): raise ValueError('reference region outside candidate')
    pts=np.stack(np.meshgrid(*axes,indexing='ij'),axis=-1)
    w=np.asarray(a['weights'])*np.asarray(a['eps']); shape=pts.shape[:-1]
    if w.shape!=shape or not np.all(np.isfinite(w)) or np.any(w<0): raise ValueError('invalid weights')
    u=np.stack([a[k] for k in ('Ex','Ey','Ez')]); v=np.stack([RegularGridInterpolator(other,b[k],bounds_error=True)(pts) for k in ('Ex','Ey','Ez')]);
    if u.shape!=v.shape or not np.all(np.isfinite(u)) or not np.all(np.isfinite(v)): raise ValueError('invalid fields')
    aa=np.sum(w*abs(u)**2); bb=np.sum(w*abs(v)**2)
    if aa<=0 or bb<=0: raise ValueError('zero field')
    return float(np.clip(abs(np.sum(w*u.conj()*v))**2/(aa*bb),0,1))

def match(refs,candidates):
    scores=np.array([[overlap(a,b) for b in candidates] for a in refs]); i,j=linear_sum_assignment(-scores)
    return [(int(x),int(y),float(scores[x,y])) for x,y in zip(i,j)]

if __name__=='__main__':
 import argparse,json
 p=argparse.ArgumentParser();p.add_argument('reference');p.add_argument('candidates',nargs='+');a=p.parse_args()
 with np.load(a.reference) as r:
  rows=[]
  for path in a.candidates:
   with np.load(path) as c: s=overlap(r,c)
   rows.append(dict(path=path,overlap=s,passes=s>=.95))
 print(json.dumps(sorted(rows,key=lambda x:-x['overlap']),indent=2))
