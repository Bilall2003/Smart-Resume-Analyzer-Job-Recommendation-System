import numpy as numpy
import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sns
import streamlit as st
import os
from urllib.parse import quote_plus

            
class Sidebar():
    
    st.markdown("""
            <style>
            #small_smartAi{
                font-size:25px;
                font-weight:bold;
                background: linear-gradient(to right, #2193b0, #6dd5ed);
                -webkit-background-clip: text;
                margin-top:70px;
                color: transparent;
                
            }
            
            .buttons{
                background:linear-gradient(to right, #2193b0, #6dd5ed);
                width:70px,
                color: white;
            }
             </style>       
        """,unsafe_allow_html=True)
    
    def side_bar(self):

        st.sidebar.markdown("""
        <style>
        @keyframes mergeBehindSync {
            0%, 100% { transform: translateX(30px); z-index: 1; }
            50% { transform: translateX(100px); z-index: 0; } /* left moves right behind center */
        }

        @keyframes mergeBehindSyncRight {
            0%, 100% { transform: translateX(-30px); z-index: 1; }
            50% { transform: translateX(-100px); z-index: 0; } /* right moves left behind center */
        }

        .animated-container {
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            gap: 10px;
            width: 100%;
        }

        .animated-container img.left {
            width: 120px;
            animation: mergeBehindSync 4s infinite ease-in-out;
        }

        .animated-container img.right {
            width: 120px;
            animation: mergeBehindSyncRight 4s infinite ease-in-out;
        }

        .animated-container img.center {
            width: 150px;
            position: relative;
            z-index: 2; /* always on top */
        }
        </style>

        <div class="animated-container">
            <img class="left" src="https://raw.githubusercontent.com/Bilall2003/Smart-Resume-Analyzer-Job-Recommendation-System/main/script/assets/cv%20(1).png">
            <img class="center" src="https://raw.githubusercontent.com/Bilall2003/Smart-Resume-Analyzer-Job-Recommendation-System/refs/heads/main/script/assets/cv.png">
            <img class="right" src="https://raw.githubusercontent.com/Bilall2003/Smart-Resume-Analyzer-Job-Recommendation-System/main/script/assets/cv.png">
        </div>
        """, unsafe_allow_html=True)




        st.sidebar.markdown("<h3 id ='small_smartAi'>Smart Resume AI</h3>",unsafe_allow_html=True)
        st.sidebar.divider()
        
        st.markdown("""
                <style>
                div.stButton > button:first-child {
                    background: linear-gradient(#2193b0, #6dd5ed);
                    width: 200px;       
                    height:60px;        
                    cursor: pointer;
                    border-radius: 10px;
                    display: flex;
                    justify-content: center;   /* center horizontally */
                    align-items: center;       /* center vertically */
                    text-align: center;
                    margin-left: 30px;
                    margin-top:10px;
                    color: white;
                    white-space: nowrap;
          
                }

                div.stButton > button:first-child:hover {
                    transform: scale(1.05);
                    opacity: 0.9;
                }
                </style>
            """, unsafe_allow_html=True)
        

class Pages(Sidebar):
    
    def all_pages(self):
    
        def home():
            but_sel1 = st.sidebar.button("🏠HOME",key="button1")
            if but_sel1:
                st.info("Welcome to Home Page")
        home()
        
        def analyzer():
            but_sel2 = st.sidebar.button("🔍RESUME ANALYZER",key="button2")
            if but_sel2:
                st.info("Welcome to analyzer Page")
        analyzer()
        
        def dashboard():
            but_sel3 = st.sidebar.button("📊DASHBOARD",key="button3")
            if but_sel3:
                st.info("Welcome to dashboard Page")
        dashboard()
        
        def feedback():
            but_sel4 = st.sidebar.button("💬FEED BACK",key="button4")
            if but_sel4:
                st.info("Welcome to feed Page")
        feedback()
        
        def about():
            but_sel5 = st.sidebar.button("ℹ️ ABOUT",key="button5")
            if but_sel5:
                st.info("Welcome to about Page")
        about()

        st.sidebar.divider()
        
        
obj=Pages()
obj.side_bar()
obj.all_pages()