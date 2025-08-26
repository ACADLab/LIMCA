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
