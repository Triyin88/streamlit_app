import streamlit as st # streamlit package
import numpy as np
import pandas as pd
from millify import millify # shortens values (10_000 ---> 10k)
from streamlit_extras.metric_cards import style_metric_cards # beautify metric card with css
import plotly.graph_objects as go
import altair as alt 
import plotly.express as px

st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Amasis MT Pro Black';
        src: url('https://path-to-your-font/AmasisMTPro-Black.ttf');  /* Ensure you provide the correct URL to the font file */
    }
    .custom-text {
        font-family: 'Amasis MT Pro Black', sans-serif;
        font-size: 60px;
        font-weight: bold;
        color: black;pip install streamlit numpy pandas streamlit_extras millify altair plotly
    }
    </style>
    <div class="custom-text">
      E-Commerce Fraud Detection
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.success("Data Dashboard")
if hasattr(st.session_state, 'df'):
    df = st.session_state.df

    dash_1 = st.container()

    with dash_1:
    # get metrics
        total_fraud = len(df[df.Prediction=='fraud'])
        per_fraud = round((total_fraud/len(df))*100, 2)
        total_value = round(df[df['Prediction'] == 'fraud']['Transaction Amount'].sum(),2)
        
        col1, col2, col3 = st.columns(3)
        # create column span
        col1.metric(label="Total Fraudulent Transactions", value= total_fraud)
        col2.metric(label="Percentage of Fraudulent Transactions", value=f"{per_fraud}%", delta="")
        col3.metric(label="Defrauded Amount", value=f"${total_value:,}", delta="")
    
        # this is used to style the metric card
        style_metric_cards(border_left_color="red")

    
    col1, col2, col3 = st.columns(3)
    with col1:
        fraud_counts = df['Prediction'].value_counts().reset_index()
        fraud_counts.columns = ['Transaction Type', 'Count']
       # Custom colors for the pie chart
        custom_colors = ['#77DD77','#FF6961']
        
    
        fig = px.pie(fraud_counts, values='Count', names='Transaction Type', 
                 title='Percentage of Fraudulent and Non-Fraudulent Transactions',
                 labels={'Transaction Type': 'Transaction Type', 'Count': 'Count'},
                 hole=0.4,  # To create a donut chart
                 color_discrete_sequence=custom_colors)
        fig.update_layout(height=550, width=550)
        st.plotly_chart(fig)


    with col2:
        fraud_df = df[df['Prediction'] == 'fraud']
        fraud_by_hour = fraud_df['Transaction Hour'].value_counts().reset_index()
        fraud_by_hour.columns = ['Transaction Hour', 'Fraud Count']
        fraud_by_hour = fraud_by_hour.sort_values(by='Transaction Hour')
        fig = px.bar(fraud_by_hour, x='Transaction Hour', y='Fraud Count', 
                title='Fraud Count by Transaction Hour', height=600, width=500, color_discrete_sequence=['deepskyblue'])
        st.plotly_chart(fig)

    with col3:
        fig = px.scatter(df, x='Transaction Amount', y='Account Age Days', color='Prediction',
                     title='Scatter Plot of Transaction Amount vs. Account Age Days', height=600, width=600,
                     labels={'Transaction Amount': 'Transaction Amount', 'Account Age Days': 'Account Age Days'},
                     category_orders={'Prediction': ['non-fraud', 'fraud']},
                     color_discrete_map={'non-fraud': 'darkgreen', 'fraud': 'lightsalmon'})
        fig.update_layout(legend=dict(x=1, y=1))
        st.plotly_chart(fig)

    st.write("DataFrame from Fraud Detection:")
    st.write(df)
else:
    st.warning("No DataFrame found. Please go to Fraud Detection page to upload a CSV file.")
    dash_2 = st.container()
    with dash_2:
        col1, col2, col3 = st.columns(3)
        # create column span
        col1.metric(label="Total Fraudulent Transactions", value= 0)
        col2.metric(label="Percentage of Fraudulent Transactions", value=f"{0}%", delta="")
        col3.metric(label="Defrauded Amount", value=f"${0:,}", delta="")
    
        # this is used to style the metric card
        style_metric_cards(border_left_color="red")

        

