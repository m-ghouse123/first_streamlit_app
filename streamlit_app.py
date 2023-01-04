import streamlit
import pandas
import requests
import snowflake.connector
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response)
# streamlit.header("Fruityvice Fruit Advice!")
# streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
# streamlit.write('The user entered ', fruit_choice)
streamlit.dataframe(fruityvice_normalized)
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
