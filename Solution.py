import streamlit as st 

def run() :
    st.header("My Solutions")
   
    c1,c2 = st.columns(2)
    with c1:
        st.selectbox(label = "By Date",placeholder = "select the questions to display", options = ('All','This Month','Today','This Week'))
    with c2:
        st.selectbox(label = "By Rating",placeholder = "Select date", options = ('All Solutions','Positively Rated Solution','Negatively Rated Solution ','Rated Solution'))
    st.divider()
    col1, col2 = st.columns(2)
    with col1:      
        col = st.container()
        with col:
            question1 = st.container(border = True)
            question1.write("Write a java Program for adding one and two")
            question2 = st.container(border = True)
            question2.write("Need answer Asap!!!")
            question3 = st.container(border = True)
            question3.write("SQL")
            question4 = st.container(border = True)
            question4.write("question on Computer Science")
        with col2 :
            st.subheader("Student Question",anchor = False)
            cotent = '''
A short label explaining to the user what this select widget is for. 
The label can optionally contain Markdown and supports the following elements: Bold, Italics, Strikethroughs, Inline Code, Emojis, and Links.
'''         
            st.info(cotent)

           

