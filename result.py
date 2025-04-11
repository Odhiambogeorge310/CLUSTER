#import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
#...............................................................................................................................

#Setting page
st.set_page_config(page_title="Cluster_Dashboard", page_icon=":school:", layout="wide")
#main page title
st.title("🎓CLUSTER_DASHBOARD📊")
st.markdown('<style>h1{padding-top:2rem;}</style>', unsafe_allow_html=True)

#................................................................................................................................
#invoking the css function
# load CSS Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
#.................................................................................................................................
#loading data_set
@st.cache_data
def get_data():
    data=pd.read_excel('results.xlsx')
    return data
#accessing data by calling the function
data=get_data()

#....................................................................................................................................
#Navigation sidebar
st.subheader("COUNT_SUMMARY:")
st.sidebar.subheader('Filter_Here:')
gender=  st.sidebar.radio("Select_Gender:", options=data['GENDER'].unique())
grade=   st.sidebar.multiselect("Select_Grade:", options=data['GRADE'].unique(), default=data['GRADE'].unique())
#....................................................................................................................................

#Querying the dataset
df_selected=data.query('GENDER==@gender & GRADE==@grade')
#.....................................................................................................................................
def metrics():
    from streamlit_extras.metric_cards import style_metric_cards
    left_column,middle_column,right_column=st.columns(3)
    left_column.metric("🧍_🧍‍♀️All_Learners:",value=data.ID.count(), delta='All_Learnes')
    middle_column.metric("🧍‍♀️Boys_Count:",value=df_selected.loc[df_selected['GENDER']=='Boy'].count()[0], delta='Boys_Count')
    right_column.metric("🧍Girls_Count:",value=df_selected.loc[df_selected['GENDER']=='Girl'].count()[0], delta='Girls_Count')
    style_metric_cards(background_color="#121270",border_left_color="#c750a3",box_shadow="3px")
#.....................................................................................................................................
st.divider()
metrics()
st.divider()
st.subheader("📊 ASSESSMENT_RUBRICS_VISUALIZATION:")

#.....................................................................................................................................
#Sidebar for Grades
grades=   st.sidebar.multiselect("Pick_Grade:", options=data['GRADE'].unique(), default=data['GRADE'].unique())
#.....................................................................................................................................


#.....................................................................................................................................
#Querying the grades
df_selected=data.query('GRADE==@grades')
#.....................................................................................................................................


#.....................................................................................................................................
#Visualizing
div1, div2,div3,div4=st.columns(4)

#math
def bar_math():
    theme_plotly = None  # None or streamlit
    
    with div1:  # Assuming div1 is a valid Streamlit container or section in your code
        # Create the bar plot using Plotly Express
        fig = px.bar(df_selected, 
                     y='MATHS',  # The column for Y-axis
                     x='MATHS',  # The column for X-axis
                     text_auto='.2s',     # Automatically display text on the bars
                     title="MATHS DISTRIBUTION SCORES")
        
        # Replace x-axis numeric values (1, 2, 3, 4) with custom labels
        custom_labels = {
            1: "B.E",
            2: "A.E",
            3: "M.E",
            4: "E.E"
        }
        
        # Update x-axis with custom labels
        fig.update_layout(
            xaxis=dict(
                tickmode='array',  # Set to 'array' for custom ticks
                tickvals=[1, 2, 3, 4],  # X-axis values that need to be replaced
                ticktext=[custom_labels[1], custom_labels[2], custom_labels[3], custom_labels[4]]  # Corresponding custom labels
            )
        )
        
        # Customize text appearance for the bars
        fig.update_traces(
            textfont_size=18,  # Font size for the text
            textangle=0,       # Angle of the text on the bars
            textposition="outside",  # Position the text outside the bars
            cliponaxis=False,   # Prevent clipping of text
             marker=dict(color='#fcba03')
        )
        
        # Display the plot in the Streamlit app
        st.plotly_chart(fig, use_container_width=True, theme="streamlit")

#....................................................................................................................................................................................
#bar chart
def bar_eng():
    theme_plotly = None  # None or streamlit
    
    with div2:  # Assuming div1 is a valid Streamlit container or section in your code
        # Create the bar plot using Plotly Express
        fig = px.bar(df_selected, 
                     y='ENGLISH',  # The column for Y-axis
                     x='ENGLISH',  # The column for X-axis
                     text_auto='.2s',     # Automatically display text on the bars
                     title="ENGLISH DISTRIBUTION SCORES")
        
        # Replace x-axis numeric values (1, 2, 3, 4) with custom labels
        custom_labels = {
            1: "B.E",
            2: "A.E",
            3: "M.E",
            4: "E.E"
        }
        
        # Update x-axis with custom labels
        fig.update_layout(
            xaxis=dict(
                tickmode='array',  # Set to 'array' for custom ticks
                tickvals=[1, 2, 3, 4],  # X-axis values that need to be replaced
                ticktext=[custom_labels[1], custom_labels[2], custom_labels[3], custom_labels[4]]  # Corresponding custom labels
            )
        )
        
        # Customize text appearance for the bars
        fig.update_traces(
            textfont_size=18,  # Font size for the text
            textangle=0,       # Angle of the text on the bars
            textposition="outside",  # Position the text outside the bars
            cliponaxis=False,  # Prevent clipping of text
            marker=dict(color='#03fc13')
        )
        
        # Display the plot in the Streamlit app
        st.plotly_chart(fig, use_container_width=True, theme="streamlit")

