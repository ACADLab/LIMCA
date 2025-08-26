# LIMCA: LLM for Automating Analog In-Memory Computing Architecture Design Exploration

**LIMCA** is a novel framework that leverages large language models (LLMs) to automate the design and evaluation of analog In-Memory Computing (IMC) crossbar architectures. By integrating an automated pipeline for SPICE netlist generation and validation, LIMCA significantly reduces design space exploration time and minimizes human intervention—all while satisfying strict power, area, and accuracy constraints.

---

## Overview

The LIMCA framework addresses the challenges of manual, knowledge-intensive design processes in analog IMC by:
- **Automating Design Space Exploration:** Systematically generating and evaluating a vast design space of IMC architectures under user-defined performance metrics.
- **Leveraging LLMs:** Utilizing a fine-tune-free LLM-driven approach for generating circuit netlists and performing SPICE-level simulations.
- **Enabling No-Human-In-Loop (NHIL) Verification:** Implementing an automated design verification phase that reduces manual debugging and iterative refinements.

This repository includes the complete implementation, dataset, and scripts to reproduce the experimental results presented in the paper.

---

## Key Features

- **Automated Design Generation:** Generate IMC crossbar designs based on specific power (≤3W), area, and accuracy (≥96%) constraints.
- **LLM-Based SPICE Netlist Creation:** Convert high-level design specifications into detailed circuit netlists for SPICE simulations.
- **Automated Verification:** Validate designs with an NHIL approach to ensure compliance with hardware-aware constraints.
- **Extensible IMC Dataset:** A structured dataset that captures over 400 analog and digital IMC variations to support future model fine-tuning and design exploration.

---
## Installation

To set up the LIMCA environment locally:

1. 


## License

This project is licensed under the [MIT License](LICENSE).
