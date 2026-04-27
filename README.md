# Baton Rouge Housing Data Explorer (Streamlit App)
Brandon Rugg | September 2025

Interactive geospatial dashboard for exploring socioeconomic and housing characteristics across Baton Rouge census tracts.

This project was developed during a DataKind DC DataDive (civic data hackathon) in collaboration with Georgetown/GWU partners. The work was presented at the end of the event to Baton Rouge government stakeholders who participated virtually. The original dataset and initial preprocessing were provided by event organizers. The folder `Streamlit_App_BKR` contains my contribution: an interactive Streamlit application for exploratory analysis and visualization.

## Interactive Dashboard

View the deployed app here:  
https://baton-rouge-housing-and-health-myxtvk7g5ntbpvbezmv4bj.streamlit.app/

## Features

This dashboard allows users to:

- Explore census-tract level geographic variation in Baton Rouge housing and demographic variables  
- Generate choropleth maps for selected socioeconomic indicators  
- Examine correlation structure across variables via heatmaps 
- Interactively compare relationships between two variables using scatterplots  
- View computed Pearson correlation coefficients  

## Data

The app uses a processed GeoJSON dataset containing census-tract level features:

- Population and demographic composition (race/ethnicity shares)
- Income distribution and tenure-stratified income measures (owner vs renter)
- Poverty indicators, including child poverty metrics
- Housing occupancy and tenure (owner-occupied vs renter-occupied vs vacant units)
- Housing structure (single-family vs multi-family units, bedroom counts)
- Housing age composition proxies (e.g., percent built after 2000, before 1980)
- Rent and cost burden metrics (including 30%+ and 50%+ burden thresholds)

Source data was provided as part of the DataKind DC DataDive project materials and extended during exploratory analysis.

## Event Context (DataKind DC DataDive)

This project originated from a one-day civic data hackathon organized by DataKind DC in collaboration with George Washington University.

Participants worked in teams to explore real-world datasets supporting policy-relevant questions related to housing, health, and urban development.

At the end of the event, participants presented results to organizers and Baton Rouge government stakeholders who joined virtually.

https://www.meetup.com/datakind-dc/events/310923763/
