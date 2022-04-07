#Core Packages
from audioop import reverse
import imp
from secrets import choice
from tkinter import Menu
from unittest import result
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
def get_recommendation(title,cosine_sim_mat,num_of_rec=5):
    #indices of the course
    courses_indices=pd.Series(df,index,index=df['course_title']).drop_duplicates()
    #Index of the course
    idx=courses_indices[title]

    #Look into the cosine matrix for that index
    sim_scores=list(enumerate(cosine_sim_mat[idx]))
    sim_scores=sorted(sim_scores, key=lambda x: x[1],reverse=True)
    return sim_scores[1:]

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
        cosine_sim_mat=vectorize_text_to_cosine_mat(df['course_title'])
        search_term=st.text_input("Search")
        num_of_rec=st.sidebar.number_input("Namber",4,30,7)
        if st.button("Recommend"):
            if search_term is not None:
                try:
                    result=get_recommendation(search_term,cosine_sim_mat,df,num_of_rec)
                except Exception as e:
                    result="Not Found"
                   
                st.write(result)
    else:
        st.subheader("About")
        st.text("Built with Streamlit & Pandas")

if __name__=='__main__':
    main()