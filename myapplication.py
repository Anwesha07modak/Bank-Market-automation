import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 


# read csv from a github repo
df = pd.read_csv("bank.csv")


st.set_page_config(
    page_title = 'Bank Marketing Dashboad- Real time',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Live/Bank Marketing Dashboard")

# top-level filters 

job_filter = st.selectbox("Select the Job", pd.unique(df['job']))

education_filter = st.selectbox("Select the education type", pd.unique(df['education']))

# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

df = df[df['job']==job_filter]
df = df[df["education"]==education_filter]

# near real-time / live feed simulation 

for seconds in range(200):
#while True: 
    
    df['age_new'] = df['age'] * np.random.choice(range(1,5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

    # creating KPIs 
    avg_age = np.mean(df['age_new']) 

    count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
    
    balance = np.mean(df['balance_new'])

    count_education = int(df[(df["education"]=='tertiary')]['education'].count() + np.random.choice(range(1,30)))

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="Age ⏳", value=round(avg_age), delta= round(avg_age) - 10)
        kpi2.metric(label="Married Count 💍", value= int(count_married), delta= - 10 + count_married)
        kpi3.metric(label="A/C Balance ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)
        kpi2.metric(label="Education Count 🎓", value= int(count_education), delta= - 10 + count_education)

        # create two columns for charts 

        fig_col1, fig_col2, fig_col3 = st.columns(3)
        with fig_col1:
            st.markdown("### First Chart")
            fig1 = px.density_heatmap(data_frame=df, y='age_new', x='marital')
            st.write(fig1)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x='age_new')
            st.write(fig2)
        with fig_col3:
            st.markdown("### Third Chart")
            fig3 = px.bar(data_frame=df, x='age_new', y='balance_new')
            st.write(fig3)

        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)