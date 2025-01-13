import streamlit as st
import sen_mail as sm

st.header("Contact me")
with st.form(key="form"):
    user_email=st.text_input("Your email")
    message=st.text_area("Your message")
    button=st.form_submit_button("Click me")
    msg=f"""\
Subject: New email from Your {user_email}
From: {user_email}
{message}
"""
    if button:
        sm.send_mail(msg)
        st.info("The mail was sent sucessfully")
        