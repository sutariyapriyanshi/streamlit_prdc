import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk
import base64
from PIL import Image
import os

# Assuming 'lung.png' is in the same directory as your script

# Loading Image using PIL
im = Image.open('lung.png')
# Adding Image to web app
st.set_page_config(page_title="Heart Disease Predictor", page_icon = im)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('h.jpg')

st.sidebar.title('Feature Selection Menu')
choice = st.sidebar.radio("Select any",("Heart Disease Predictor","Disease Prescription","Chatbot"))

if choice=="Heart Disease Predictor":

    model = pk.load(open('Heart_disease_model.pkl', 'rb'))
    data = pd.read_csv('heart_disease.csv')

    st.header('Heart Disease Predictor')

    gender = st.selectbox('Choose Gender', data['Gender'].unique())
    if gender == 'Male':
        gen = 1
    else:
        gen = 0

    age = st.number_input('Enter Age',min_value=0, max_value=150,value=45,step=5)
    currentSmoker	 = st.number_input('Is patient currentSmoker',min_value=0, max_value=1,step=1)
    cigsPerDay	 = st.number_input('Enter cigsPerDay',min_value=0, max_value=100,step=1)
    BPMeds	 = st.number_input('Enter BPMeds',min_value=0, max_value=1,step=1)
    prevalentStroke	 = st.number_input('Is patient had storke',min_value=0, max_value=1,step=1)
    prevalentHyp = st.number_input('Enter prevalentHyp status',min_value=0, max_value=1,step=1)
    diabetes = st.number_input('Enter diabetes status',min_value=0, max_value=1,step=1)
    totChol	 = st.number_input('Enter totChol',min_value=0, max_value=500,value=190,step=10)
    sysBP = st.number_input('Enter sysBP',min_value=0, max_value=200,value=120,step=10)
    diaBP	 = st.number_input('Enter diaBP',min_value=0, max_value=150,value=80,step=10)
    BMI	 = st.number_input('Enter BMI',min_value=0, max_value=60,value=35,step=1)
    heartRate	 = st.number_input('Enter heartRate',min_value=0, max_value=150,value=70,step=10)
    glucose	 = st.number_input('Enter glucose level',min_value=0, max_value=150,value=100,step=5)

    hide_default_format = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_default_format, unsafe_allow_html=True)

    if st.button('Predict'):
        input = np.array([gen,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diabetes,BMI,heartRate,glucose]).reshape(1, -1)
        output = model.predict(input)
        if output[0] == 0:
            stn = 'Patient is Healthy,No heart Disease'
        else:
            stn = 'Patient may have Heart Disease'
        st.markdown(stn)
    # Copyright information
    copyright_html = """
    <div style="text-align: center; padding: 10px;">
    <p style="margin: 0;">&copy; 2024 Your Company. All rights reserved.</p>
    </div>
    """
    st.markdown(copyright_html, unsafe_allow_html=True)


