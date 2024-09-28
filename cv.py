import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title='VictorAnalyst',
    page_icon="🤖",
    layout='wide', )





# sidebar

top_sidebar_placeholder = st.sidebar.empty()
top_sidebar_placeholder.markdown('''
<p style="text-align: center;">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Victor-Analyst/refs/heads/main/bilder/portada.jpg?token=GHSAT0AAAAAACXPZG5MLQWWR4XXNVGV4HDUZXVVP2A" width="100%">
  <br>
</p>
''', unsafe_allow_html=True)
st.sidebar.title('Index')


page = st.sidebar.radio('', ['How Am I?', 'Machine Learning', 'Visualization','SQL','Python' ])
about_selection = ''
### PÁGINA  PRINCIPAL

with st.spinner('Creando un mundo mejor...'):
    if page == 'How Am I?':
        st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Victor-Analyst/refs/heads/main/bilder/jeg.jpeg?token=GHSAT0AAAAAACXPZG5NORLLY6HD74Z7A7IYZXVVNTA" width="30%" alt="Víctor Gutiérrez Data Analyst">
  <br>
</p>
''', unsafe_allow_html=True)
        st.subheader('How Am I?')
        st.markdown("####  👨‍🏫 I am a junior data analyst with more than ten years of experience in the field of teaching and culture. Now I am working on improving my knowledge in Machine Learning and advanced data visualization. If you´re wondering where I am, I´m probably taking a walk in the nearby mountains or participating in some cultural activity.")

        st.markdown('### Why did I create this?')
        st.markdown('#### I recently had a job interview and I had a bit of a hard time figuring out what my skills are or what projects I have created.')
        
        

### perfil


# Página 'Tu Perfil'
    elif page == 'Python':
        about_selection = st.sidebar.radio('', ['Night at the museum', 'King of the Pirates' ])
        if about_selection == 'Night at the museum':
             st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Victor-Analyst/refs/heads/main/bilder/museum.jpg?token=GHSAT0AAAAAACXPZG5M4IXSVPZVNKWGH6ZOZXVWW4A" width="30%" alt="Akkurat">
  <br>
</p>
''', unsafe_allow_html=True)
             st.markdown(
    "<h1 style='text-align: center;'>Night at the museum</h1>",
    unsafe_allow_html=True
)
             st.markdown("## Introduction")
             st.markdown('#### This project has its origins in the practices of a data analysis Bootcamp. It is inspired by the typical "create your own story" notebooks where the journey of the adventure is the adventure itself, with the outcome being unimportant.')
        
        elif about_selection == 'King of the Pirates':
            st.markdown("# King of the Pirates")
            st.markdown("## Introduction")




# Enlaces de mis perfiles

github_url = "https://github.com/Vicgutgam"
linkedin_url = "https://www.linkedin.com/in/v%C3%ADctor-guti%C3%A9rrez-gamero-81048b179/"


# Agregar el enlace en la barra lateral

st.sidebar.markdown(f"[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=social&logo=github)]({github_url})")  
        
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=social&logo=linkedin)]({linkedin_url})")