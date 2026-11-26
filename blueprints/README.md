# Experimental laboratory drawings — revision A

**NOT FABRICATION RELEASED.** No measured switching, radiation Q, or nonlinear volume. All dimensions are design starting points. Obtain foundry DRC, material characterization, laser safety approval and optical coupling design before manufacture.

## P1 — free-space organic polariton NOR reproduction

Reference: https://www.nature.com/articles/s41467-024-49690-3 . Reproduce the published stack and excitation conditions from its methods and supplement; do not substitute the approximate stack below without measuring the optical constants.

Conceptual stack: bottom 9.5 and top 6.5 SiO₂/Ta₂O₅ mirror pairs, 35 nm MeLPPP active film, nominal 50 nm silica spacers, approximate target 470 nm. Layer termination, actual thicknesses and pump wavelengths must be verified from the paper.

Use independently attenuated control A/B and pump, spatial/spectral filtering, calibrated detector and time-resolved measurement. Pump-only output is logical 1. Record all four input combinations and pump-off baseline. Repeat with two optically coupled stages before claiming cascadability.

## P2 — AlGaAs suspended nanobeam coupon

Nominal 7 µm length, 600 nm width, 350 nm thickness, period 350 nm. Hole centers x=±(j+0.3)a, j=1…8, y=0; radii a(0.22+0.08 min(j/5,1)). Through holes across thickness. Nominal index 3.28, target wavelength 1550 nm, alloy Al₀.₁₈Ga₀.₈₂As. See [nanobeam drawing](nanobeam.svg) and [hole coordinates](holes.csv).

This is an isolated cavity, **not** a complete mask: anchors, release, substrate, couplers, access waveguides, etch bias and alignment marks are not designed.

Start with passive spectroscopy, measure linewidth and ringdown, then calibrated pump/probe detuning. Sweep width 550/600/650 nm, period 340/350/360 nm, defect offset 0.2/0.3/0.4. Do not assume intrinsic Q=8000 or Vnl=0.02212 µm³.

## P3 — Kerr Mach–Zehnder reference

Two nominal 50:50 couplers, matched arms, 117.5 µm nominal active length, AlGaAs 600×350 nm cross section on silica (separate platform from suspended cavity). Prior scalar model estimates 200 nm gap and ~11.63 µm coupling length for 50:50; these are unvalidated. Pump injection/filtering require separate design. Measure passive splitting, insertion loss and phase bias first, then pump-induced phase and nonlinear absorption. An earlier 60 fJ prediction used hypothetical n₂; a later AlGaAs screen estimated ~34 pJ for an ideal straight-waveguide π shift.

## P4 — two-stage cascade / restoration bench

Two independently pumped P1 cells with relay optics and calibrated variable attenuation. Split output only after single-stage transfer curve measured. Record energy in each accepted spatial/spectral mode, pump energy, extinction, timing jitter, recovery and fanout. No electrical conversion in signal path; detectors are instrumentation. Require accepted-mode gain and noise margins before extension to logic board.

## Lab acceptance and safety

Use approved enclosed/interlocked laser setup, qualified personnel, wavelength-specific protective equipment and beam dumps; invisible 1550 nm radiation is hazardous. No laser operating power prescription is supplied. Measure low-power passive response first. Record device ID, temperature, polarization, wavelength, pulse width, input/output energy, uncertainty, raw traces and calibration.

For NOR test: 00→1, 01/10/11→0. Initial targets ER≥30 dB, ON transmission≥95% (passive switch reference), loaded lifetime≤1 ps, control≤60 fJ; targets are not measurements. Distinguish control energy from total optical pump and wall-plug energy. Stop if damage or thermal drift occurs. Do not release fabrication before full-vector open-boundary convergence and foundry review.
