import time
import streamlit as st
import pandas as pd
from pandas.api.types import CategoricalDtype
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

from src.cleaning import *

#Page Setup
st.set_page_config(
    page_title="Renewable Prediction",
    page_icon=":infinity:",
    layout="wide",
    initial_sidebar_state="expanded"
)

hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

def main():
    #Sidebar
    st.sidebar.title('Menu')

    #Selecting the Region
    region_select = st.sidebar.selectbox("Region:",df['Region'].unique())

    df = df.query('Region == @region_select')

    #Selecting the Country
    cntry_select = st.sidebar.selectbox("Country:",df['Country'].unique())


    df = df.query('Country == @cntry_select')
    pop = pop.query('Country == @cntry_select')
    dem = dem.query('Country == @cntry_select')
    lcoe = lcoe.query('Country == @cntry_select')
    fin = fin.query('Country == @cntry_select')

    #Selecting the year
    yr_select = str(st.sidebar.slider('Year:', 2000, 2021, 2000))

    df_select = df[['Country','Region','Technology',yr_select]]
    pop_select = pop[['Country','Region',yr_select]]
    dem_select = dem[['Country','Region',yr_select]]
    yr_fin = int(yr_select)
    fin_select = fin.query('Year == @yr_fin')

    #Main Body
    st.title(f':bar_chart: Renewable Production in {cntry_select}')


    #Section 1
    sec_1 = st.container()
    sec_1.header(f'Annual Report - {yr_select}', divider='gray')

    #KPIs Calculations
    production_2000 = float(df['2000'].sum())
    production_2021 = float(df['2021'].sum())
    demand_2000 = float(dem['2000'])
    demand_2021 = float(dem['2021'])

    if production_2000 == 0:
        growth_production = 0
        growth_demand = 0
    else:
        growth_production = (production_2021-production_2000)/(production_2000)
        growth_demand = (demand_2021-demand_2000)/(demand_2000)


    population_total = pop_select[yr_select].sum()
    total_production = df_select[yr_select].sum()
    production_percap = total_production/population_total
    production_rate = growth_production/(2021-2000)

    total_demand = dem_select[yr_select].sum()
    hab_demand = (total_production)/(population_total)
    growth_rate = growth_demand/(2021-2000)

    fin_percap = (fin_select['Investment_M_USD'].sum())/population_total

    df_select['Percentage'] = round((df[yr_select]/total_production),2)

    if yr_select != '2000':
        yr = int(yr_select)
        prev_yr = str(yr-1)
        prev_production = df[prev_yr].sum()
        delta_production = ((total_production-prev_production)/total_production)
        prev_demand = dem[prev_yr].sum()
        delta_demand = ((total_demand-prev_demand)/total_demand)
    else:
        delta_production = 0
        delta_demand = 0

    #Section layout section 1
    col1_s1, col2_s1, col3_s1 = sec_1.columns(3, gap='large')

    #Printing the metrics
    col1_s1.metric(
        label="Renewable Production:",
        value=f'{round(total_production/1000,2)} TWh',
        delta=f'{round(delta_production*100,2)} %'
    )


    col2_s1.metric(
        label="Energy Demand:",
        value=f'{round(total_demand,1)} TWh',
        delta=f'{round(delta_demand*100,2)} %'
    )

    col3_s1.metric(
        label="Population:",
        value=f'{round(population_total,1)} Millions'
    )


    st.divider()

    #Subsection 1
    sub_1 = st.container()
    sub_1.subheader(':grey[KPIs]')

    #Subsection layout subsection 1
    col1_sub1, col2_sub1 = sub_1.columns([1,2], gap='large')


    #Section 2
    sec_2 = st.container()
    sec_2.header('Overview', divider='gray')

    #Section layout section 2
    col1_s2, col2_s2 = sec_2.columns(2, gap='small')

    #Section 4
    sec_4 = st.container()

    #Section layout
    col1_s4, col2_s4 = sec_4.columns(2,gap='large')

    
if __name__ == '__main__':
    main()

