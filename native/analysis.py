"""Finite-domain nondispersive field-volume diagnostics, not QNM normalization."""
import numpy as np

def volumes(eps, fields, active, dv):
    e2=sum(abs(np.asarray(f))**2 for f in fields)
    w=eps*e2
    u=(w*dv).sum()
    if u<=0: raise ValueError('zero field')
    return dict(peak_volume_um3=u/w.max(), nonlinear_volume_um3=u*u/((w*w*active*dv).sum()), active_fraction=(w*active*dv).sum()/u)

def ringdown(t, energy, wavelength=1.55):
    t=np.asarray(t); energy=np.asarray(energy)
    slope,intercept=np.polyfit(t,np.log(energy),1)
    if slope>=0: raise ValueError('not decaying')
    return -1/slope, -2*np.pi*299.792458/wavelength/slope
