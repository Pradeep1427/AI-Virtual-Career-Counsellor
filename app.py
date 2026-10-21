
import streamlit as st
from career_engine import recommend_careers

st.set_page_config(
    page_title="AI Virtual Career Counsellor",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Virtual Career Counsellor")
st.subheader("Discover careers that match your interests")

st.write(
    "Tell me about your interests, skills, favorite subjects, "
    "or activities. I'll suggest career paths you can explore."
)

# Store chat messages during the session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hi! 👋 Welcome to your AI Virtual Career Counsellor. "
                "What subjects do you enjoy, and what activities "
                "or skills interest you?"
            )
        }
    ]

# Display the conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
user_message = st.chat_input(
    "Describe your interests and skills..."
)

if user_message:
    # Display and store the user's message
    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )

    with st.chat_message("user"):
        st.markdown(user_message)

    # Generate career recommendations
    recommendations = recommend_careers(user_message)

    if recommendations:
        reply = "## Your personalized career suggestions 🎯\n\n"

        for item in recommendations:
            reply += f"### {item['domain']}\n\n"
            reply += f"{item['reason']}\n\n"

            # Display matched interests
            matched = item.get("matched_keywords", [])

            if matched:
                reply += "**Your matched interests:** "
                reply += ", ".join(matched) + "\n\n"

            # Display careers
            reply += "**Career options to explore:**\n\n"

            for career in item["careers"]:
                reply += f"- {career}\n"

            reply += "\n"

        reply += (
            "These are starting suggestions, not a final career "
            "decision. Tell me more about your strengths, skills, "
            "and goals to explore your options further."
        )

    else:
        reply = (
            "I'd like to understand you better! 😊\n\n"
            "Please tell me about your favorite subjects, skills, "
            "or activities. For example, you could mention "
            "coding, design, business, science, healthcare, "
            "teaching, law, or media."
        )

    # Store and display the chatbot's response
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)
