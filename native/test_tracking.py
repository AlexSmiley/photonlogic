import unittest,numpy as np
from tracking import overlap,match

def field(n=11,phase=0,pol=0,shift=0):
 x=np.linspace(-1,1,n); X,Y,Z=np.meshgrid(x,x,x,indexing='ij'); f=np.exp(-4*((X-shift)**2+Y**2+Z**2))*np.exp(1j*phase); z=np.zeros_like(f)
 return dict(x=x,y=x,z=x,eps=np.ones_like(X),weights=np.ones_like(X)*(2/(n-1))**3,Ex=f if pol==0 else z,Ey=f if pol==1 else z,Ez=z)
class Tests(unittest.TestCase):
 def test_phase(self): self.assertAlmostEqual(overlap(field(),field(phase=2)),1)
 def test_polarization(self): self.assertAlmostEqual(overlap(field(),field(pol=1)),0)
 def test_grid(self): self.assertGreater(overlap(field(),field(17)),.99)
 def test_shift(self): self.assertLess(overlap(field(),field(shift=.5)),.95)
 def test_assignment(self): self.assertEqual([(i,j) for i,j,s in match([field(),field(pol=1)],[field(pol=1),field()])],[(0,1),(1,0)])
 def test_zero(self):
  b=field();b['Ex']*=0
  with self.assertRaises(ValueError): overlap(field(),b)
