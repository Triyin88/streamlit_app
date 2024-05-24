
import streamlit as st


# Configure dashboard
st.set_page_config(
   page_title="E-Commerce Fraud Detection",
   layout="wide")

import base64

# dashboard title
st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Amasis MT Pro Black';
        src: url('https://path-to-your-font/AmasisMTPro-Black.ttf');  /* Ensure you provide the correct URL to the font file */
    }
    .custom-text {
        font-family: 'Amasis MT Pro Black', sans-serif;
        font-size: 60px;
        font-weight: bold;
        color: black;
    }
    </style>
    <div class="custom-text">
      E-Commerce Fraud Detection
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.success("About")

col1, spacer, col2 = st.columns([1, 0.1, 1])

with col1:
    # Display the image in Streamlit
  st.image('picture1.jpg',  width=950, caption='Image by macrovector on Freepik')

with spacer:
    st.write("")

with col2:
   st.write(
    """
    <style>
    @font-face {
        font-family: 'Amasis MT Pro Black';
        src: url('https://path-to-your-font/AmasisMTPro-Black.ttf');  /* Ensure you provide the correct URL to the font file */
    }
    .custom-text1 {
        font-family: 'Amasis MT Pro Black', sans-serif;
        font-size: 40px;
        font-weight: bold;
        color: blue;
    }
    </style>
    <div class="custom-text1">
      About this app
    </div>
    """,
    unsafe_allow_html=True
)

   st.markdown("""
    ### Introduction:
    Innovatively designed to monitor and stop fraudulent activity in the e-commerce sector is the E-commerce Fraudulent Detection System. Both customers and merchants have been quite concerned about fraud given the explosive growth in online transactions. Advanced machine learning methods are used by this software to provide a secure environment for all e-commerce sites. Developed as a prototype in the WQD7006 Machine Learning for Data Science course by Group 7, this application is expected to offer a practical and easy-to-use real-time fraud detection solution. By use of transaction data analysis, the technology so lowers financial losses and boosts confidence in the e-commerce sector.
    """)

    # Users Section
   st.markdown("""
    ### Who are its users:
    Use of this application is open to everyone who is directly or indirectly engaged in the e-commerce sector. Some of the anticipated users consist of:
    - **Online merchants**: Owners of stores who offer goods or services online and want to protect their company from dishonest practices.
    - **Payment processors**: Businesses who handle online payments and must therefore guarantee the security of any financial information.
    - **Fraud analysts**: Experts in the field of transaction monitoring and analysis in real time to spot and stop fraud.
    - **E-commerce platforms**: Organisations that provide online store infrastructures and want to keep their customers' purchasing environments safe.
    """)

    # Function of the Application Section
   st.markdown("""
    ### What is the function of this application?
    The main job of this application is to identify fraudulent e-commerce transactions. With it, users can:
    - **Convenient Data Input**: Users can either enter the transactional data manually or upload a CSV file. This adaptability accommodates the various requirements and circumstances of data availability of users. Complex machine learning models will be used to analyse the input data by the app to forecast the possibility of fraud for the specific transaction.
    - **Visual Feedback**: Users can easily grasp the likelihood of fraud and take appropriate action because they are given visual returns.
    """)

    # Purpose of the Application Section
   st.markdown("""
    ### Purpose of this Application?
    This application will be a highly useful and efficient tool to detect fraudulent transactions in the context of minimising financial loss caused by such transactions. Main goals are:
    - **For Security**: It shields customers and retailers from fraud by being a powerful solution for its detection and prevention.
    - **For Establishing Trust**: If fraud could be properly identified, people would trust it and more people would choose to conduct business online instead of in person.
    - **Educational Value**: Completing this project as part of the WQD7006 Machine Learning for Data Science course has an educational value. All e-commerce stakeholders can benefit from this application since advanced machine learning methods enable to produce precise and timely fraud detection services.
    """)













    