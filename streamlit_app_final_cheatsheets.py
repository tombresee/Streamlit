"""
Tom Bresee
"""


#---------------------------------------------------------------------------------------------------------
import streamlit as st
from pathlib import Path
import base64
#---------------------------------------------------------------------------------------------------------
st.set_page_config(
     page_title='Reinforcement Learning Cheat Sheet',
     layout="wide",
     initial_sidebar_state="expanded",)
#---------------------------------------------------------------------------------------------------------
def main():
    cs_sidebar()
    cs_body()

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
# <small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v1.0.0](https://www.streamlit.io/).</small>
#     ''', unsafe_allow_html=True)

#     st.sidebar.markdown('__How to install and import__')

#     st.sidebar.code('$ pip install streamlit')

#     st.sidebar.markdown('Import convention')

#     st.sidebar.markdown('__Add widgets to sidebar__')

#     st.sidebar.markdown('__Command line__')


#     st.sidebar.code('''
#     $ streamlit --help
#     $ streamlit run your_script.py
#     $ streamlit hello
#     $ streamlit config show
#     $ streamlit cache clear
#     $ streamlit docs α β
#     $ streamlit --version
#     ''')

#     st.sidebar.markdown('__Pre-release features__')

#     st.sidebar.markdown('[Beta and experimental features](https://docs.streamlit.io/en/stable/api.html#beta-and-experimental-features)')

#     st.sidebar.code('''
# pip uninstall streamlit
# pip install streamlit-nightly --upgrade
#     ''')


#     st.sidebar.markdown('''<small>[st.cheat_sheet v1.0.0](https://github.com/daniellewisDL/streamlit-cheat-sheet)  | Oct 2021</small>''', unsafe_allow_html=True)

    return None  # i think you have to return something, but None is fine 
#---------------------------------------------------------------------------------------------------------
def cs_body():

    col1, col2 = st.columns(2)

    col1.subheader('Magic commands')

    col1.code('''# Magic commands implicitly `st.write()`
\'\'\' _This_ is some __Markdown__ \'\'\'
a=3
'dataframe:', data
    ''')



    # Display text

    col1.subheader('Display text')
    col1.code('''
st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.caption('Balloons. Hundreds of them...')
st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
* optional kwarg unsafe_allow_html = True
    ''')

    # Display data

    col1.subheader('Display data')
    col1.code('''
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")
    ''')

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

    # Display media

    col1.subheader('Display media')
    col1.code('''
st.image('./header.png')
st.audio(data)
st.video(data)
    ''')

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

    # Control flow

    col2.subheader('Control flow')
    col2.code('''
st.stop()
    ''')

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

    # Display code

    col2.subheader('Display code')
    col2.code('''
st.echo()
>>> with st.echo():
>>>     st.write('Code will be executed and printed')
    ''')

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




if __name__ == '__main__':
    main()