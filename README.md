# RenewablesPrediction-

The main objective of this project is to create a dashboard to analyze the data from several sources and develop a common place for these insights. This is a part of a bigger project, so check more about the first part.

## Medium Article

Check the part 1 here:
<a href='https://medium.com/@forceliuss/renewable-insight-eda-with-streamlit-006a4a0c7b6c' target='_blank'>Renewable Insights — EDA with Streamlit</a>

## Datasets

- Renewable Energy Production by Country (2000 - 2021)
  <a href='https://pxweb.irena.org/pxweb/en/IRENASTAT/IRENASTAT__Power%20Capacity%20and%20Generation/REGEN_2023_cycle2.px/' target='_blank'>IRENA</a>

- Investment in Renewable by Source (1960 - 2022)
  <a href='https://ourworldindata.org/grapher/investment-in-renewable-energy-by-technology?facet=none' target='_blank'>Our World in Data</a>

* Renewable Energy (1960 - 2023) - main source (https://www.oecd-ilibrary.org/energy/renewable-energy/indicator/english_aac7c3f1-en)
  <a href='https://www.kaggle.com/datasets/imtkaggleteam/renewable-energy-1960-2023' target='_blank'>Kaggle dataset</a>

* World GDP by Country (1960 - 2022)
  <a href='https://www.kaggle.com/datasets/sazidthe1/world-gdp-data' target='_blank'>Kaggle dataset</a>

## Code focus objectives

- Import and clear the data from the datasets
- Combine all the different sources into a main dataframe
- Analyze the dataframe and create metrics
- Create a local dashboard (StreamLit)
- Sort the global datasets by countries

## Libraries

- Pandas
- StreamLit
- Seaborn
- MathplotLib
- Plotly Express

## How to run

1. Clone this project
   `git clone https://github.com/forceliuss/RenewablesPrediction.git`
2. Run your python kernel
3. Install all the libraries above
   `pip install -r requirements.txt`
4. Run `app.py` through the streamlit command
   `streamlit run app.py`
