<p align="center">
  <!-- change width value to resize logo -->
  <img src="fast_rv_logo_transparent.png" alt="FAST-RV logo" width="620">
</p>

# FAST-RV
[![CI](https://github.com/proxima786/FAST-RV/actions/workflows/ci.yml/badge.svg)](https://github.com/proxima786/FAST-RV/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

**F**irst-order **A**utomated **S**ingle-planet **T**ool for **R**adial **V**elocities) is a tiny, no-drama toolkit to grab **radial-velocity (RV) time series from VizieR** and fit a **simple Keplerian model — fast**.

No MCMC.  
No Bayesian rabbit holes.  
Just a clean first order look at your Radial velocity data !

Includes a classic demo of deriving the famous RV curve of "51 Pegasi b" (the first discovered exolpanet)

---

# What FAST-RV assumes

This package is intentionally **first-order** and works best when:

- The system contains **a single planet**
- The RV data comes from **a single instrument**
- The VizieR table follows a simple format where the **first three columns are**

```
time (days) | RV | RV error
```

(RV and error are often reported in **km/s or m/s**.)

If your table contains an `Inst` column (multiple instruments), simply **filter the data to one instrument** before running the fit.

---

# Where the data comes from

FAST-RV expects a **VizieR catalog ID**, which can be queried easily in Python  
(see the **51 Peg example notebook**).

The fitting routine is inspired by the **PyAstronomy KeplerRVModel** implementation.

You can estimate the orbital period using a **Lomb–Scargle periodogram**, but for best results it is recommended to use approximate parameters (period, eccentricity, etc.) from the **NASA Exoplanet Archive**.

### Useful links

VizieR catalog portal (CDS)  
https://vizier.cds.unistra.fr/

PyAstronomy KeplerRVModel  
https://pyastronomy.readthedocs.io/

NASA Exoplanet Archive  
https://exoplanetarchive.ipac.caltech.edu/

---

# Usage

### 1. Clone the repository

```bash
git clone https://github.com/proxima786/FAST-RV.git
pip install -r requirements.txt
pip install fast-rv
```

### 2. Open the example notebook

```
51_peg.ipynb
```

### 3. Choose a VizieR catalog

Change the `catalog_id` to any RV catalog you like.  
(Some example IDs are already provided in the notebook if you feel lazy.)

### 4. Run the notebook

The code will:

- load the RV time series  
- estimate the period  
- fit a Keplerian model  
- produce a **phase-folded RV curve**

### 5. Ta-da!

You now have your **own radial velocity orbit**.

---

# Contact

If you have questions, suggestions, or ideas for improvements:

📧 **jebraanjamil@gmail.com**
