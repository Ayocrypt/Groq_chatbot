# Custom CSS to align chat messages
def chat_message_mk():
  
    return """
    <style>
    .user-message {
        display: flex;
        justify-content: flex-end;
    }
    .user-message > div {
        background-color: #e6f3ff; /* Light theme background */
        color: #000; /* Light theme text color */
        border-radius: 10px;
        padding: 5px 10px; /* Adjusted padding for a tighter fit */
        margin-bottom: 10px;
        max-width: 70%; /* Ensures the card wraps tightly around the text */
        word-wrap: break-word;
    }
    .assistant-message {
        display: flex;
        justify-content: flex-start; /* Ensure assistant messages are aligned to the left */
    }
    .assistant-message > div {
        background-color: #f0f0f0; /* Light theme background */
        color: #000; /* Light theme text color */
        border-radius: 10px;
        padding: 5px 10px; /* Adjusted padding for a tighter fit */
        margin-bottom: 10px;
        max-width: 70%; /* Ensures the card wraps tightly around the text */
        word-wrap: break-word; /* Allow text to wrap */
    }
    /* Dark theme styles */
    body[data-theme='dark'] .user-message > div {
        background-color: #1e1e1e; /* Dark theme background */
        color: #fff; /* Dark theme text color */
        max-width: 70%; /* Ensures the card wraps tightly around the text */
        word-wrap: break-word;
    }
    body[data-theme='dark'] .assistant-message > div {
        background-color: #2a2a2a; /* Dark theme background */
        color: #fff; /* Dark theme text color */
        max-width: 70%; /* Ensures the card wraps tightly around the text */
        word-wrap: break-word; /* Allow text to wrap */
    }
    </style>
    """