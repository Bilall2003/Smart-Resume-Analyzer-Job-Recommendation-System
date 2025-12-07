import numpy as numpy
import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sns
import streamlit as st
import os
from urllib.parse import quote_plus

            
class Sidebar:
    
    st.markdown("""
            <style>
            .sidebar .small_smartAi,
            .small_smartAi {
                font-size: 70px ;
                font-weight: bold !important;
                margin-top: 70px !important;
                text-align:left;

                background: linear-gradient(to right, #2193b0, #6dd5ed);
                -webkit-background-clip: text;
                background-clip: text;

                -webkit-text-fill-color: transparent;
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
            0%, 100% { transform: translateX(30px); z-index: 1; } /*z-index to put image backside*/
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




        st.sidebar.markdown("<h1 class ='small_smartAi'>Smart Resume AI</h1>",unsafe_allow_html=True)
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
                    background:linear-gradient(to right, #2193b0);
                }
                </style>
            """, unsafe_allow_html=True)
        

class Pages(Sidebar):
    
    def all_pages(self):
    
        def home():
            but_sel1 = st.sidebar.button("🏠HOME",key="button1")
            if but_sel1:
                st.markdown("""
                    <style>

                    .green-box {
                        background: linear-gradient(45deg, rgba(0, 180, 219, 0.7) 100%, rgba(0, 131, 176, 0.05) 100%);          
                        padding: 20px;
                        border-radius: 12px;
                        color: white;
                        max-width: 800px;
                        margin-top: 15px;
                        display:flex;
                        justify-content:flex-start;
                        
                    }
                    
                    .green-box h2 {
                        font-size: 2.5rem;
                        font-weight: bold;
                        margin-bottom: 10px;
                    }

                    .green-box p {
                        font-size: 1.2rem;
                        line-height: 1.5;
                    }
                    </style>

                    <div class="green-box">
                        <h2>Smart Resume AI</h2>
                        <p>
                            Transform your career with AI-powered resume analysis and building.<br>
                            Get personalized insights and create professional resumes that stand out.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("""
                        <style>
                        .sec-box {
                        background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);          
                            padding: 20px;
                            border-radius: 12px;
                            color: white;
                            max-width: 800px;
                            margin-top: 70px;
                            position: relative;
                        }

                        /* Animation */
                        @keyframes Syncimg {
                            0%, 100% { transform: translateX(50px); z-index: 1; }
                            50% { transform: translateX(-50px); z-index: -1; }
                        }

                        .secmoveright {
                            width: 40px;
                            position: relative;
                            animation: Syncimg 2s infinite ease-in-out;
                        }

                        .sec-box h2 {
                            font-size: 2.5rem;
                            font-weight: bold;
                            margin-bottom: 10px;
                        }

                        .sec-box p {
                            font-size: 1.2rem;
                            line-height: 1.5;
                        }

                        .sec-box:hover {
                            cursor: pointer;
                            transform: scale(1.02);
                            transition: 0.1s;
                            color: grey;
                        }
                        </style>

                        <div class="sec-box">
                            <img class="secmoveright" src="https://raw.githubusercontent.com/Bilall2003/Smart-Resume-Analyzer-Job-Recommendation-System/main/script/assets/cv%20(1).png">
                            <h2>AI-Powered Analysis</h2>
                            <p>
                                Get instant feedback on your resume with advanced AI analysis that identifies strengths and areas for improvement.
                            </p>
                        </div>
                        """, unsafe_allow_html=True)

                st.markdown("""
                    <style>
                    .thrd-box {
                       background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);           
                        padding: 20px;
                        border-radius: 12px;
                        color: white;
                        max-width: 800px;
                        margin-top: 35px;
                    }
                     /* Animation */
                    @keyframes Syncimg {
                        0%, 100% { transform: translateX(50px); z-index: 1; }
                        50% { transform: translateX(-50px); z-index: -1; }
                    }

                    .thrdmoveright {
                        width: 40px;
                        position: relative;
                        animation: Syncimg 2s infinite ease-in-out;
                    }

                    .thrd-box h2 {
                        font-size: 2.5rem;
                        font-weight: bold;
                        margin-bottom: 10px;
                    }

                    .thrd-box p {
                        font-size: 1.2rem;
                        line-height: 1.5;
                    }
                    
                    .thrd-box:hover {
                        cursor: pointer;
                        transform: scale(1.02);
                        transition: 0.1s;
                        color:grey;
                    }
                    </style>

                    <div class="thrd-box">
                        <img class="thrdmoveright" src="https://raw.githubusercontent.com/Bilall2003/Smart-Resume-Analyzer-Job-Recommendation-System/main/script/assets/cv%20(1).png">
                        <h2>Dashboard Exploration</h2>
                        <p>
                             visual interfaces that aggregate key performance indicators and metrics from various data sources into a single, easy-to-digest format.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown("""
                    <style>
                    .forth-box {
                        background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);          
                        padding: 20px;
                        border-radius: 12px;
                        color: white;
                        max-width: 800px;
                        margin-top: 35px;
                    }
                    
                     /* Animation */
                    @keyframes Syncimg {
                        0%, 100% { transform: translateX(50px); z-index: 1; }
                        50% { transform: translateX(-50px); z-index: -1; }
                    }

                    .forthmoveright {
                        width: 40px;
                        position: relative;
                        animation: Syncimg 2s infinite ease-in-out;
                    }

                    .forth-box h2 {
                        font-size: 2.5rem;
                        font-weight: bold;
                        margin-bottom: 10px;
                    }

                    .forth-box p {
                        font-size: 1.2rem;
                        line-height: 1.5;
                    }
                    .forth-box:hover {
                        cursor: pointer;
                        transform: scale(1.02);
                        transition: 0.1s;
                        color:grey;
                    }
                    
                    </style>
                    <div class="forth-box">
                        <img class="forthmoveright" src="https://raw.githubusercontent.com/Bilall2003/Smart-Resume-Analyzer-Job-Recommendation-System/main/script/assets/cv%20(1).png">
                        <h2>Career Insights</h2>
                        <p>
                            Access detailed analytics and personalized recommendations to enhance your career prospects.
                        </p>
                    </div>
                    
                    """, unsafe_allow_html=True)
                

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