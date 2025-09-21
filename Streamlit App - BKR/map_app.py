import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import numpy as np
from streamlit_folium import st_folium

# Load GeoJSON
gdf = gpd.read_file(r'../Output Data/housing_data_with_geometry.geojson')

# Page title
st.title("Comparison of Baton Rouge Housing Data")
st.text("Select variable to plot from dropdown menu. More variables are accessible from the GeoJSON dataframe. Code to add additional variables to the source GeoJSON exists in 'exploratory_analysis.ipynb'")

# Numeric columns dropdown
numeric_cols = [
    'Total_Population',
    'Percent_Black',
    'Percent_White',
    'Percent_Hispanic',
    'Children_Below_Poverty',
    'Percent_Children_Below_Poverty',
    'Median_Household_Income',
    'Percent_Low_Income_Under_35K',
    'Percent_High_Income_100K_Plus',
    'Percent_Below_Poverty',
    'Percent_Households_Below_Poverty',
    'Percent_Occupied',
    'Percent_Vacant',
    'Percent_Renter_Occupied',
    'Percent_High_Rent_Burden_30_Plus',
    'Percent_Built_Pre_1980',
    'Percent_Built_2000_Plus'
]

### Geographic Map

selected_var = st.selectbox("Select variable to plot:", numeric_cols)

# Create Folium map
m = folium.Map(location=[30.4615, -91.1371], zoom_start=10)

# Add choropleth
folium.Choropleth(
    geo_data=gdf,
    data=gdf,
    columns=['GEOID', selected_var],
    key_on='feature.properties.GEOID',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name=selected_var,
).add_to(m)

# Display map
st_folium(m, width=700, height=800)

st.markdown("---")

### Correlation matrix

st.subheader("Correlation Matrix of Selected Variables")


# Compute correlation matrix
corr_matrix = gdf[numeric_cols].corr()

# Create a mask for the upper triangle
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Upper triangle

# Plot heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    mask=mask,               # Mask upper triangle
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    cbar=True,
    ax=ax
)
ax.set_title("Correlation Matrix (Lower Triangle)")
st.pyplot(fig)


st.markdown("---")

### Explore correlations in more detail
st.subheader("Explore Correlation Between Variables")
# Dropdowns for x and y
var_x = st.selectbox("Select X variable:", numeric_cols)
var_y = st.selectbox("Select Y variable:", numeric_cols)

# Scatter plot
fig, ax = plt.subplots()
ax.scatter(gdf[var_x], gdf[var_y], alpha=0.6)
ax.set_xlabel(var_x)
ax.set_ylabel(var_y)
ax.set_title(f"{var_x} vs {var_y}")

st.pyplot(fig)

# Display correlation
corr = gdf[var_x].corr(gdf[var_y])
st.write(f"Correlation coefficient: {corr:.2f}")