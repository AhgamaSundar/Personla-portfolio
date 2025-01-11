import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.image("images/photo.jpg")
with col2:
    st.title("Ahgama Sundar")
    content="""I'm Ahgama Sundar,I’m a tech enthusiast with a strong foundation in Linux systems and web development. I thrive on solving problems, optimizing workflows, and building practical, user-centric applications. With  a passion for exploring tools like R for data analysis, I’m always looking to deepen my knowledge and contribute to impactful solutions. 
    Let’s connect to collaborate and share ideas!
"""
    st.info(content)
infos="Below are the links to some of the apps I've built and the ways to contact me "
st.write(infos)

col3,col4=st.columns(2)
df=pd.read_csv('data.csv',sep=";")
with col3:
    for i,n in df[:int(len(df)/2)].iterrows():
        st.header(n['title'])
        st.write(n["description"])
        st.image("images/"+n["image"])
        st.write(f"[Source]({n["url"]})")

with col4:
    for i,n in df[int(len(df)/2):].iterrows():
        st.header(n['title'])
        st.write(n["description"])
        st.image("images/"+n["image"])
        st.write(f"[Source]({n["url"]})")