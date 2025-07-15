
import streamlit as st
import requests,base64
from datetime import datetime
import time,os
import streamlit as st

from scipy.io.wavfile import write
def typewriter(text: str):
    """
    Simulates a typewriter effect for displaying text character by character.

    Parameters:
    - text: The text to be displayed.
    """
    speed = 13  # Speed of the typewriter effect
    tokens = text.split()  # Split the text into words
    container = st.empty()  # Create a placeholder for displaying the text

    # Display the text one word at a time
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.write(f"{curr_full_text} ⚪️")
        time.sleep(1 / speed)  # Pause for the specified speed

import requests
from packaging import version as vs
from PIL import Image
#icon=Image.open("Logo.png")
session=requests.Session()
st.set_page_config(
    page_title="Langchain Tools and Agents",
    page_icon="🤖",
    #]theme='black',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
             'Get Help':'https://www.linkedin.com/in/shadrach-bruce-arhin-8154462a2',
             'Report a bug':"https://facebook.com",
             'About':'# This is an LLM-powered Chatbot!'
    }
    )

st.header("⚡🤖:rainbow[ BRUCE CHATBOT ]🤖⚡",anchor='centered',divider="rainbow")
st.divider()


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "STORE" not in st.session_state:
    st.session_state.STORE={}
    
if "thread" not in st.session_state:
    st.session_state.thread=[]

# Function to download a file
def download_file_from_flask(file_name):
    try:
        
        url = f'http://127.0.0.1:8000/download/{file_name}.json'  # Adjust this URL if needed
        response = requests.get(url)

        if response.status_code == 200:
            return response.content  # Return the file content
        else:
            st.error(f'Error downloading file: {response.status_code}')
            return None
    except Exception as er:
        st.error(f'Error Contacting Server : {er}')
with st.sidebar:
        
        st.title(":green[AKWAABA] ",anchor= 'centered')
        st.markdown('''
        About ⬇️
      \nThis is an LLM-powered Chatbot Built Using:
      \n- [Streamlit](https://streamlit.io) 
      \n- [OPENAI](https://platform.openai.com/usage)
      \n- [Langchain](https://python.langchain.com/docs)\n ''')
   
 
        st.write("Made with ❤️ by prompt Engineer Bruce Arhin Shadrach")
        if st.session_state.thread:
            st.write('Download Your Conversation History ')
            if  st.button('Submit',type='primary'):
                data=download_file_from_flask(f"{st.session_state.thread[0]}")
                if data:
                    st.download_button(
                        label='Download',
                        data=data,
                        file_name=f"{st.session_state.thread[0]}.json",
                        mime="application/octet-stream")

            
    
