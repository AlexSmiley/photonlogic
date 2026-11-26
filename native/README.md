# PL-FVM6.2.2 — native 3D resonance and mode tracking

This solver **has not been executed** in the current environment. Native Meep API compatibility and DFT field alignment require verification on a workstation. No physical Q, resonance, volume or switching performance is established.

```bash
docker compose build
docker compose run --rm solver python -m unittest -v
docker compose run --rm solver python native.py --resolution 30 --out results/ref
docker compose run --rm solver python native.py --resolution 40 --out results/candidate
docker compose run --rm solver python tracking.py results/ref/fields.npz results/candidate/fields.npz
```

`--mode-index` selects zero-based rank among positive-Q modes sorted by proximity to 1/1.55 µm⁻¹; inspect modes.json. Geometry parameters: `--period`, `--width`, `--thickness`, `--defect` (dimensionless center offset).

Evaluate electromagnetic mode identity across mesh, boundary, geometry and frequency changes. Finite-domain field volumes and overlap do **not** constitute rigorous quasinormal-mode normalization. Synthetic overlap tests pass in the previous archive, but no native solver result has been verified.
