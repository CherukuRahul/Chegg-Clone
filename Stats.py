import streamlit as st
import pandas as pd 

def run():
    st.subheader("My Stats",anchor = False)
    data = {
        "Category" : ["CF Score","Solved","Skipped"],
        "Count" : ["4.5","10","50"]
    }
    dataf = pd.DataFrame(data)
    st.dataframe(dataf,hide_index=True,use_container_width = True)
    st.subheader("Quick links",anchor = False)
    data = {
        "Category" : ["Contact us","Authoring Guideliness"],
        "Quick Links" : ["https://www.cheggindia.com/expert-support/","https://www.cheggindia.com/chegg-qa-answering-guidelines/"]
    }
    datal = pd.DataFrame(data)
    st.dataframe(datal, column_config = {
        "Quick Links" : st.column_config.LinkColumn(
            label = "Quick Links",
            display_text = "Open Link"
        )
    }, hide_index = True,use_container_width = True
    )
    
