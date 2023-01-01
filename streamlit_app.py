import streamlit
import pandas
import requests
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response)
# streamlit.header("Fruityvice Fruit Advice!")
# streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
# streamlit.write('The user entered ', fruit_choice)
# streamlit.dataframe(fruityvice_normalized)
