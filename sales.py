import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib as plt
import seaborn as sns


### Creating the Title page of Sales board 


st.title("RetailCo Sales Dashboard")
st.header("Overview")
st.subheader("Raw Transaction Data")

# (assume full_data was built/loaded above, same as previous classes)

full_data=pd.read_csv('full_data.csv')
st.dataframe(full_data.head())
st.dataframe(full_data.describe())




region_options = ["All"] + sorted(full_data["region"].unique().tolist())
selected_region = st.selectbox("Select a region:", region_options)


if selected_region != "All":
    filtered_data = full_data[full_data["region"] == selected_region]
else:
    filtered_data = full_data


st.write(f"Showing {len(filtered_data)} transactions")
st.dataframe(filtered_data)




category = st.multiselect("Category:", options=full_data["category"].unique(), default=full_data["category"].unique())





min_rev, max_rev = st.slider(
    "Revenue range ($):",
    min_value=(full_data["revenue"].min()),
    max_value=(full_data["revenue"].max()),
    value=(float(full_data["revenue"].min()), float(full_data["revenue"].max())),
)

col1, col2,col3,col4=st.columns(4)

with col1:
    st.metric("Max_Revenue",full_data['revenue'].max())


with col2:
    st.metric("Min_Revenue",full_data['revenue'].min())


with col3:
    st.metric("Total_Revenue",full_data['revenue'].sum())


with col4:
    st.metric("avg_Revenue",full_data['revenue'].mean().round(2))






date_range = st.date_input(
    "Order date range:",
    value=(full_data["order_date"].min(), full_data["order_date"].max()),
)



show_raw = st.checkbox("Show raw data table")



filtered = full_data[
    (full_data["category"].isin(category)) &
    (full_data["revenue"].between(min_rev, max_rev))
]

st.write(f"**{len(filtered)}** transactions match your filters")
if show_raw:
    st.dataframe(filtered)






st.sidebar.header("Filters")
selected_region = st.sidebar.selectbox("Region:", region_options)
selected_category = st.sidebar.multiselect("Category:", full_data["category"].unique(), default=full_data["category"].unique())





col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${filtered['revenue'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered['profit'].sum():,.0f}")
col3.metric("Orders", f"{len(filtered):,}")
col4.metric("Avg Order Value", f"${filtered['revenue'].mean():,.2f}")




tab1, tab2, tab3 = st.tabs(["Trends", "Regional Breakdown", "Product Detail"])

with tab1:
    st.subheader("Revenue by Region")
    
    import matplotlib.pyplot as plt
    import seaborn as sns

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=filtered, x="region", y="revenue", estimator="sum", errorbar=None, ax=ax)
    ax.set_title("Revenue by Region")
    st.pyplot(fig)



with tab2:
    st.subheader("Trends")
   
    import plotly.express as px

    fig = px.line(
    filtered.groupby("order_date", as_index=False)["revenue"].sum(),
    x="order_date", y="revenue", markers=True, title="Daily Revenue Trend",
    )
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Product-Level Detail")
   


region_revenue = (
    full_data.groupby("region", as_index=False)["profit"]
    .sum()
    .round(2)
)

st.dataframe(region_revenue)

        













































































































































































































































































































































































































































































































