def Loading():
        secret:str=st.text_input('Insert Your Authorization Key Here',type="password",max_chars=31 )
        login=st.button("Login ")
        if login:
            
                    
                    if secret and secret.startswith('thread_'):
                        
                        try:
                            with st.spinner(" Establishing Connection"):
                                    headers = {
                                        "Authorization": secret,
                                        "Content-Type": "application/json"
                                    }
                                    Thread=session.get('http://127.0.0.1:8000/Login/Authenticate',headers=headers)
                                     
                                    
                                    text=st.empty()
                                    text.write("⏳  Making API Request")
                                    time.sleep(0.5)
                                    text.write("⏳ Authenticating Authorization Key")
                                    
                                    if Thread.status_code==200:
                                        outt=Thread.json()
                                        text.write('Authentication successful')
                                        time.sleep(1)
                                        st.session_state.thread.append(secret)
                                        text.write("⏳  Downloading Previous Chat Conversation")
                                        
                                        time.sleep(2)
                                        
                                        time.sleep(0.5)
                                        text.write("⏳  Reconstruction Chat Conversation")
                                        for pair in outt:

                                                
                                            st.session_state.messages.append({"role": "Human", "content": f"`User:` {pair["Human"]}","time":f"{pair.get('time','')}"})
    
                                            st.session_state.messages.append({"role": "AI", "content": f"`ChatBot:` {pair["AI"]}","time":f"{pair.get('time','')}"})
                                        text.write("⏳  Reconstructing Previous Chat Conversation")
                                        time.sleep(2)
                                        time.sleep(1)
                                        
                                        greet=session.post("http://127.0.0.1:8000/Greetings",json={"History": st.session_state.messages})
                                        
                                       
                                        
                                        
                                        if greet.status_code==200:
                                            text.write("⏳  Establishing Connection....... ")
                                            time.sleep(0.2)
                                            text.write("⏳  Establishing Connection.. ")
                                            time.sleep(1)
                                            time.sleep(0.2)
                                            text.write("⏳  Connection Established ")
                                            time.sleep(0.2)
                                            text.empty()
                                            outy=greet.text
                                            respond=f"`ChatBot:` {outy}"
                                            with st.chat_message("assistant"):
                                                typewriter(text=respond)
                                            # Add assistant response to chat history
                                            st.session_state.messages.append({"role": "AI", "content": respond})
                                        else:
                                            st.warning(":red[Error: Unable to Establish Connection]",icon="⚠️")
                                        st.toast('Message was Loaded Sucessfully',icon='✔️')   
                                    elif Thread.status_code==202:
                                        text.write(f"{Thread.json().get('status')}")
                                        time.sleep(2)
                                        text.write(f"{Thread.json().get('message')}")
                                        time.sleep(2)
                                        time.sleep(1)
                                        st.session_state.thread.append(secret)
                                        
                                        greet=session.post("http://127.0.0.1:8000/Greetings",json={"History": st.session_state.messages})
                                        text.write("⏳  Establishing Connection....... ")
                                        time.sleep(0.2)
                        
                                        text.write("⏳  Establishing Connection.. ")
                                        time.sleep(1)
                                        time.sleep(0.2)
                                        text.write("⏳  Connection Established ")
                                        time.sleep(0.2)
                                        text.empty()
                                        
                                    
                                        if greet.status_code==200:
                                            outy=greet.text
                                            respond=f"`ChatBot:` {outy}"
                                            with st.chat_message("assistant"):
                                                typewriter(text=respond)
                                            # Add assistant response to chat history
                                            st.session_state.messages.append({"role": "AI", "content": respond})
                                        else:
                                            st.warning(":red[Error: Unable to Establish Connection]",icon="⚠️")
                                        st.toast(f"{Thread.json().get('message')}",icon='❌')
                                                
                                    else:
                                        st.warning(f":red[Error: {Thread.text}]",icon="⚠️")
                                                
                                        
                        except:
                            st.warning(":red[Error: Unable to Establish Connection, Server Maybe Down OR Under Maintanance.]",icon="⚠️")  
                    else:
                        st.warning(f":red[Error: Authorization Key Needed]",icon="⚠️")

        
       
def Chat():
    query=st.chat_input("Message Bruce ChatBot",key="sageinput",accept_file=True,file_type=["jpg", "jpeg", "png"])
    if query and query["files"] and query.text:
        st.image(query["files"][0])
    elif query and query.text:
        User=f"`User:` {query.text}"
   
        # Display user message in chat message container
        st.chat_message("user").markdown(User)
        # Add user message to chat history
        st.session_state.messages.append({"role": "Human", "content":User, 'time':datetime.now().strftime("%d/%m/%Y, %H:%M:%S")})
        #st.write(st.session_state.messages)
        try:
            with st.spinner("Just a moment, Thinking !! "):
                headers = {
                            "Authorization": st.session_state.thread[0],
                            "Content-Type": "application/json"
                                    }  
                response = session.post('http://127.0.0.1:8000/api/chat/Agent', json={'message': query.text,'memory':st.session_state.messages,"Thread":st.session_state.thread},headers=headers)
                
                if response.status_code == 200:
                    out = response.text
                
                  
                    respond=f"`ChatBot:` {out}"
                    with st.chat_message("assistant"):
                        typewriter(text=respond)
                    st.toast('There you Go!',icon='✔️') 
                    
                # Add assistant response to chat history
                    st.session_state.messages.append({"role": "AI", "content": respond,'time':datetime.now().strftime("%d/%m/%Y, %H:%M:%S")})
                else:
                    st.warning(f":red[{'A Server Error. This Error is from ourside, Please Try Again' if not response.text else response.text}]",icon="⚠️")
                
        except requests.exceptions.RequestException:
                    st.write("Error: Unable to Establish connection to the Flask server.")  
   
        # query["files"][0].getvalue()
        # base64.b64encode(query["files"][0].getvalue()).decode()



if not st.session_state.thread:
   Loading()
    
 
                                  
if st.session_state.thread:
    Chat()
    
    
    
                    
