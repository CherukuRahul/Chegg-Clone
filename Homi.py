import streamlit as st 
import Expert
def run() :
    st.subheader("Welcome, Expert!",anchor = False)
    expert = st.container(border = True)
    with expert :
        st.write("Expert Q&A")
        content = '''
Quality Tip : \n
Students love reading clear, step-by-step solutions.Author well-explained solutions
using our in-built editor tools.
'''
        st.info(content)
        dummy,button, alimit,aprice = st.columns([0.1,0.3,0.3,0.3])
        con  = '''Increase your Authoring Limit by increasing your :orange[Chegg] and :orange[Student] :grey[Rating]'''
        with button :
            st.button("Start Solving")
            st.caption('''Click  to start :    :orange[Solving]''')
        with alimit :
            st.metric(label = "Authoring Limit",
                  value = "10",
                  delta = "+10",
                  help = con)
        with aprice:
            st.metric(label = "Authoring Price",
                  value = "1x",
                  delta = "1x",
                  help = con)
    Questions = st.container()
    with Questions :
        Questions.write("Frequently Asked Questions")
        e1 = st.expander(label = "My question got skipped automatically.How can i get the same question again", expanded = True)
        e2 = st.expander(label = "What happen if my account gets revoked?", expanded = False)
        e3 = st.expander(label = "Can i change my bank details", expanded = False)
        e4 = st.expander(label = "Can i change my pan card details", expanded = False)
        with e1 :
            st.info("Once a question gets skipped, you cannot get it back. Questions on Q&A board get auto-skipped if you log in on multiple devices or from multiple browsers simultaneously. They may also get auto-skipped due to disruption of internet connection or when you leave your computer screen idle for more than 15 minutes.")
        with e2 :
            st.info("Once revoked, your account cannot be re-instated ever in the same or in any other subject. Payment for all eligible solutions will be settled in accordance with the terms and conditions of your engagement with Chegg in the upcoming payment cycle.")
        with e3 :
            st.info("No. Bank account details once submitted cannot be changed.")
        with e4 :
            st.info("No. PAN Card details once submitted cannot be changed.")
        
       