# PhotonLogic research history

Historical milestone results are numerical model outputs, not laboratory measurements.

| Stage | Scope and outcome | Validation |
|---|---|---|
| V1–V1.2.1 | Boolean NOR gates, multilayer transfer matrix, FDTD/FDFD convergence | Analytical/numerical |
| Logic/processor phase | Full adders, ALU, 8-bit toy CPU | Ideal logic |
| V9.1–V9.5 | All-optical regeneration and prior-art comparison | Hypothesis screens |
| V9.5.5–9.5.6 | Differential wavelength stabilization, energy restoration/fanout budgets | Reduced-order |
| V9.5.7–9.5.7.2 | Reservoir/photon nonlinear mode dynamics and gate transfer behavior | Reduced-order |
| V9.5.7.3–9.5.7.5 | Cavity Q vs speed, MZI and ring energy tradeoffs | Passive/idealized |
| V9.5.7.6–9.5.7.8.3 | Nonlinear envelope propagation, pulsed ring chains and dispersion | Envelope and TCMT |
| V9.5.7.9–9.5.7.9.2.2 | Scalar/vector screening, couplers, χ² and proposed nanocavities | Approximate |
| V9.5.7.9.2.3 | 1D Fourier–Bloch photonic bandgap solver | 1D numerical |
| V9.5.7.9.2.4–2.5.2 | Native 3D Meep scripts, Docker, finite-volume metrics, synthetic mode tracking | Preparation only |

## Quantitative lessons

* Simulated passive multilayer cavities exhibited a confinement-versus-speed tradeoff: Q up to ~134k for a high-reflectivity stack, with modeled lifetimes in tens of picoseconds.
* A hypothetical ideal MZI with Δn≈0.005, 47 μm active length and nonlinear coefficient 1e−15 m²/W suggested ~0.1 pJ; this coefficient is not verified for the proposed AlGaAs process.
* A later approximate AlGaAs straight-waveguide screen estimated ~34 pJ for an idealized π phase shift over 117.5 μm using n₂≈1.5e−17 m²/W.
* A cavity loading model predicted 22–53 fJ only for a *prescribed* nonlinear volume V≈0.1(λ/n)³ and a single-linewidth switching proxy, not a demonstrated optical gate.
* Initial scalar spatial nanocavity solutions did not show converged physical Q or mode volume.
* Meep is absent from the current computation environment, so intrinsic Q, radiation loss, optical switching, and actual nonlinear volume for PL-PC2B are **unknown**.

## Prior art pointers (not exhaustive)
- [Experimental organic-polariton NOT/NOR](https://www.nature.com/articles/s41467-024-49690-3)
- [Polariton transistor research](https://www.nature.com/articles/s41566-019-0392-8)
- [US20240152027A1](https://patents.google.com/patent/US20240152027A1/en)
- [US20110222856A1](https://patents.google.com/patent/US20110222856A1/en)

Patent scope, priority, family and current status require formal legal verification.

## Selected equations

**Kerr:** n(I)=n₀+n₂I.

**Resonant energy decay:** U(t)=U₀ exp(−t/τ), Q=ωτ.

**Passive loaded Q:** Q_L⁻¹=Q_i⁻¹+Q_e⁻¹+Q_abs⁻¹.

**Peak-energy volume:** V_pk=(∫ε|E|² dV)/max(ε|E|²).

**Nonlinear overlap-volume diagnostic:** V_NL=(∫ε|E|²dV)²/(∫active ε²|E|⁴ dV). Requires careful open-mode normalization and pump/probe tensor overlap.

**Mode overlap:** M=|∫ε E_ref*·E_test dV|² / (∫ε|E_ref|²dV ∫ε|E_test|²dV).

**MZI:** T≈sin²(Δφ/2) for ideal balanced components, bias dependent.

**Fanout power factor:** F ×10^(L_dB/10)/η_overlap.

**Control-energy screens** are proxy calculations, not an independently verified device operating energy.

## Reproducibility
See [remaining-history import](IMPORT_HISTORY.md). Previous 32 milestone snapshots and numerical datasets must be imported before claiming full reproducibility.
