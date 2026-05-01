import streamlit as st
from utils import get_llm_response
from db import save_candidate

st.set_page_config(page_title="TalentScout AI")
st.title("TalentScout Hiring Assistant")

fields = ["name", "email", "phone", "experience", "role", "location", "tech_stack"]

questions_map = {
    "name": "What is your full name?",
    "email": "Enter your email address:",
    "phone": "Enter your phone number:",
    "experience": "How many years of experience do you have?",
    "role": "What role are you looking for?",
    "location": "Your current location?",
    "tech_stack": "List your tech stack (e.g., Python, Django, SQL):"
}

# Initialize session
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.chat = []
    st.session_state.completed = False

# Show chat history
for msg in st.session_state.chat:
    st.chat_message(msg["role"]).write(msg["content"])

# Welcome message
if st.session_state.step < len(fields) and not st.session_state.chat:
    st.chat_message("assistant").write("Welcome to TalentScout Hiring Assistant")
    st.chat_message("assistant").write(questions_map[fields[0]])

# Input
user_input = st.chat_input("Type your answer...")

if user_input:

    st.chat_message("user").write(user_input)

    st.session_state.chat.append({
        "role": "user",
        "content": user_input
    })

    # Prevent crash after completion
    if st.session_state.completed:
        st.chat_message("assistant").write(
            "Interview already completed. Click restart to try again."
        )

    else:
        field = fields[st.session_state.step]

        # Save user input
        st.session_state.data[field] = user_input
        st.session_state.step += 1

        # If all fields collected
        if st.session_state.step == len(fields):

            st.session_state.completed = True

            tech_stack = st.session_state.data["tech_stack"]

            prompt = f"""
Generate 3 to 5 technical interview questions for:
{tech_stack}

Rules:
- Clear
- Bullet points
"""

            questions = get_llm_response(prompt)

            st.chat_message("assistant").write("Here are your technical questions:")
            st.chat_message("assistant").write(questions)

            ending = "Thank you! Our team will contact you soon. "
            st.chat_message("assistant").write(ending)

            # Save to MySQL
            save_candidate(st.session_state.data)

        else:
            next_field = fields[st.session_state.step]
            st.chat_message("assistant").write(questions_map[next_field])

# Restart button
if st.session_state.completed:
    if st.button("Restart"):
        st.session_state.step = 0
        st.session_state.data = {}
        st.session_state.chat = []
        st.session_state.completed = False
        st.rerun()