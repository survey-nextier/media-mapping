import streamlit as  st
import pandas as pd


st.set_page_config(layout="wide")



"""
# UNICEF Media Mapping
##
"""


st.sidebar.header("Media Type")

media = st.sidebar.selectbox(
    'Select Media Type',
    ('Radio & TV', 'Daily, Weekly & Magazine', 'Online Magazine')
    
)

if media == "Radio & TV":
    st.subheader("Radio and TV")



    filename = "data/radio_tv.csv"
    df = pd.read_csv(filename, encoding="ISO-8859-1")
    df = df.drop(columns=['STATE','Percentage2', 'GENDER:', 'AGE GROUP OF LISTENERS:', 'MARITAL STATUS:', 'LITERACY LEVEL(EDUCATION):', 'AUDIENCE INCOME (PERSONAL):', 'RELIGION:', 'AUDIENCE OCCUPATION:', 'TIME:', 'SOCIAL CLASS:', 'Percentage_6' ])

    # left, right = st.columns(2)

    # with right:
        
    choiceMedia = st.sidebar.multiselect("Filter by Media Type", df['MEDIA TYPE'].unique(), default=df['MEDIA TYPE'].unique())
    
    df = df[df['MEDIA TYPE'].isin(choiceMedia)]

    # with left:
    choiceRegion = st.sidebar.multiselect("Filter by Region", df['REGION'].unique(), default=df['REGION'].unique())  
    df = df[df['REGION'].isin(choiceRegion)]

    df = df.sort_values(by="ESTIMATED AUDIENCE SIZE", ascending=False).reset_index(drop=True)
    df['ESTIMATED AUDIENCE SIZE'] = df['ESTIMATED AUDIENCE SIZE'].apply("{:,}".format)

    st.markdown("#")

elif media == "Daily, Weekly & Magazine":
    st.subheader("Daily, Weekly & Magazine")
    filename = "data/daily_mag.csv"
    df = pd.read_csv(filename, encoding="ISO-8859-1")
    # df = df.drop(columns=['STATE','Percentage2', 'GENDER:', 'AGE GROUP OF LISTENERS:', 'MARITAL STATUS:', 'LITERACY LEVEL(EDUCATION):', 'AUDIENCE INCOME (PERSONAL):', 'RELIGION:', 'AUDIENCE OCCUPATION:', 'TIME:', 'SOCIAL CLASS:', 'Percentage_6' ])

    choiceMedia = st.sidebar.multiselect("Filter by Media Type", df['MEDIA TYPE'].unique(), default=df['MEDIA TYPE'].unique())
    
    df = df[df['MEDIA TYPE'].isin(choiceMedia)]

    # choiceRegion = st.sidebar.multiselect("Filter by Region", df['REGION'].unique(), default=df['REGION'].unique())  
    # df = df[df['REGION'].isin(choiceRegion)]

    df = df.sort_values(by=" ESTIMATED AUDIENCE SIZE ", ascending=False).reset_index(drop=True)
    df[' ESTIMATED AUDIENCE SIZE '] = df[' ESTIMATED AUDIENCE SIZE '].apply("{:,}".format)
  

elif media == "Online Magazine":
    st.subheader("Online Magazine")
    filename = "data/online_mag.csv"
    df = pd.read_csv(filename, encoding="ISO-8859-1")
    # df = df.drop(columns=['STATE','Percentage2', 'GENDER:', 'AGE GROUP OF LISTENERS:', 'MARITAL STATUS:', 'LITERACY LEVEL(EDUCATION):', 'AUDIENCE INCOME (PERSONAL):', 'RELIGION:', 'AUDIENCE OCCUPATION:', 'TIME:', 'SOCIAL CLASS:', 'Percentage_6' ])

    # choiceMedia = st.sidebar.multiselect("Filter by Media Type", df['MEDIA TYPE'].unique(), default=df['MEDIA TYPE'].unique())
    
    # df = df[df['MEDIA TYPE'].isin(choiceMedia)]

    # choiceRegion = st.sidebar.multiselect("Filter by Region", df['REGION'].unique(), default=df['REGION'].unique())  
    # df = df[df['REGION'].isin(choiceRegion)]

    # df = df.sort_values(by=" ESTIMATED AUDIENCE SIZE ", ascending=False).reset_index(drop=True)
    # df[' ESTIMATED AUDIENCE SIZE '] = df[' ESTIMATED AUDIENCE SIZE '].apply("{:,}".format)
  

df.index = df.index + 1

df


st.markdown("##")


st.subheader("Cable Tv")


filename = "data/cable_tv.csv"

df = pd.read_csv(filename, encoding="ISO-8859-1")

df = df.sort_values(by=' ESTIMATED AUDIENCE SIZE ', ascending=False).reset_index(drop=True)
df[' ESTIMATED AUDIENCE SIZE '] = df[' ESTIMATED AUDIENCE SIZE '].apply("{:,}".format)


st.dataframe(df)




st.markdown("#")

st.subheader("Top Tv Programs")

filename = "data/tv_programs.csv"

df = pd.read_csv(filename)

df = df.sort_values(by=' ESTIMATED AUDIENCE SIZE ', ascending=False).reset_index(drop=True)
df[' ESTIMATED AUDIENCE SIZE '] = df[' ESTIMATED AUDIENCE SIZE '].apply("{:,}".format)
df = df.drop(columns=["MEDIA OUTLET"])


df.index = df.index + 1

df



st.markdown("#")

st.subheader("Top Cable Channels")

filename = "data/top_cable.csv"

df = pd.read_csv(filename, encoding="ISO-8859-1")

df = df.sort_values(by=' ESTIMATED AUDIENCE SIZE ', ascending=False).reset_index(drop=True)
df[' ESTIMATED AUDIENCE SIZE '] = df[' ESTIMATED AUDIENCE SIZE '].apply("{:,}".format)


df.index = df.index + 1
df

