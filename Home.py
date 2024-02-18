import streamlit as st 
import Images 
st.title(":orange[Chegg]", help = "largest Tutoring Center ")
st.subheader("Hello Cheruku Rahul",anchor = False)
st.title(":bold[What would you like to do today?]",anchor = False)
row1 ,row2 = st.columns([0.7,0.3])

with row1 :
    x = st.container(border = True)
    x.image("Images\computer.jpg", width = 100)
    x.page_link(page = "pages/Dashboard.py"  ,
                label = ":bold[Expert Q&A]",
                 use_container_width = True )
    x.caption("start solving student questions.")