#kiswahili
def bar_kisw():
    theme_plotly = None  # None or streamlit
    
    with div3:  # Assuming div1 is a valid Streamlit container or section in your code
        # Create the bar plot using Plotly Express
        
        fig = px.bar(df_selected, 
                     y='KISWAHILI',  # The column for Y-axis
                     x='KISWAHILI',  # The column for X-axis
                     text_auto='.2s',     # Automatically display text on the bars
                     title="KISWAHILI DISTRIBUTION  SCORES")
        
        # Replace x-axis numeric values (1, 2, 3, 4) with custom labels
        custom_labels = {
            1: "B.E",
            2: "A.E",
            3: "M.E",
            4: "E.E"
        }
        
        # Update x-axis with custom labels
        fig.update_layout(
            xaxis=dict(
                tickmode='array',  # Set to 'array' for custom ticks
                tickvals=[1, 2, 3, 4],  # X-axis values that need to be replaced
                ticktext=[custom_labels[1], custom_labels[2], custom_labels[3], custom_labels[4]]  # Corresponding custom labels
            )
        )
        
        # Customize text appearance for the bars
        fig.update_traces(
            textfont_size=18,  # Font size for the text
            textangle=0,       # Angle of the text on the bars
            textposition="outside",  # Position the text outside the bars
            cliponaxis=False,   # Prevent clipping of text
            marker=dict(color='#4254f5')
        )
        
        # Display the plot in the Streamlit app
        st.plotly_chart(fig, use_container_width=True, theme="streamlit")


#science
def bar_scie():
    theme_plotly = None  # None or streamlit
    
    with div4:  # Assuming div1 is a valid Streamlit container or section in your code
        # Create the bar plot using Plotly Express
        fig = px.bar(df_selected, 
                     y='SCIENCE_TECH',  # The column for Y-axis
                     x='SCIENCE_TECH',  # The column for X-axis
                     text_auto='.2s',     # Automatically display text on the bars
                     title="SCIENCE_TECHNOLOGY DISTRIBUTION SCORES")
        
        # Replace x-axis numeric values (1, 2, 3, 4) with custom labels
        custom_labels = {
            1: "B.E",
            2: "A.E",
            3: "M.E",
            4: "E.E"
        }
        
        # Update x-axis with custom labels
        fig.update_layout(
            xaxis=dict(
                tickmode='array',  # Set to 'array' for custom ticks
                tickvals=[1, 2, 3, 4],  # X-axis values that need to be replaced
                ticktext=[custom_labels[1], custom_labels[2], custom_labels[3], custom_labels[4]]  # Corresponding custom labels
            )
        )
        
        # Customize text appearance for the bars
        fig.update_traces(
            textfont_size=18,  # Font size for the text
            textangle=0,       # Angle of the text on the bars
            textposition="outside",  # Position the text outside the bars
            cliponaxis=False   # Prevent clipping of text
        )
        
        # Display the plot in the Streamlit app
        st.plotly_chart(fig, use_container_width=True, theme="streamlit")



#pie chart
#pie chart
def pie_cre():
   # None or streamlit
  with div1:
    fig = px.pie(df_selected, values='CRE', names='CRE',title="CRE DISTRIBUTION SCORES",hole = 0.5)
    fig.update_layout(legend_title="CRE_Scores", legend_y=0.9)
    #fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")

#pie chart
def pie_cr():
   # None or streamlit
  with div2:
    fig = px.pie(df_selected, values='CREATIVE_ARTS', names='CREATIVE_ARTS',title="CREATIVE_ART DISTRIBUTION SCORES")
    fig.update_layout(legend_title="Creative_Arts_Scores", legend_y=0.9)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    #fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")



def pie_sst():
 with div3:
  theme_plotly = None # None or streamlit
  fig = px.pie(df_selected, values='SST', names='SST', title='SOCIAL_STUDIES DISTRIBUTION SCORES',hole = 0.5)
  fig.update_layout(legend_title="SST_Scores", legend_y=0.9)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)




#......................................................................................................................................................................................
#invoking the functions to display the plotted charts
def table():
  with st.expander("Tabular"):
  #st.dataframe(df_selection,use_container_width=True)
   shwdata = st.multiselect('Filter :', data.columns, default=["GENDER","GRADE","MATHS","ENGLISH","KISWAHILI","SCIENCE_TECH","CRE","SST","CREATIVE_ARTS"])
   st.dataframe(df_selected[shwdata],use_container_width=True)
#......................................................................................................................................................................................


#option menu
from streamlit_option_menu import option_menu
with st.sidebar:
        selected=option_menu(
        menu_title="Main Menu",
         #menu_title=None,
        options=["Home","Table"],
        icons=["house","book"],
        menu_icon="cast", #option
        default_index=0, #option
        orientation="vertical",

        )
 

if selected=="Home":
    
    bar_math()
    bar_eng()
    bar_kisw()
    bar_scie()
    
    pie_sst()
    pie_cr()
    pie_cre()
    #metrics()
    #pie_scie()

   
    


if selected=="Table":
   metrics()
   table()
   st.dataframe(df_selected.describe().T,use_container_width=True)
 
#............................................................................................................................................................................................
 












































































































