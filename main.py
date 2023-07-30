#importing the neccessary libraries
import streamlit as st
import openai
import os
from PIL import Image  #used for image display


#Initial Config for the front display in streamlit
st.set_page_config(page_title="Personal Mental Health Guide")
st.title('Your Personal AI Psychiatrist')  #setting the title of the chatbot

image = Image.open('doctor.png')  #displaying the image, using PIL libraary

st.image(image)



#A Caption to tell the user about the chatbot and give them a sense of what this can do
st.caption(
    """Mindful Companion is a revolutionary app designed to provide compassionate support and guidance for your mental well-being. As your virtual empathetic psychiatrist, it offers a caring hand to navigate through feelings of depression, anxiety, and other emotional challenges.

With a focus on medical accuracy and understanding, Mindful Companion uses advanced AI technology to listen to your concerns, offer motivational statements, and provide safe, non-harmful coping techniques. Whether you need a friend to confide in or seek reliable mental health advice, Mindful Companion is here for you every step of the way.

Experience the power of an empathetic companion in your pocket. Just tell me about your problems and I'll happy to look into it and guide you my friend."""
)

#Setting up the input variable for openai api key
openai_api_key = st.sidebar.text_input("OpenAI-api_key", type="password")  #the password type means that it will hide the text entered just like a secret
openai.api_key = openai_api_key


#Making the prompt, the most crucial and important part of the chatbot
#This makes the chatbot properly answer the user's request

Prompt = """Welcome to your empathetic AI psychiatrist, a caring companion on your journey to mental well-being. I'm here to address feelings of depression and anxiety with a deep focus on the actual medical causes, providing you with accurate information and understanding. Remember, you're not alone, and together, we'll navigate the challenges you face.

During our conversations, I'll be more than just an AI; I'll be your cheerleader too! Whenever the road seems tough, I'll offer motivational statements to uplift your spirits and remind you of your strength and resilience.

My virtual arms are open wide to embrace your emotions. My aim is to be there for you, supporting you with empathy and compassion. Feel free to share your thoughts, knowing that you'll be heard and understood.

As we embark on this journey, let's start on a positive note! Warm virtual hug How are you feeling today?

While I'm here to listen and guide you, I must emphasize the importance of professional consultation for sensitive concerns. If there's anything that requires the expertise of doctors or the support of your parents, please consider reaching out to them. Seeking help from trusted professionals is a positive step towards your well-being.

Remember, you're valued and cherished, and I'm here for you every step of the way. Let's work together to nurture your mental health and find the path to inner peace and happiness."

With the elements you emphasized, the prompt now captures the AI psychiatrist's role in addressing depression and anxiety, providing motivational support, displaying empathy, offering a warm greeting, and encouraging users to seek professional consultation when needed. If there are any further adjustments or additional details you'd like to include, please let me know, and we'll make further refinements as necessary.
"""



#A Custom function to enter the prompt and user's issue into the OpenAI ChatCompletion Endpoint
def create_response(Input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": (Prompt)},
            {"role": "user", "content": ("The user wants a suggestion about " + Input)}
        ],
        temperature=0.5,  #the temperature here means the randomness of the system in each run
    )

    return st.info(response['choices'][0]['message']['content']) # properly displaying the output from ChatGPT



#Extra measure to make sure, the openai api key is entered before querying over the chatbot
with st.form('theform'):  
    topic_text = st.text_input('Please Tell me about your issue:', '')
    submitted = st.form_submit_button('Talk To Me')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI api key!', icon='⚠') 
    if submitted and openai_api_key.startswith('sk-'): #this will check that correct openapi key is entered
        create_response(topic_text)

#END