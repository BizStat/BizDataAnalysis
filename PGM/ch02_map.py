import geopandas as gpd
import matplotlib.pyplot as plt

# Read the shapefile
sf = gpd.read_file('../DATA/TL_SCCO_SIG.shp')

sf.head()
sf.convex_hull.plot(color='gray', edgecolor="w")
