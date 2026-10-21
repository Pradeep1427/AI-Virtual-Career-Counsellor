from career_engine import recommend_careers
import streamlit as st

st.set_page_config(
    page_title="Career Profile",
    page_icon="👤",
    layout="centered"
)

st.title("👤 Career Profile")
st.write(
    "Tell us about yourself to help explore suitable careers."
)

# Create a form to collect the user's details
with st.form("career_profile_form"):
    skills = st.text_input(
        "Your skills",
        placeholder="Example: Python, communication, drawing"
    )

    interests = st.text_input(
        "Your interests",
        placeholder="Example: AI, design, teaching"
    )

    favorite_subject = st.selectbox(
        "Favorite subject",
        [
            "Computer Science",
            "Mathematics",
            "Science",
            "Business",
            "Arts",
            "Languages",
            "Other"
        ]
    )

    work_style = st.selectbox(
        "Preferred work style",
        [
            "Solving technical problems",
            "Creative work",
            "Working with people",
            "Research and analysis",
            "Business and management"
        ]
    )

    submitted = st.form_submit_button("Create My Profile")

# Save the submitted information using a separate session-state key
if submitted:
    st.session_state["saved_career_profile"] = {
        "skills": skills,
        "interests": interests,
        "favorite_subject": favorite_subject,
        "work_style": work_style
    }

    st.success("Your career profile has been created!")

# Display the saved profile
if "saved_career_profile" in st.session_state:
    profile = st.session_state["saved_career_profile"]

    st.subheader("Your Profile Summary")
    st.write("**Skills:**", profile["skills"] or "Not provided")
    st.write("**Interests:**", profile["interests"] or "Not provided")
    st.write("**Favorite subject:**", profile["favorite_subject"])
    st.write("**Preferred work style:**", profile["work_style"])


    st.divider()
    st.subheader("🎯 Career Recommendations Based on Your Profile")

    profile_text = (
        profile["skills"] + " " + profile["interests"]
    )

    recommendations = recommend_careers(profile_text)

    if recommendations:
        for item in recommendations:
            st.markdown(f"### {item['domain']}")
            st.write(item["reason"])

            if item.get("matched_keywords"):
                st.write(
                    "Matched interests:",
                    ", ".join(item["matched_keywords"])
                )

            st.write("Career options:")
            for career in item["careers"]:
                st.write(f"- {career}")
    else:
        st.info(
            "No matching careers found yet. Try adding skills "
            "or interests such as coding, design, business, "
            "science, teaching, law, or media."
        )
