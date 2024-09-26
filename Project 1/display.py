#  streamlit run .\display.py --server.port 8888
import mysql.connector
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='project_1'
)

# Fetch data from the database
query = "SELECT order_date, product_id,	product_name, product_category,	customer_name	,customer_phone_number	,no_of_products_buy,	product_purchase_price,	product_sale_price,	profit_margin,	loss_margin	,year	,region,	country	,state	,city FROM project_1_table"
df = pd.read_sql(query, conn)
# Close the connection
conn.close()

st.set_page_config(page_title="Cash&Carry Store", page_icon=":clipboard:",layout="wide")

st.title(" :clipboard: Cash&Carry Store")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)


filtered_df = df
category_df = filtered_df.groupby(by = ["product_category"], as_index = False)["product_sale_price"].sum()
st.subheader("Category wise Sales")
fig = px.bar(category_df, x = "product_category", y = "product_sale_price", text = ['${:,.2f}'.format(x) for x in category_df["product_sale_price"]],
                template = "seaborn")
st.plotly_chart(fig,use_container_width=True, height = 200)



st.subheader("Region wise Sales")
fig = px.pie(filtered_df, values = "product_sale_price", names = "region", hole = 0.5)
fig.update_traces(text = filtered_df["region"], textposition = "outside")
st.plotly_chart(fig,use_container_width=True)


st.subheader("Country wise Sales")
fig = px.pie(filtered_df, values = "product_sale_price", names = "country", hole = 0.5)
fig.update_traces(text = filtered_df["country"], textposition = "outside")
st.plotly_chart(fig,use_container_width=True)



category_df = filtered_df.groupby(by = ["year"], as_index = False)["no_of_products_buy"].sum()
st.subheader("Product buy Yearly")
fig = px.bar(category_df, x = "year", y = "no_of_products_buy", text = ['${:,.2f}'.format(x) for x in category_df["no_of_products_buy"]],template = "seaborn" , color_discrete_sequence=["#28A745"] )
st.plotly_chart(fig,use_container_width=True, height = 200)



st.subheader("Hierarchical view of Sales of product using TreeMap")
fig3 = px.treemap(filtered_df, path = ["region","product_category","product_name"], values = "product_sale_price",hover_data = ["product_sale_price"],
                  color = "product_name")
fig3.update_layout(width = 800, height = 650)
st.plotly_chart(fig3, use_container_width=Tru


fig = px.line(
    df,
    x='year',
    y='product_category',
    labels={'product_c': 'Total Loss Margin'},
    title='Loss Margin Over Years',
    height=500,
    width=1000
)

# Display the chart in Streamlit
st.subheader('Loss Margin Per Year')
st.plotly_chart(fig, use_container_width=True)
