import streamlit
import pandas as p
import requests
# try:

fruit_choice = streamlit.text_input('What fruit would you like information about?') 
if not fruit_choice:
    streamlit.error('please select a fruit to get information.')
else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized=p.json.normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
