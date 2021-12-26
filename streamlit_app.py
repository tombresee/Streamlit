#---------------------------------------------------------------------------------------------------------


"""

Author:    Tom Bresee
Date:      Dec 25th, 2021
Layouts:   https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/
Status:    This is the latest streamlist app showing at:  https://share.streamlit.io/tombresee/streamlit/main

"""


#---------------------------------------------------------------------------------------------------------
import streamlit as st
from pathlib import Path
import base64
#---------------------------------------------------------------------------------------------------------
st.set_page_config(
     page_title='Streamlit Commands',
     layout="wide",
     initial_sidebar_state="expanded",)  # or initial sidebard doesn't have to be 
#---------------------------------------------------------------------------------------------------------
def main():
    cs_sidebar()      # so it is defined, but doesn't have to be used ! 
    cs_main_body()    
    return None
#---------------------------------------------------------------------------------------------------------
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
#---------------------------------------------------------------------------------------------------------
def cs_sidebar():
#     st.sidebar.header('Streamlit cheat sheet')
#     st.sidebar.markdown('''
#     <small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v1.0.0](https://www.streamlit.io/).</small>
#     ''', unsafe_allow_html=True)

#     st.sidebar.code('$ pip install streamlit')

#     st.sidebar.markdown('Import convention')

#     st.sidebar.markdown('__Add widgets to sidebar__')

#     st.sidebar.markdown('__Pre-release features__')

#     st.sidebar.markdown('[Beta and experimental features](https://docs.streamlit.io/en/stable/api.html#beta-and-experimental-features)')

#     st.sidebar.code('''
#     pip uninstall streamlit
#     pip install streamlit-nightly --upgrade
#     ''')

    st.sidebar.markdown('''<small>[st.cheat_sheet v1.0.0](https://github.com/daniellewisDL/streamlit-cheat-sheet)  | Oct 2021</small>''', unsafe_allow_html=True)

    return None  # i think you have to return something, but None is fine 
#---------------------------------------------------------------------------------------------------------
# TEMPORARY SIDEBAR WORK:
st.sidebar.header('Streamlit cheat sheet')
st.sidebar.markdown('Pre-release features')
st.sidebar.markdown('Author:  Tom Bresee')
# st.sidebar.error('This is an error')

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


#---------------------------------------------------------------------------------------------------------
def cs_main_body():
    # DEFINE 
    col1, col2 = st.columns(2)
    # col1, col2 = st.columns(2) is the generic form 
    # col1.image(original, use_column_width=True)
#---------------------------------------------------------------------------------------------------------
    # SECTION
    # starting 
    col1.subheader('Fundamentals')
    col1.code('''
    pip install streamlit
    import streamlit as st  # top of code 
    streamlit --help # command line
    streamlit --version
    streamlit run your_script.py
    streamlit config show
    streamlit cache clear
    streamlit docs
    ''')
#---------------------------------------------------------------------------------------------------------
    # SECTION
    col1.subheader('Display text')
    # or could do col1. header('Something')
    # i am writting everything into code snippets, nice clean format 
    col1.code('''
    # within container or section, enter:
    st.title('My title')
    st.header('My header')
    st.subheader('My subheader')
    st.text('My fixed width text')
    st.markdown('_Markdown_')  # markdown formatted text
    st.markdown('Streamlit is **_really_ cool**.') 
    st.caption('My image caption')
    st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
    st.write('anything') # words, dataframe, plots
    st.write(['st', 'is <', 3])
    st.code('for i in range(8): foo()')
    ''')
#---------------------------------------------------------------------------------------------------------
    # # SECTION
    col1.subheader('Display code snippets')
    col1.code('''
    def hello():
        print("Hello, Streamlit!"), language="python"''')
#---------------------------------------------------------------------------------------------------------
    # SECTION
    # Display data
    col1.subheader('Display data')
    col1.code('''
    st.dataframe(my_dataframe)
    st.table(data.iloc[0:10])
    st.json({'foo':'bar','fu':'ba'})
    st.metric(label="Temp", value="273 K", delta="1.2 K")
    ''')
#---------------------------------------------------------------------------------------------------------
    # SECTION
    # charts 
    col1.subheader('Visualize a chart')
    col1.code('''
    import pandas as pd
    import numpy as np
    import altair as alt
    df = pd.DataFrame(np.random.randn(200, 3),
                      columns=['a', 'b', 'c'])
    c = alt.Chart(df).mark_circle().encode(
                           x='a', 
                           y='b', 
                           size='c',
                           color='c',
                           tooltip=['a', 'b', 'c'])
    st.write(c)  # outputs chart''')
