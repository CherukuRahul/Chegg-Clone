import streamlit as st

import Homi, Expert, Solution,Stats, Account
god = st.container()
#row1 = st.columns(1)
with god :
    x , y = st.columns([0.7,0.3],gap = "large")
    row1, row2,row3 = x.tabs(["Home","Expert Q&A","My Solutions"])
    row4, row5 = y.tabs(["Stats", "Account"])
    
with row1:
    Homi.run()
with row2:
    Expert.run()
with row3:
    Solution.run()
with row4:
    Stats.run()
with row5:
    Account.run()
