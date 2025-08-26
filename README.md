# LIMCA: LLM for Automating Analog In-Memory Computing Architecture Design Exploration

> ⚠️ **Under Construction**  
> This repository is actively evolving. Installation and usage sections are being finalized. Updates will be pushed regularly.
---

## Overview

**LIMCA** is a novel framework that leverages large language models (LLMs) to automate the design and evaluation of analog In-Memory Computing (IMC) crossbar architectures. By integrating an automated pipeline for SPICE netlist generation and validation, LIMCA significantly reduces design space exploration time and minimizes human intervention—all while satisfying strict power, area, and accuracy constraints.

This repository includes the implementation, dataset stubs, and scripts to reproduce results from our paper (to be released). Sections marked “🚧 WIP” will be filled in as we land features.

### Key Features
- **Automated Design Generation** — Generate IMC crossbar designs under constraints (e.g., power ≤ 3 W, accuracy ≥ 96%).
- **LLM-Based SPICE Netlist Creation** — Translate high-level specs into detailed SPICE netlists.
- **No-Human-In-Loop (NHIL) Verification** — Automated verification for hardware-aware constraints.
- **Extensible IMC Dataset** — Structured dataset capturing 400+ analog/digital IMC variants.

---

## Relationship to IMAC-Sim

This project **builds upon** and **references** [iCAS-Lab/IMAC-Sim](https://github.com/iCAS-Lab/IMAC-Sim) as a Git submodule. We do **not** copy code from IMAC-Sim; we reference it at `extern/IMAC-Sim`.

> If you’re cloning this repository, please use the `--recurse-submodules` flag below to fetch IMAC-Sim.

---

## Quick Start (🚧 WIP)

### 1) Clone with submodules
```bash
git clone --recurse-submodules https://github.com/ACADLab/LIMCA.git
cd LIMCA
```

If you already cloned without submodules:
```bash
git submodule update --init --recursive
```

---

## Usage (🚧 WIP)

Planned CLI:
```bash
limca generate \
  --spec configs/crossbar/a3w3.yaml \
  --constraints power<=3W accuracy>=96% \
  --out runs/exp001

limca verify --run runs/exp001 --nhil
```

---

## Roadmap
- [ ] Public configs for crossbar families
- [ ] SPICE generation & validation flows
- [ ] Reproducibility scripts
- [ ] Results & tables
- [ ] Dataset card + release notes

---

## Citing

If you use LIMCA in your work, please cite:

**LIMCA: LLM for Automating Analog In-Memory Computing Architecture Design Exploration**  
[arXiv:2503.13301](https://arxiv.org/abs/2503.13301)

BibTeX:
```bibtex
@misc{vungarala2025limcallmautomatinganalog,
      title={LIMCA: LLM for Automating Analog In-Memory Computing Architecture Design Exploration}, 
      author={Deepak Vungarala and Md Hasibul Amin and Pietro Mercati and Arnob Ghosh and Arman Roohi and Ramtin Zand and Shaahin Angizi},
      year={2025},
      eprint={2503.13301},
      archivePrefix={arXiv},
      primaryClass={cs.AR},
      url={https://arxiv.org/abs/2503.13301}, 
}
```


---

## License

This project is licensed under the [MIT License](LICENSE).

**Acknowledgment:** We reference [iCAS-Lab/IMAC-Sim](https://github.com/iCAS-Lab/IMAC-Sim) as an external dependency via Git submodule. Please consult their repository for their terms. No code from IMAC-Sim is copied into this repository.
