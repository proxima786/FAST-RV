#!/usr/bin/env python
# coding: utf-8

# In[119]:


import numpy as np
import matplotlib.cm
import matplotlib.pyplot as plt
cmap = matplotlib.cm.get_cmap("Spectral")
#%matplotlib widget
#matplotlib.use("TkAgg")
from matplotlib.widgets import RangeSlider
from PyAstronomy.modelSuite import KeplerRVModel
from astroquery.vizier import Vizier
from astropy.timeseries import LombScargle


# In[120]:


# if you are not sure what your table looks like, print the columns, set the table as needed
# to make the code work.
def vizier_table_inspection(catalog_id):
    """A function to inspect the table"""
    Vizier.ROW_LIMIT = -1
    tables = Vizier.get_catalogs(catalog_id)
    t = tables[0]
    author = Vizier(catalog = catalog_id).get_catalog_metadata()['authors']

    if len(t.colnames) < 3:
        raise ValueError("Table must have at least 3 columns: time, RV, RV error.")

    print("Table description:", t.meta.get("description", "N/A"))
    print("Total data points:", len(t))

    print("Time :", getattr(t.columns[0], "description", "N/A"))
    print("RV   :", getattr(t.columns[1], "description", "N/A"))
    print("Err  :", getattr(t.columns[2], "description", "N/A"))
    print("authors:" , author)

    return t


# In[121]:


# to make it work, the table should have 3 columns: time (days), RV, RV error
def get_vizier_data(catalog_id,name):
    """A function to get the contents of the table (assumes first 3 columns are time/RV/err)."""
    Vizier.ROW_LIMIT = -1
    t = Vizier.get_catalogs(catalog_id)[0]

    if len(t.colnames) < 3:
        raise ValueError("Table must have at least 3 columns: time, RV, RV error.")

    time_data = np.array(t.columns[0], dtype=float)
    time_description = getattr(t.columns[0], "description", "") or ""
    description = t.meta.get("description", "")

    rv_col = t.columns[1]
    err_col = t.columns[2]
    rv_data = np.array(rv_col, dtype=float)
    err_rv = np.array(err_col, dtype=float)

    # --- minimal unit handling ---
    # If RV is in km/s -> convert to m/s; if already m/s -> keep
    rv_unit = getattr(rv_col, "unit", None)
    err_unit = getattr(err_col, "unit", None)

    if rv_unit is not None and str(rv_unit) == "km / s":
        rv_data_ms = rv_data * 1e3
    else:
        rv_data_ms = rv_data

    if err_unit is not None and str(err_unit) == "km / s":
        err_rv_ms = err_rv * 1e3
    else:
        err_rv_ms = err_rv

    # plot original data in its native units (km/s if that's what the table is)
    plt.errorbar(time_data, rv_data, yerr=err_rv, fmt="ko", label= name)
    plt.title(f"{description}", fontsize=14)
    plt.xlabel(f"{time_description}", fontsize=14)
    plt.ylabel(f"RV [{rv_unit if rv_unit is not None else 'unknown'}]", fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.legend(fontsize=14)

    return time_data, rv_data_ms, err_rv_ms


# In[122]:


def run_periodogram(time, rv , error, min_period , max_period):
    """
    Runs a Lomb–Scargle periodogram and returns a first-order period guess.
    Note:
    - Uneven / nightly sampling can introduce alias peaks (often near 1 day and its harmonics),
    so the highest peak is not always the true orbital period.
    - If a reliable literature period is available (authors from vizier_table_inspection), 
    use it as the initial guess (or constrain per1) and treat the periodogram as a diagnostic.
    """
    min_freq = 1.0 / max_period
    max_freq = 1.0 / min_period
    ls = LombScargle(time, rv, error)
    frequency, power = ls.autopower(
    minimum_frequency=min_freq,
    maximum_frequency=max_freq,
    samples_per_peak=10,)  # oversampling
    period = 1.0 / frequency
    idx = np.argsort(period)
    power = power[idx]
    period = period[idx]
    period_guess = period[np.argmax(power)]
    plt.figure()
    plt.plot(period, power, "-")
    plt.xlabel("Period [days]" , fontsize =14)
    plt.ylabel("Lomb-Scargle power" , fontsize =14)
    plt.axvline(period_guess , color = "gray" , linestyle = "--", label = f'Best period : {period_guess:.3f}') 
    plt.xticks(fontsize =14)
    plt.legend()
    plt.yticks(fontsize =14)
    plt.xlim(min_period, max_period)
    return period_guess




# In[123]:


def fitting_rv_model(time, rv, err, **p):
    idx_t = np.argsort(time)

    model = KeplerRVModel(mp=1, deg=0)

    # unpack dictionary
    model["mstar"] = p["mstar"]
    model["per1"]  = p["per"]
    model["e1"]    = p["e"]
    model["w1"]    = p["w"]
    model["K1"]    = p["K"]

    # reasonable starting guesses
    model["tau1"] = np.nanmedian(time)
    model["c0"]   = np.nanmedian(rv)

    # Step 1: circular fit (robust) -> force e=0, w fixed
    model["e1"] = 0.0
    model["w1"] = 90.0

    model.thaw(["K1", "tau1", "c0"])
    model.freeze(["mstar", "per1", "e1", "w1"])
    model.fit(time[idx_t], rv[idx_t], yerr=err[idx_t])

    # smooth model curve for plotting
    xgrid = np.linspace(time[idx_t].min(), time[idx_t].max(), 2000)
    ygrid = model.evaluate(xgrid)

    return time[idx_t], rv[idx_t], err[idx_t], xgrid, ygrid, model


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