elif choice == 'Disease Prescription':
   
    st.header("Drug Prescription")
    st.subheader("BMI (Body Mass Index)")
    st.write("BMI is a useful measure of overweight and obesity. It is calculated from your height and weight. BMI is an estimate of body fat and a good gauge of your risk for diseases that can occur with more body fat. The higher your BMI, the higher your risk for certain diseases such as heart disease, high blood pressure, type 2 diabetes, gallstones, breathing problems, and certain cancers.")
    st.image('b1.png')
    st.image('b2.png')
    st.subheader('Risk Factors for Health Topics Associated With Obesity')
    st.write('Risk Factors')
    st.markdown('- High blood pressure (hypertension)')
    st.markdown('- High LDL cholesterol ("bad" cholesterol)')
    st.markdown('- Low HDL cholesterol ("good" cholesterol))')
    st.markdown('- High triglycerides')
    st.markdown('- High blood glucose (sugar)')
    st.markdown('- Family history of premature heart disease')
    st.markdown('- Physical inactivity')
    st.markdown('- Cigarette smoking')
    st.subheader('Cholestrol')
    st.write('Cholesterol levels vary by age, weight, and sex. They typically increase over time, and people over 20 should check their cholesterol levels every 5 years.')
    st.image('chol.png')
    st.write('How can I lower my cholesterol levels?')
    st.write('According to the National Institute of Health (NIH), the following tips can help you lower your cholesterol levels')
    st.markdown('- Include heart-healthy foods in your diet')
    st.markdown('- Be physically active')
    st.markdown('- Quit smoking')
    st.markdown('- Maintain adequate weight')
    st.markdown('- Manage stress')
    st.subheader('Blood Pressure')
    st.write('To accurately gauge the state of an individual\'s cardiovascular health, healthcare professionals refer to blood pressure charts categorised by age. It is important to note that normal ranges may vary slightly depending on the source; thus, one must consider various references when assessing blood pressure values. Nonetheless, as a general guide, normal blood pressure ranges for adults are typically defined as a systolic pressure below 120 mm Hg and a diastolic pressure below 80 mm Hg.')
    st.image('bp.png')
    st.write('By understanding the normal blood pressure ranges according to age, one can identify patterns, detect potential health risks, and take proactive measures to maintain cardiovascular well-being. Regular blood pressure checks, adhering to a healthy lifestyle and adopting medical interventions when necessary are vital steps in preventing cardiovascular diseases and enhancing the overall quality of life.')
    st.write('High blood pressure can damage your arteries by making them less elastic, which decreases the flow of blood and oxygen to your heart and leads to heart disease. In addition, decreased blood flow to the heart can cause:')
    st.markdown('- Chest pain, also called angina.')
    st.markdown('- Heart attack, which happens when the blood supply to your heart is blocked and heart muscle begins to die without enough oxygen. The longer the blood flow is blocked, the greater the damage to the heart.')
    st.markdown('- Heart failure, a condition that means your heart can’t pump enough blood and oxygen to your other organs.')
    st.subheader('What behaviors increase the risk of heart disease?')
    st.title('Your lifestyle can increase your risk for heart disease.')
    st.markdown('- Eating a diet high in saturated fats, trans fat, and cholesterol has been linked to heart disease and related conditions, such as atherosclerosis. Also, too much salt (sodium) in the diet can raise blood pressure.')
    st.markdown('- Not getting enough physical activity can lead to heart disease. It can also increase the chances of having other medical conditions that are risk factors, including obesity, high blood pressure, high cholesterol, and diabetes. Regular physical activity can lower your risk for heart disease.')
    st.markdown('- Drinking too much alcohol can raise blood pressure levels and the risk for heart disease. It also increases levels of triglycerides, a fatty substance in the blood which can increase the risk for heart disease.')
    st.markdown('- Women should have no more than 1 drink a day.')
    st.markdown('- Men should have no more than 2 drinks a day. ')
    st.markdown('- Tobacco use increases the risk for heart disease and heart attack:')
    st.markdown('- Cigarette smoking can damage the heart and blood vessels, which increases your risk for heart conditions such as atherosclerosis and heart attack.')
    st.markdown('- Nicotine raises blood pressure.')
    st.markdown('- Carbon monoxide from cigarette smoke reduces the amount of oxygen that your blood can carry.')
    st.markdown('- Exposure to secondhand smoke can also increase the risk for heart disease, even for nonsmokers.')
    st.subheader('How do genetics and family history affect the risk of heart disease?')
    st.write('When members of a family pass traits from one generation to another through genes, that process is called heredity.')
    st.write('Genetic factors likely play some role in high blood pressure, heart disease, and other related conditions. However, it is also likely that people with a family history of heart disease share common environments and other factors that may increase their risk.')
    st.write('The risk for heart disease can increase even more when heredity combines with unhealthy lifestyle choices, such as smoking cigarettes and eating an unhealthy diet.')
    st.subheader('Do age and sex affect the risk of heart disease?')
    st.write('Heart disease is the number one killer of both men and women. Heart disease can happen at any age, but the risk goes up as you age.')
    st.subheader('Do race and ethnicity affect the risk of heart disease?')
    st.write('Heart disease and stroke can affect anyone, but some groups are more likely to have conditions that increase their risk for cardiovascular disease.')
    st.write('Heart disease is the leading cause of death for people of most racial and ethnic groups in the United States, including African Americans, American Indians and Alaska Natives, and white people. For Asian Americans and Pacific Islanders and Hispanics, heart disease is second only to cancer.')

else :
    # Placeholder responses for the chatbot
    def get_assistant_response(user_input):
        if user_input == 'what is project theme?':
            return "Our Project Theme is Heart disease predictor, it is called Apollo 20"
        elif user_input == 'Tell me about heart disease':
            return "Please refer to the disease and prescription page."
        elif user_input == 'Hi, how are you?':
            return "I'm good. What about you?"
        elif user_input == 'I am also good':
            return "Sounds Good"
        elif user_input == 'Help':
            return "Do you need any help?"
        else:
            return "I'm sorry, I didn't understand that."

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        # Accept user input
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message st
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant response
        assistant_response = get_assistant_response(prompt)

        # Add assistant message to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
