# PhotonLogic — All-Optical Computing Research

> **Experimental research only.** No native three-dimensional nanocavity validation, hardware measurement or verified 60 fJ switching demonstration exists yet.

PhotonLogic investigates optically powered logic gates, regeneration, nanocavity switching and scalable optical computing (Architecture C).

## Project
- [Laboratory prototype drawings](blueprints/README.md)
- [Nanobeam top-view drawing](blueprints/nanobeam.svg)
- [Hole coordinate table](blueprints/holes.csv)
- [React research dashboard](web/)
- [Development and scientific history](docs/RESEARCH_HISTORY.md)
- [Import remaining historical research](docs/IMPORT_HISTORY.md)

## Local web
```bash
cd web
npm install
npm test
npm run dev
```

Vercel: root directory `web`, framework **Vite**, build `npm run build`, output `dist`. The frontend runs analytical/illustrative models; 3D Maxwell solvers run separately on a workstation.

## Scientific status
Optical NOR reference (visible polariton) and AlGaAs nanobeam/Kerr and MZI variants at ~1550 nm are different experimental branches. Prior work includes transfer-matrix modeling, FDFD, rate equations, normalized logic gates, coupled-mode calculations, idealized waveguide and cavity energy screens, 1D bandgap modeling and preliminary native solver code. Many results use uncalibrated material parameters. The native 3D Meep stage remains unexecuted.

## Safety, patents and publication
**This repository is currently public.** Research disclosures may affect patent rights; consult qualified patent counsel before publishing new inventions or fabrication-enabling details. Experimental designs are **not fabrication released**. Qualified laboratory personnel must follow laser and cleanroom safety rules. No guarantee of novelty or patentability is made.

The consolidated historical source/data ZIP is available as a separate conversation attachment; this branch currently contains the selected documentation, frontend and starting blueprints, **not yet every historical simulator or dataset**.
