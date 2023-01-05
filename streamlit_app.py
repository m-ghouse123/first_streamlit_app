import streamlit
import pandas as pa
import requests
# streamlit.stop()
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Mom''s New Healthy Dinner')
streamlit.header('Breakfast Menu')
# 🥣 🥗 🐔 🥑🍞
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacodo Toast')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")
# streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pa.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.write('The user entered ', fruit_choice)
streamlit.dataframe(fruityvice_normalized)
my_fruit_list = pa.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include
my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple','Banana','Grapefruit'])
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple','Banana','Grapefruit'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
# my_data_row = my_cur.fetchone()
my_data_row = my_cur.fetchall()
# streamlit.text("The fruit list contain:")
streamlit.header("The fruit list contain:")
# streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)
# try:
#    fruit_choice = streamlit.text_input('What fruit would you like information about?') 
if not fruit_choice:
    streamlit.error('please select a fruit to get information.')
else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized=pa.json.normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
# except URLError as e:
#    streamlit.error()
# streamlit.write('The user entered ', first_choice)
# my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")

