import subprocess
import streamlit as st
import streamlit.components.v1 as components
from groq import Groq  # Import Groq API
from dotenv import load_dotenv
import os
from chat_message_mk import chat_message_mk

load_dotenv()

st.set_page_config(
    page_title="Groq Chatbot",
    initial_sidebar_state="expanded"
)





st.title("Streamlit Groq Chatbot")
st.info("This is a simple chatbot powered by the Groq API. It is designed to be a fun and interactive way to chat with the chatbot. The chatbot is designed to be a fun and interactive way to chat with the chatbot. The chatbot is designed to be a fun and interactive way to chat with the chatbot.")


# load custom css
chat_message_mk()
st.markdown(chat_message_mk(), unsafe_allow_html=True)


# Function to toggle theme
def toggle_theme():
    config_path = os.path.expanduser(os.path.join('~', ".streamlit", "config.toml"))

    try:
        with open(config_path, "r") as f:
            config = f.read()
    except FileNotFoundError:
        st.error(f"Config file not found at {config_path}. Creating a new one.")
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        config = '[theme]\nbase = "light"\n'
    
    if "base = \"light\"" in config:
        new_config = config.replace("base = \"light\"", "base = \"dark\"")
    else:
        new_config = config.replace("base = \"dark\"", "base = \"light\"")
    
    with open(config_path, "w") as f:
        f.write(new_config)
    




# sets up sidebar nav widgets
with st.sidebar:
    st.markdown("# Chat Options")

    # Select model (Groq models available)
    model = st.selectbox('What model would you like to use?', ('llama3-8b-8192', 'llama3-70b-8192'))

    # Temperature setting
    temperature = st.number_input('Temperature', value=0.7, min_value=0.1, max_value=1.0, step=0.1,
                                  help="The temperature setting to be used when generating output from the model.")

    # Max token length
    max_token_length = st.number_input('Max Token Length', value=1000, min_value=200, max_value=1000, step=100,
                                       help="Maximum number of tokens to be used when generating output.")
    
    # Theme toggle button
    components.html(
        """
  
        """,
        height=120,
    )
    st.toggle("Toggle Theme", key="theme-toggle-button", help="Toggle the theme of the chatbot", on_change=toggle_theme, label_visibility="visible")




# checks for existing messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to get the current theme
def get_current_theme():
    return st.session_state.get("theme-toggle-button", False)

# Display chat messages from session state
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'''
            <div class="user-message" style="display: flex; align-items: center;">
                <div style="margin-left: auto; margin-right: 10px; display: none;"></div>  <!-- No avatar for user -->
                <div>{message["content"]}</div>
            </div>
        ''', unsafe_allow_html=True)
    else:
        # Determine the appropriate avatar based on the theme
        if get_current_theme():  # Dark theme
            avatar_image = 'https://de3516419baed78fc1226297c7180913.cdn.bubble.io/f1706222499253x610178193274935000/Logo.svg'
            # avatar_image = "https://img.freepik.com/free-vector/chatbot-conversation-vectorart_78370-4107.jpg?t=st=1727188704~exp=1727192304~hmac=90b1b465ca04d75fe49390a9fe3d989424bb44e29f73bc231153972c407c357d&w=1060"
        else:  # Light theme
            # avatar_image = "https://img.freepik.com/free-vector/chatbot-conversation-vectorart_78370-4107.jpg?t=st=1727188704~exp=1727192304~hmac=90b1b465ca04d75fe49390a9fe3d989424bb44e29f73bc231153972c407c357d&w=1060"
            avatar_image = 'https://de3516419baed78fc1226297c7180913.cdn.bubble.io/f1706222499253x610178193274935000/Logo.svg'
        st.markdown(f'''
            <div class="assistant-message" style="display: flex; align-items: center;">
                <img src="{avatar_image}" style="width: 30px; height: 30px; margin-right: 10px;" />  <!-- Custom assistant avatar -->
                <div>{message["content"]}</div>
            </div>
        ''', unsafe_allow_html=True)

# Function to interact with Groq API
def groq_chat(user_prompt, model, max_tokens, temp):
    client = Groq(api_key="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")
    chat_completion = client.chat.completions.create(
        messages=[
            {"role":"system", "content":"Your name is Groq Bot an assignment instance"},
            {"role": "user", "content": user_prompt}
        ],
        model=model,
        max_tokens=max_tokens,
        temperature=temp
    )
    return chat_completion.choices[0].message.content

if user_prompt := st.chat_input("Message Groq Here"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    st.markdown(f'''
        <div class="user-message" style="display: flex; align-items: center;">
            <div style="margin-left: auto; margin-right: 10px; display: none;"></div>  <!-- No avatar for user -->
            <div>{user_prompt}</div>
        </div>
    ''', unsafe_allow_html=True)

    with st.spinner('Generating response...'):
        # Retrieves response from Groq
        groq_response = groq_chat(user_prompt, model=model, max_tokens=max_token_length, temp=temperature)

        # Appends response to the message list in session state
        st.session_state.messages.append({"role": "assistant", "content": groq_response})

    # Display assistant response in chat message container

        avatar_image = 'https://de3516419baed78fc1226297c7180913.cdn.bubble.io/f1706222499253x610178193274935000/Logo.svg'
        st.markdown(f'''
            <div class="assistant-message" style="display: flex; align-items: center;">
                <img src="{avatar_image}" style="width: 30px; height: 30px; margin-right: 10px;" />  <!-- Custom assistant avatar -->
                <div>{groq_response}</div>
            </div>
        ''', unsafe_allow_html=True)
