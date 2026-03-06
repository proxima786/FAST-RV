<p align="center">
  <!-- change width value to resize logo -->
  <img src="fast_rv_logo_transparent.png" alt="FAST-RV logo" width="620">
</p>

# FAST-RV

[![CI](https://github.com/proxima786/FAST-RV/actions/workflows/ci.yml/badge.svg)](https://github.com/proxima786/FAST-RV/actions/workflows/ci.yml)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

**FAST-RV** (First-order Automated Single-planet Tool for Radial Velocities) is a lightweight Python toolkit for quickly analyzing exoplanet radial velocity data from VizieR catalogs.

It performs fast first-order Keplerian fitting and produces phase-folded radial velocity curves without going to any complexities of Bayesian inference / MCMC . 

## Features

- Fetch radial velocity time series from VizieR
- Estimate orbital period
- Fit a simple single-planet Keplerian model
- Generate phase-folded RV plots
- Example workflow for **51 Pegasi b**

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/proxima786/FAST-RV.git
cd FAST-RV
pip install -r requirements.txt
```

## Usage
```bash

import fast_rv
```

Example analysis is available in:
```bash

examples/51_peg.ipynb
```

## FAST-RV currently assumes:

- single-planet systems  
- a single instrument  
- standard VizieR RV tables (time, RV, RV error)

## License

MIT License. See `LICENSE` for details.

## Author

Jebraan Mudholkar