#---------------------------------------------------------------------------------------------------------
    # SECTION
    # Display charts
    col1.subheader('Display charts')
    col1.code('''
    st.line_chart(data)
    st.area_chart(data)
    st.bar_chart(data)
    st.pyplot(fig)
    st.altair_chart(data)
    st.vega_lite_chart(data)
    st.plotly_chart(data)
    st.bokeh_chart(data)
    st.pydeck_chart(data)
    st.deck_gl_chart(data)
    st.graphviz_chart(data)
    st.map(data)
    ''')
#---------------------------------------------------------------------------------------------------------
    # SECTION
    # Display media
    col1.subheader('Display media')
    col1.code('''
    st.image('./header.png')
    st.audio(data)
    st.video(data)
    ''')
#---------------------------------------------------------------------------------------------------------
    # SECTION
    # Display media
    col1.subheader('Status elements')
    col1.code('''
    st.error('This is an error')     # error (red) display message
    st.warning('This is a warning')  # warning (yellow) display message
    st.info('This is an informational message') # info (blue) display message
    st.success('This is a success message!')    # success (green) display message
    ''')
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
    # SECTION - but now on right hand side ! 
    # Display interactive widgets
    col2.subheader('Display interactive widgets')
    col2.code('''
    st.button('Hit me')
    st.download_button('On the dl', data)
    st.checkbox('Check me out')
    st.radio('Radio', [1,2,3])
    st.selectbox('Select', [1,2,3])
    st.multiselect('Multiselect', [1,2,3])
    st.slider('Slide me', min_value=0, max_value=10)
    st.select_slider('Slide to select', options=[1,'2'])
    st.text_input('Enter some text')
    st.number_input('Enter a number')
    st.text_area('Area for textual entry')
    st.date_input('Date input')
    st.time_input('Time entry')
    st.file_uploader('File uploader')
    st.color_picker('Pick a color')
    ''')
    col2.write('Use widgets\' returned values in variables:')
    col2.code('''
    >>> for i in range(int(st.number_input('Num:'))): foo()
    >>> if st.sidebar.selectbox('I:',['f']) == 'f': b()
    >>> my_slider_val = st.slider('Quinn Mallory', 1, 88)
    >>> st.write(slider_val)
    ''')
#---------------------------------------------------------------------------------------------------------
    # SECTION
    # Control flow
    col2.subheader('Control flow')
    col2.code('''
    st.stop()
    ''')
#---------------------------------------------------------------------------------------------------------
    # SECTION
    # Lay out your app
    col2.subheader('Lay out your app')
    col2.code('''
    st.form('my_form_identifier')
    st.form_submit_button('Submit to me')
    st.container()
    st.columns(spec)
    >>> col1, col2 = st.columns(2)
    >>> col1.subheader('Columnisation')
    st.expander('Expander')
    >>> with st.expander('Expand'):
    >>>     st.write('Juicy deets')
    ''')

    col2.write('Batch widgets together in a form:')
    col2.code('''
    >>> with st.form(key='my_form'):
    >>> 	text_input = st.text_input(label='Enter some text')
    >>> 	submit_button = st.form_submit_button(label='Submit')
    ''')
#---------------------------------------------------------------------------------------------------------
    # SECTION
    # Display code
    col2.subheader('Display code')
    col2.code('''
    st.echo()
    >>> with st.echo():
    >>>     st.write('Code will be executed and printed')
    ''')
#---------------------------------------------------------------------------------------------------------
    # SECTION
    # Display progress and status
    col2.subheader('Other key parts of the API')
    col2.markdown('''
    <small>[State API](https://docs.streamlit.io/en/stable/session_state_api.html)</small><br>
    <small>[Theme option reference](https://docs.streamlit.io/en/stable/theme_options.html)</small><br>
    <small>[Components API reference](https://docs.streamlit.io/en/stable/develop_streamlit_components.html)</small><br>
    <small>[API cheat sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)</small><br>
    ''', unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------
    return None
#---------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
#---------------------------------------------------------------------------------------------------------
















#---------------------------------------------------------------------------------------------------------
# APPENDIX: 
#---------------------------------------------------------------------------------------------------------
# COLUMNS

# col1, col2 = st.columns(2)

# original = Image.open(image)
# col1.header("Original")
# col1.image(original, use_column_width=True)

# grayscale = original.convert('LA')
# col2.header("Grayscale")
# col2.image(grayscale, use_column_width=True)
#---------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------


