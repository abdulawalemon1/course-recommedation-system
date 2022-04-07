#Core Packages
import imp
from secrets import choice
from tkinter import Menu
import streamlit as st
import streamlit.components.v1 as stc


#Loading EDA
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel
#Load Dataset
def load_data(data):
    df=pd.read_csv(data)
    return df
#Fxn
#Vectorize +Cosine Similarity Matrix
def vectorize_text_to_cosine_mat(data):
    coun_vect=CountVectorizer()
    cv_mat= coun_vect.fit_transform(data)
    #Get Cosine
    cosine_sim_mat=cosine_similarity(cv_mat)
    return cosine_sim_mat


#Recommendation System
#Search For Course
def main():
    st.title("Course Recommendation App")
    menu=["Home","Recommend","About"]
    choice=st.sidebar.selectbox("Menu",menu)

    df=load_data("data/udemy_courses.csv")
    if choice=="Home":
        st.subheader("Home")
        st.dataframe(df.head(10))
    elif choice=="Recommend":
        st.subheader("Recommend Courses")
        search_term=st.text_input("Search")
        num_of_rec=st.sidebar.number_input("Namber",4,30,7)
        if st.button("Recommend"):
            if search_term is not None:
                pass
    else:
        st.subheader("About")
        st.text("Built with Streamlit & Pandas")

if __name__=='__main__':
    main()