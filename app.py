import streamlit as st
import pickle
import gzip
movies=pickle.load(open("movies_list.pkl",'rb'))

    
with gzip.open("similarity.pkl.gz4","rb") as f:
     similarity=pickle.load(f)

#similarity=pickle.load(open("similarity.pkl",'rb'))
movies_list=movies['title'].values


st.header("movie Recommend system")
value=st.selectbox("select movie from dropdown",movies_list)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    recommaned_movie=[]
    for i in distance[1:6]:
         recommaned_movie.append(movies.iloc[i[0]].title)
    return recommaned_movie



if st.button("show recommend"):
     movie_name=recommend(value)
     col1,col2,col3,col4,col5=st.columns(5)
     with col1:
          st.text(movie_name[0])
     with col2:
          st.text(movie_name[1])
     with col3:
          st.text(movie_name[2])
     with col4:
          st.text(movie_name[3])
     with col5:
          st.text(movie_name[4])    
    
    

