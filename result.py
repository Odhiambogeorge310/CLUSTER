#import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
theme_plotly = None
from streamlit_extras.metric_cards import style_metric_cards
#...............................................................................................................................

#Setting page
st.set_page_config(page_title="Cluster_Dashboard", page_icon=":school:", layout="wide")
#main page title
st.title("🎓CLUSTER_DASHBOARD")
st.markdown('<style>h1{padding-top:2rem;}</style>', unsafe_allow_html=True)
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
st.subheader("Roll_Summary")
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

#pie chart
def pie_math():
 with div1:
  theme_plotly = None # None or streamlit
  fig = px.pie(df_selected, values='MATHS', names='MATHS', title='Maths Distribution')
  fig.update_layout(legend_title="Maths_Scores", legend_y=0.9)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#pie chart
def pie_english():
   # None or streamlit
  with div2:
    fig = px.pie(df_selected, values='ENGLISH', names='ENGLISH',title="English Distribution",hole = 0.5)
    fig.update_layout(legend_title="English_Scores", legend_y=0.9)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    #fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")


def pie_scie():
   # None or streamlit
  with div3:
    fig = px.pie(df_selected, values='SCIENCE_TECH', names='SCIENCE_TECH',title="Science Distribution")
    fig.update_layout(legend_title="Science_Scores", legend_y=0.9)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    #fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")


#pie chart
def pie_kisw():
   # None or streamlit
  with div4:
    fig = px.pie(df_selected, values='KISWAHILI', names='KISWAHILI',title="KISWAHILI Distribution",hole = 0.5)
    fig.update_layout(legend_title="kiswahili_Scores", legend_y=0.9)
    #fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")


#bar chart
def bar_art():
    theme_plotly = None  # None or streamlit
    
    with div1:  # Assuming div1 is a valid Streamlit container or section in your code
        # Create the bar plot using Plotly Express
        fig = px.bar(df_selected, 
                     y='CREATIVE_ARTS',  # The column for Y-axis
                     x='CREATIVE_ARTS',  # The column for X-axis
                     text_auto='.2s',     # Automatically display text on the bars
                     title="CREATIVE_ARTS DISTRIBUTION")
        
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

#SST
def bar_sst():
    theme_plotly = None  # None or streamlit
    
    with div2:  # Assuming div1 is a valid Streamlit container or section in your code
        # Create the bar plot using Plotly Express
        
        fig = px.bar(df_selected, 
                     y='SST',  # The column for Y-axis
                     x='SST',  # The column for X-axis
                     text_auto='.2s',     # Automatically display text on the bars
                     title="SST DISTRIBUTION")
        
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


#CRE
def bar_cre():
    theme_plotly = None  # None or streamlit
    
    with div3:  # Assuming div1 is a valid Streamlit container or section in your code
        # Create the bar plot using Plotly Express
        fig = px.bar(df_selected, 
                     y='CRE',  # The column for Y-axis
                     x='CRE',  # The column for X-axis
                     text_auto='.2s',     # Automatically display text on the bars
                     title="CRE DISTRIBUTION")
        
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


#math
def bar_math():
    theme_plotly = None  # None or streamlit
    
    with div4:  # Assuming div1 is a valid Streamlit container or section in your code
        # Create the bar plot using Plotly Express
        fig = px.bar(df_selected, 
                     y='MATHS',  # The column for Y-axis
                     x='MATHS',  # The column for X-axis
                     text_auto='.2s',     # Automatically display text on the bars
                     title="MATHS DISTRIBUTION")
        
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
    
    pie_math()
    pie_english()
    pie_kisw()
    #metrics()
    pie_scie()

    bar_art()
    bar_sst()
    bar_cre()
    bar_math()
    


if selected=="Table":
   metrics()
   table()
   st.dataframe(df_selected.describe().T,use_container_width=True)
 
#............................................................................................................................................................................................
 












































































































