import streamlit as st 
import sqlite3 as sq
conn = sq.connect("users.db")
c = conn.cursor()
c.execute("CREATE TABLE  if not exists users(username TEXT,password TEXT, mail TEXT)")

st.title("My Form")
with st.form("User Registration"):
    uname=st.text_input("Username")
    passw=st.text_input("Password")
    c_passw=st.text_input("Re-type Password")
    mail=st.text_input("Mail")
    # st.text_input("Age")
    but=st.form_submit_button("Submit")
    r_but = st.form_submit_button("red")
if r_but: 
    c.execute("SELECT * FROM users")
    data= c.fetchall()
    st.write(data)

if but: 
    if uname== "" and mail==""and passw=="" and passw==c_passw: 
        st.success("Register successfully" + " " + uname)
    else: 
        st.error("please check the form again")
        c.execute("INSERT INTO users VALUES (?,?,?)",(uname,passw,mail))
        conn.commit()