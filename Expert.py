import streamlit as st
def run():
    st.subheader("Dear Expert!")
    st.write("Thank you for your efforts on Chegg Q&A! Unfortunately, no Qs are available in your queue at the moment.")
    st.write(":blue[Possible Reasons]")
    content = '''
    :small_orange_diamond: You have skipped all the available Qs. \n
:small_orange_diamond: All available Qs are currently being solved by other experts. You’ll get more Qs as and when students ask more Qs, or when other Experts release Qs that are currently locked by them.\n
:small_orange_diamond: Your quality score is low.'''
    st.info(content)
    st.write(":blue[What can you do now?]")
    an_content = ''' 
:small_orange_diamond: Refresh the page after some time to check for newly posted questions. Most new Qs are posted between 1AM – 8AM. Login during this time to avail more Qs.\n
:small_orange_diamond: Improve your quality score to become eligible for solving more Qs.
'''
    st.info(an_content)
    col1, col2 = st.columns([0.7,0.3])
    with col1 :
        st.write("Got a query? Reach out to our self-help section OR raise a query ticket at :")
    with col2:
        st.page_link(label = "Chegg - Support",page = "https://qnasupport.cheggindia.com/portal/en/home",use_container_width = True)
