# Cell 3: Execute Cross-Grid Empirical Statistical Matrix
import numpy as np
from scipy.stats import pearsonr

print("Step 5: Running whole-planet cross-grid statistical validation...")

# Flatten arrays for two-tailed correlation screening
mci_flat = delta_mci.values.flatten()
forcing_flat = delta_forcing.values.flatten()

# Filter out any potential infinite bounds or NaN cells safely
valid_mask = np.isfinite(mci_flat) & np.isfinite(forcing_flat)

r_global, p_global = pearsonr(forcing_flat[valid_mask], mci_flat[valid_mask])

print("\n=== FINAL GLOBAL-SCALE EMPIRICAL STATISTICAL METRICS ===")
print(f"Global Pearson Correlation Coefficient (r): {r_global:.4f}")
print(f"Global Statistical Significance (p-value): {p_global:.4e}")
print("========================================================")