# Cell 2: Ingest Binary Stream & Execute Planetary Fluid Formulations
import netCDF4 as nc
import xarray as xr
import numpy as np

print("Step 1: Ingesting global multi-decadal upper-air fluid fields via direct file stream...")
# Open using raw netCDF4 library directly to bypass active environment memory locks
nc_file = nc.Dataset('real_atmosphere.nc', mode='r')
ds = xr.open_dataset(xr.backends.NetCDF4DataStore(nc_file))

# Dynamically resolve variable names from the Copernicus structure
u_key = [k for k in ds.data_vars if 'u' in k.lower()][0]
v_key = [k for k in ds.data_vars if 'v' in k.lower()][0]
time_dim = [d for d in ds.dims if 'time' in d.lower()][0]

print("Step 2: Isolating global 200 hPa Jet Stream profiles (1990 vs 2020)...")
u_90 = ds[u_key].isel({time_dim: 0})
v_90 = ds[v_key].isel({time_dim: 0})
u_20 = ds[u_key].isel({time_dim: 1})
v_20 = ds[v_key].isel({time_dim: 1})

# Calculate Meridional Circulation Index (Sinuosity Framework)
mci_90 = np.abs(v_90) / (np.sqrt(u_90**2 + v_90**2) + 1e-5)
mci_20 = np.abs(v_20) / (np.sqrt(u_20**2 + v_20**2) + 1e-5)
delta_mci_raw = (mci_20 - mci_90).squeeze()

delta_mci = xr.DataArray(
    delta_mci_raw.values,
    coords={'latitude': delta_mci_raw.latitude.values, 'longitude': delta_mci_raw.longitude.values},
    dims=['latitude', 'longitude']
).sortby('latitude').sortby('longitude')

print("Step 3: Compiling Global Lower Planetary Boundary Forcing anomalies...")
forcing_90 = np.sqrt(u_90**2 + v_90**2)
forcing_20 = np.sqrt(u_20**2 + v_20**2)
delta_forcing_raw = (forcing_20 - forcing_90).squeeze()

delta_forcing = xr.DataArray(
    delta_forcing_raw.values,
    coords={'latitude': delta_mci.latitude.values, 'longitude': delta_mci.longitude.values},
    dims=['latitude', 'longitude']
).sortby('latitude').sortby('longitude')

print("Step 4: Computing global-scale fluid anomaly intersections...")
global_susceptibility = delta_mci / (delta_forcing - 1e-4)

print("✅ Global data structures processed and ready for mapping!")