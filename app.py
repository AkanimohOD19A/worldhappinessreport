import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

## Title - 1
html_temp = """
<div>
    <h1 style = "color:#80471c; text-align:left;">
        World Happiness Report - 2021
    </h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

### Info
"""
Happiness can be a subjective term, especially when every country has to be considered. 
In this Exploratory Data Analysis, the collected [data]() is formed on various parameters that 
are general indicators of healthy living and upward mobility. 

For emphasis the only African countries has been filtered for exploration.
"""

## Read Data
"""
##### DATA SAMPLE
"""
df = pd.read_csv('WorldHappinessReport/world-happiness-report.csv')

### Cleaning
df = df.rename(columns={'Country name': 'Country'})

africa = ['Angola',  'Benin', 'Botswana', 'Burkina Faso',
          'Burundi', 'Cameroon', 'Central African Republic', 'Chad',
          'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Djibouti', 'Egypt',
          'Ethiopia', 'Gabon', 'Gambia', 'Ghana',
          'Guinea', 'Ivory Coast', 'Jamaica', 'Kenya',
          'Lesotho', 'Liberia', 'Libya', 'Madagascar',
          'Malawi', 'Malaysia', 'Mali', 'Mauritania',
          'Mauritius', 'Morocco', 'Mozambique', 'Namibia',
          'Niger', 'Nigeria', 'Rwanda', 'Senegal',
          'Sierra Leone', 'Somalia', 'Somaliland region', 'South Africa',
          'South Sudan', 'Sudan', 'Swaziland', 'Tanzania',
          'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

frames = []
for country in africa:
    country = df[df['Country'] == country]
    frames.append(country)
    df2 = pd.concat(frames)

na = ['Algeria',
      'Egypt',
      'Libya',
      'Liberia',
      'Morocco',
      'Sudan',
      'South Sudan',
      'Tunisia']

sa = ['Botswana',
      'Namibia',
      'South Africa']

ea = ['Burundi',
      'Djibouti',
      'Ethiopia',
      'Malawi',
      'Mauritius',
      'Mozambique',
      'Kenya',
      'Rwanda',
      'Somalia',
      'Tanzania'
      'Uganda',
      'Zambia',
      'Zimbabwe']

ca = ['Angola', 'Cameroon', 'Central African Republic',
      'Chad', 'Congo (Brazzaville)', 'Congo (Kinshasa)']

n_wa = na + sa + ea + ca

wa = []
for country in africa:
    if country not in n_wa:
        wa.append(country)

### Creating Regions
df2.insert(2, 'Regional indicator', ' ')
## Southern African
for i in df2['Country']:
    for j in sa:
        if i == j:
            df2.loc[df2['Country'] == i, "Regional indicator"] = "Southern Africa"

## Northern Africa

for i in df2['Country']:
    for j in na:
        if i == j:
            df2.loc[df2['Country'] == i, "Regional indicator"] = "Northern Africa"

## Eastern Africa

for i in df2['Country']:
    for j in ea:
        if i == j:
            df2.loc[df2['Country'] == i, "Regional indicator"] = "Eastern Africa"

## Central Africa

for i in df2['Country']:
    for j in ca:
        if i == j:
            df2.loc[df2['Country'] == i, "Regional indicator"] = "Central Africa"

## Western Africa

for i in df2['Country']:
    for j in wa:
        if i == j:
            df2.loc[df2['Country'] == i, "Regional indicator"] = "Western Africa"

# ----------#
st.write(df2)

#### Options
year_options = df2['year'].unique().tolist()
region_options = df2['Regional indicator'].unique().tolist()

year_selected = st.selectbox("Which year would you like to see?", year_options, 0)
region_selected = st.multiselect("Which country would you like to see?", region_options, ['Western Africa'])

df2 = df2[df2['Regional indicator'].isin(region_selected)]
df2 = df2[df2['year'] == year_selected]

fig = px.scatter(df2, x="Life Ladder", y="year", color = "Regional indicator", hover_name="Country",
                 log_x=True, size_max=55, animation_frame = "year", animation_group="Country")

fig.update_layout(width=800)
st.write(fig)

## Layout Data

## Animate Data Plots
# fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 30
# fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5

# fig.update_layout(width=800)
#
# st.write(fig)