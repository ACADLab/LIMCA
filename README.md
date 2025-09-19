# LIMCA: LLM for Automating Analog In-Memory Computing Architecture Design Exploration

<div align="center">

[![arXiv](https://img.shields.io/badge/arXiv-2503.13301-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2503.13301) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT) [![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=flat-square&logo=python)](https://www.python.org/) [![Under Construction](https://img.shields.io/badge/Status-Under%20Construction-orange.svg?style=flat-square)](https://claude.ai/chat/d71b8129-f9e8-42ba-8938-508e48de3e39#) [![GitHub stars](https://img.shields.io/github/stars/ACADLab/LIMCA?style=flat-square)](https://github.com/ACADLab/LIMCA/stargazers) [![GitHub issues](https://img.shields.io/github/issues/ACADLab/LIMCA?style=flat-square)](https://github.com/ACADLab/LIMCA/issues)

</div>

> ⚠️ **Under Construction**  
> This repository is actively evolving. Updates will be pushed regularly.

---

## 🎯 Overview

**LIMCA** is a novel framework that leverages Large Language Models (LLMs) to automate the design and evaluation of analog In-Memory Computing (IMC) crossbar architectures. By integrating an automated pipeline for SPICE netlist generation and validation, LIMCA significantly reduces design space exploration time and minimizes human intervention—all while satisfying strict power, area, and accuracy constraints.

Think of LIMCA as your intelligent hardware design assistant: just like how a skilled engineer can translate system requirements into detailed circuit designs, LIMCA uses LLMs to automatically generate and optimize IMC architectures based on your specifications.

### ✨ Key Features

- 🤖 **Automated Design Generation** — Generate IMC crossbar designs under constraints (e.g., power ≤ 3 W, accuracy ≥ 96%)
- 🔧 **LLM-Based SPICE Netlist Creation** — Translate high-level specs into detailed SPICE netlists
- 🚫👨‍💻 **No-Human-In-Loop (NHIL) Verification** — Automated verification for hardware-aware constraints
- 📊 **Extensible IMC Dataset** — Structured dataset capturing 400+ analog/digital IMC variants
- 🔄 **Design Space Exploration** — Systematic exploration across technology nodes and device types
- ⚡ **Hardware Automation** — Streamlined workflow from specification to validated design

---

## 🏗️ Architecture

```
LIMCA Framework
├── 🧠 LLM Engine (Design Generation)
├── 🔌 SPICE Netlist Generator
├── ✅ NHIL Verification System
├── 📈 Performance Analyzer
└── 📚 IMC Design Database
```

---

## 🔗 Relationship to IMAC-Sim

This project **builds upon** and **references** [iCAS-Lab/IMAC-Sim](https://github.com/iCAS-Lab/IMAC-Sim) as a Git submodule. We do **not** copy code from IMAC-Sim; we reference it at `extern/IMAC-Sim`.

> 💡 **Important**: If you're cloning this repository, please use the `--recurse-submodules` flag below to fetch IMAC-Sim.

---

## 🚀 Quick Start

###  Prerequisites

- Python 3.8 or higher
- Git with submodule support
- SPICE simulator (for netlist validation) - HSPICE

---

## 📖 Usage (🚧 WIP)

### Basic Design Generation

```bash
# Generate IMC crossbar design with constraints
limca generate \
  --spec configs/crossbar/16x16_7nm_RRAM \
  --constraints power<=3W accuracy>=96% \
  --out runs/exp001

# Verify generated design
limca verify --run runs/exp001 --nhil

# Analyze results
limca analyze --run runs/exp001 --report
```

### Dataset Generation

```bash
# Generate variations across technology nodes
python scripts/generate_variations.py \
  --template configs/base_template.py \
  --output datasets/imc_variations \
  --tech-nodes 7nm,14nm,16nm \
  --devices MRAM,RRAM,PCM
```

---
## 🗂️ Dataset

Our comprehensive IMC dataset includes:

- **400+ Design Variants** across multiple technology nodes (7nm to 20nm)
- **4 Memory Technologies**: MRAM, RRAM, CBRAM, PCM
- **3 Cell Architectures**: 1T1R, 2T1R, 1TG1R
- **Performance Metrics**: Power consumption, area, accuracy, error rates
- **SPICE Netlists**: Validated circuit implementations

### Dataset Structure (Analog only)

|Technology Node|Memory Type|Cell Type|Configurations|Status|
|---|---|---|---|---|
|7nm - 20nm|MRAM|1T1R, 2T1R, 1TG1R|72 variants|✅ Complete|
|7nm - 20nm|RRAM|1T1R, 2T1R, 1TG1R|72 variants|✅ Complete|
|7nm - 20nm|CBRAM|1T1R, 2T1R, 1TG1R|72 variants|✅ Complete|
|7nm - 20nm|PCM|1T1R, 2T1R, 1TG1R|72 variants|✅ Complete|


---

## 🔬 Research Applications

LIMCA is designed for researchers and engineers working on:

- **In-Memory Computing Architecture Design**
- **Hardware-Software Co-Design**
- **AI Accelerator Development**
- **Neuromorphic Computing Systems**
- **Edge AI Hardware Optimization**

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](https://claude.ai/chat/CONTRIBUTING.md) for details.

```

---

## 📚 Citation

If you use LIMCA in your research, please cite our paper:

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

## 📄 License

This project is licensed under the [MIT License](https://claude.ai/chat/LICENSE).

**Acknowledgment**: We reference [iCAS-Lab/IMAC-Sim](https://github.com/iCAS-Lab/IMAC-Sim) as an external dependency via Git submodule. Please consult their repository for their licensing terms. No code from IMAC-Sim is copied into this repository.

---

## 🆘 Support

- 📫 **Issues**: [GitHub Issues](https://github.com/ACADLab/LIMCA/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/ACADLab/LIMCA/discussions)
- 📧 **Email**: Contact the maintainers through GitHub

---

<div align="center">

**⭐ Star this repository if LIMCA helps your research! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/ACADLab/LIMCA?style=social)](https://github.com/ACADLab/LIMCA/stargazers)

</div>
