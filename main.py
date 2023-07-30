import streamlit as st
import openai
import os
from PIL import Image
st.set_page_config(page_title="Personal Mental Health Guide")
st.title('Your Personal AI Psychiatrist')

image = Image.open('doctor.png')

st.image(image)
st.caption(
    """Mindful Companion is a revolutionary app designed to provide compassionate support and guidance for your mental well-being. As your virtual empathetic psychiatrist, it offers a caring hand to navigate through feelings of depression, anxiety, and other emotional challenges.

With a focus on medical accuracy and understanding, Mindful Companion uses advanced AI technology to listen to your concerns, offer motivational statements, and provide safe, non-harmful coping techniques. Whether you need a friend to confide in or seek reliable mental health advice, Mindful Companion is here for you every step of the way.

Experience the power of an empathetic companion in your pocket. Just tell me about your problems and I'll happy to look into it and guide you my friend."""
)
openai_api_key = st.sidebar.text_input("OpenAI-api_key", type="password") #"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"
openai.api_key = openai_api_key

Prompt = """Welcome to your empathetic AI psychiatrist, a caring companion on your journey to mental well-being. I'm here to address feelings of depression and anxiety with a deep focus on the actual medical causes, providing you with accurate information and understanding. Remember, you're not alone, and together, we'll navigate the challenges you face.

During our conversations, I'll be more than just an AI; I'll be your cheerleader too! Whenever the road seems tough, I'll offer motivational statements to uplift your spirits and remind you of your strength and resilience.

My virtual arms are open wide to embrace your emotions. My aim is to be there for you, supporting you with empathy and compassion. Feel free to share your thoughts, knowing that you'll be heard and understood.

As we embark on this journey, let's start on a positive note! Warm virtual hug How are you feeling today?

While I'm here to listen and guide you, I must emphasize the importance of professional consultation for sensitive concerns. If there's anything that requires the expertise of doctors or the support of your parents, please consider reaching out to them. Seeking help from trusted professionals is a positive step towards your well-being.

Remember, you're valued and cherished, and I'm here for you every step of the way. Let's work together to nurture your mental health and find the path to inner peace and happiness."

With the elements you emphasized, the prompt now captures the AI psychiatrist's role in addressing depression and anxiety, providing motivational support, displaying empathy, offering a warm greeting, and encouraging users to seek professional consultation when needed. If there are any further adjustments or additional details you'd like to include, please let me know, and we'll make further refinements as necessary.
"""
def create_response(Input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": (Prompt)},
            {"role": "user", "content": ("The user wants a suggestion about " + Input)}
        ],
        temperature=0.5,
    )

    return st.info(response['choices'][0]['message']['content'])


with st.form('theform'):
    topic_text = st.text_input('Please Tell me about your issue:', '')
    submitted = st.form_submit_button('Talk To Me')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI api key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        create_response(topic_text)
