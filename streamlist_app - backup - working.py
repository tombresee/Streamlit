
# TOM BRESEE

# TRYING TO UNDERSTAND STREAMLIT


from altair.vegalite.v4.api import value
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import pandas as pd
import altair as alt
import os
import pandas as pd
import numpy as np

# cwd = os.getcwd()
# css_file = os.path.join(cwd, 'streamlit', 'style.css')


st.set_page_config(
    page_title='Tom Bresee - Initial Demo',
    # page_icon=SPR_SPOTIFY_URL,
    layout="wide",
    initial_sidebar_state="expanded",)

# local_css(css_file)


st.markdown("### My Application")

st.markdown("This application is a Streamlit dashboard hosted on Heroku that can be used"
            "to explore the results from board game matches that I tracked over the last year.")

st.markdown("**General Statistics **")

st.markdown("* This gives a general overview of the data including"
            "frequency of games over time, most games played in a day, and longest break"
            "between games.")


x = st.slider('Select a value')

st.write(x, 'squared is', x * x)


df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)



import streamlit as st
import pandas as pd

df = pd.read_csv("https://github.com/MaartenGr/boardgame/raw/master/files/boardgame_new.csv").head()
st.write(df)




