import streamlit
import pandas
import requests
# streamlit.stop()
import snowflake.connector
from urllib.error import URLError

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?') 
if not fruit_choice:
    streamlit.error('please select a fruit to get information.')
else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized=pandas.json.normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()
# streamlit.write('The user entered ', first_choice)
# my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
