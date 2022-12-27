import streamlit
import pandas
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# streamlit.dataframe(my_fruit_list)
# Display the table on the page.
# my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# streamlit.dataframe(my_fruit_list)
# options = my_fruit_list['Fruit'].unique().tolist()
fruits_selected = streamlit.multiselect('Pick some fruits:',  list(my_fruit_list.index))
# fruits_selected = streamlit.multiselect('Pick some fruits:', my_fruit_list.set_index('Fruit'),['Avacado','Strawberries'])
# fruits_selected = st.sidebar.multiselect('Pick some fruits:',options,['Avacado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


