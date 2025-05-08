# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(f"Smoothie")
st.write(
  """Smoothie"""
)

session = get_active_session()

name_on_order = st.text_input("Name on Smoothie:")

my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))

ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    my_dataframe,
    max_selections = 5
)

ingredients_string = ' '.join(ingredients_list)

# st.write(ingredients_string)

my_insert_stmt = """ insert into smoothies.public.orders (name_on_order, ingredients)
            values ('""" + name_on_order + """','""" + ingredients_string + """')"""

# st.write(my_insert_stmt)
# st.stop()

if ingredients_string:

    time_to_insert = st.button("Submit Order")

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
        
