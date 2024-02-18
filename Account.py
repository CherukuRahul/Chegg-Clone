import streamlit as st 

def run():
    col1, col2, col3 = st.columns([0.25,0.5,0.25])
    with st.expander("Education Background") :
        st.write("Degree: B_tech")
    with st.expander("Skills"):
        st.write("Java, Python")
    with st.expander("Family Background"):
        st.write("Father,Mother,Brother,Me")
    col3, col4, col5 = st.columns([0.25,0.5,0.25])
    with col4:        
        st.button(label = "Log Out")

    
