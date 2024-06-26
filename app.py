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


    #Section layout section 1
    col1_s1, col2_s1, col3_s1 = sec_1.columns(3, gap='large')

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
