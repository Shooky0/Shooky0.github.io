from pyscript import document, when

# Define your exact questions (in lowercase) and answers
qa_pairs = {
    "what is this": "This is a personal website created by Bhargav Thakur using Github Pages.",
    "hi": "Hello!",
    "hello": "Hi!",
    "when will the website be completed": "Bhargav Thakur is a student, so these are just his hobbies. He does not have any plan to finish this in a deadline."
}

@when("click", "#send-btn")
def ask_bot(event):
    input_box = document.querySelector("#user-input")
    chat_box = document.querySelector("#chat-box")
    
    user_text = input_box.value.strip()
    if not user_text:
        return

    # Clean the input: lowercase and strip ? . ! from the end
    clean_text = user_text.lower().rstrip("?.!")
    
    # Check if the question matches our dictionary
    if clean_text in qa_pairs:
        bot_reply = qa_pairs[clean_text]
    else:
        bot_reply = "I dont know yet, please ask another question."

    # Add the user's question and the bot's reply to the HTML div
    chat_box.innerHTML += f'<div class="message user"><strong></strong> {user_text}</div>'
    chat_box.innerHTML += f'<div class="message bot"><strong>Not an AI:</strong> {bot_reply}</div>'

    # Scroll to the bottom of the chat box and clear the input field
    chat_box.scrollTop = chat_box.scrollHeight
    input_box.value = ""

# Allow pressing the "Enter" key to send a message
@when("keypress", "#user-input")
def handle_enter(event):
    if event.key == "Enter":
        ask_bot(event)