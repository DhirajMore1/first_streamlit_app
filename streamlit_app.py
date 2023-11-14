import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text("Grilled salmon with quinoa and steamed vegetables.")
streamlit.text("Mango avocado salad with grilled chicken and honey mustard dressing.")
streamlit.text("Chocolate chip pancakes topped with bananas and whipped cream.")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
