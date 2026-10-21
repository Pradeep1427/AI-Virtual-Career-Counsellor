# AI Virtual Career Counsellor

## Project Overview
The AI Virtual Career Counsellor is a Python-based application that suggests possible career paths based on a user's interests and skills. It provides a conversational interface and a separate career profile form.

## Features
- Interactive chatbot built using Streamlit
- Text preprocessing using NLTK
- Rule-based career recommendations
- Support for eight career domains:
  - Technology
  - Design
  - Business
  - Science
  - Healthcare
  - Education
  - Law
  - Media
- Matched-keyword explanations
- Career profile form for skills, interests, favorite subject, and preferred work style
- Fallback response when no career keywords match

## Technologies Used
- Python
- Streamlit
- NLTK

## Project Files
- `app.py` — chatbot interface
- `career_engine.py` — career domains and recommendation logic
- `test_engine.py` — recommendation engine tests
- `profile.py` — career profile and profile-based recommendations
- `README.md` — project documentation

## Installation
Install the required packages:

```bash
python -m pip install streamlit nltk
```

## Run the Chatbot
```bash
python -m streamlit run app.py
```

## Run the Career Profile
Open a second terminal and run:

```bash
python -m streamlit run profile.py
```

## Current Limitations
The recommendation engine uses keyword matching with text preprocessing. It does not yet use a trained machine-learning model, and profile data is stored only in the active Streamlit session.

## Future Enhancements
- Machine-learning-based career recommendations
- More career domains and detailed career information
- Persistent user profiles
- Career roadmap and skill-development suggestions
- Deployment for online access
