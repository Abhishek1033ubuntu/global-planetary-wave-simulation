# Cell 4: Generate High-Contrast Pixelated Mapping Output
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

print("Step 6: Generating high-contrast pixelated global teleconnection map...")

plt.figure(figsize=(16, 9))
# Implement Robinson spherical projection array centered at 0 degrees longitude
ax = plt.axes(projection=ccrs.Robinson(central_longitude=0))

# Lay down geographical decorations
ax.coastlines(resolution='110m', color='#2c3e50', linewidth=1.5)
ax.gridlines(draw_labels=True, color='gray', alpha=0.2, linestyle='--')

# Define sharp, discrete visual bins to maximize variance boundaries
color_levels = np.linspace(-1.5, 1.5, 13)

# Render the high-contrast quantized choropleth layout
pixel_plot = global_susceptibility.plot(
    ax=ax, 
    transform=ccrs.PlateCarree(), 
    cmap='RdBu_r', 
    robust=True,
    levels=color_levels,
    cbar_kwargs={
        'label': 'Global Fluid Coupling Coefficient (Delta MCI / Delta Forcing)', 
        'shrink': 0.75,
        'orientation': 'horizontal',
        'pad': 0.06,
        'ticks': [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5]
    }
)

# Academic Title configuration
title_string = "Quantized Global Planetary Wave & Biophysical Coupling Matrix\n" + \
               "Discrete Variance: Lower Boundary Forcing vs 200 hPa Jet Stream Sinuosity (1990–2020)"
plt.title(title_string, fontsize=14, weight='bold', pad=15)

# Save a production-quality 300 DPI layout to local workspace memory for report embedding
plt.savefig('global_wave_simulation_highres.png', dpi=300, bbox_inches='tight')
print("💾 High-resolution image saved to workspace as 'global_wave_simulation_highres.png'")

plt.tight_layout()
plt.show()