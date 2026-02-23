import pandas as pd
import streamlit as st
import geopandas as gpd

class DataDownloader:
    def __init__(self):
        self.STORAGE_OPTIONS = {'User-Agent': 'Our World In Data data fetch/1.0'}

        self.df_annual_change = pd.read_csv("https://ourworldindata.org/grapher/annual-change-forest-area.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = self.STORAGE_OPTIONS)
        self. df_annual_defo = pd.read_csv("https://ourworldindata.org/grapher/annual-deforestation.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = self.STORAGE_OPTIONS)
        self.df_share_protected = pd.read_csv("https://ourworldindata.org/grapher/terrestrial-protected-areas.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = self.STORAGE_OPTIONS)
        self.df_share_degraded = pd.read_csv("https://ourworldindata.org/grapher/share-degraded-land.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = self.STORAGE_OPTIONS)
        self.df_fifth = 5
        self.df_world = gpd.read_file("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip")
        self.datasets = {
            "Annual Change In Forest Area": self.df_annual_change,
            "Annual Deforestation": self.df_annual_defo,
            "Share Of Protected Land": self.df_share_protected,
            "Share Of Degraded Land": self.df_share_degraded,
            #"fifth_dataset": "PUT_YOUR_DF_HERE"  # replace with the fifth dataset
        }
        self.move_to_downloads()

    def move_to_downloads(self):
        for dataset_name,dataset_file in zip(self.datasets.keys(),self.datasets.values()):
            dataset_file.to_csv(f'downloads/{dataset_name}.csv')
        self.df_world.to_csv(f'downloads/world.csv')

objectobj = DataDownloader()

"""this is a docstring!"""

st.title('Test Title this tests the title')
selbox_text = st.selectbox(options  = objectobj.datasets.keys(), label = 'a select box?')
df_displayed = objectobj.datasets[selbox_text]
target_year = st.select_slider(options=range(df_displayed.year.min(),df_displayed.year.max()), label = 'year')
st.text(f'This graph shows {selbox_text} in the year {target_year}')

df_displayed = df_displayed[df_displayed.year == target_year].groupby('entity')[df_displayed.columns[-1]].mean()
st.bar_chart(df_displayed)
st.text(f'the select box says: {selbox_text}')

