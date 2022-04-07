#Core Packages
from secrets import choice
from tkinter import Menu
import streamlit as st
import streamlit.components.v1 as stc


#Loading EDA
import pandas as pd


def main():
    st.title("Course Recommendation App")
    menu=["Home","Recommend","About"]
    choice=st.sidebar.selectbox("Menu",menu)

    if choice=="Home":
        st.subheader("Home")
    elif choice=="Recommend":
        st.subheader("Recommend Courses")
    else:
        st.subheader("About")
        st.text("Built with Streamlit & Pandas")

if __name__=='__main__':
    main()