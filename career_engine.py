
CAREERS = {
    "technology": {
        "keywords": [
            "coding", "programming", "computer",
            "software", "technology", "ai", "data"
        ],
        "careers": [
            "Software Developer",
            "AI Engineer",
            "Data Analyst"
        ],
        "reason": "You are interested in technology and problem-solving."
    },
    "design": {
        "keywords": [
            "design", "drawing", "creative",
            "art", "visual", "ui", "ux"
        ],
        "careers": [
            "UI/UX Designer",
            "Graphic Designer",
            "Product Designer"
        ],
        "reason": "Your interests may fit creative and visual work."
    },
    "business": {
        "keywords": [
            "business", "management", "marketing",
            "finance", "leadership", "sales"
        ],
        "careers": [
            "Business Analyst",
            "Marketing Executive",
            "Financial Analyst"
        ],
        "reason": "Your interests may fit business and decision-making."
    },
    "science": {
        "keywords": [
            "science", "research", "experiment",
            "biology", "chemistry", "physics"
        ],
        "careers": [
            "Research Scientist",
            "Laboratory Analyst",
            "Environmental Scientist"
        ],
        "reason": "Your interests may fit scientific investigation."
    },
    "healthcare": {
        "keywords": [
            "health", "healthcare", "medical",
            "patient", "hospital", "helping people"
        ],
        "careers": [
            "Healthcare Administrator",
            "Public Health Specialist",
            "Medical Laboratory Scientist"
        ],
        "reason": "Your interests may fit healthcare and helping people."
    },
    
    "education": {
        "keywords": [
            "teaching", "teacher", "education",
            "learning", "training", "tutor"
        ],
        "careers": [
            "Teacher",
            "Instructional Designer",
            "Corporate Trainer"
        ],
        "reason": "Your interests may fit teaching and helping others learn."
    },
    "law": {
        "keywords": [
            "law", "legal", "justice", "lawyer",
            "court", "rights"
        ],
        "careers": [
            "Lawyer",
            "Legal Researcher",
            "Compliance Analyst"
        ],
        "reason": "Your interests may fit legal reasoning and justice."
    },
    "media": {
        "keywords": [
            "media", "journalism", "writing",
            "news", "video", "content", "photography"
        ],
        "careers": [
            "Content Writer",
            "Journalist",
            "Video Producer"
        ],
        "reason": "Your interests may fit communication and creative storytelling."
    }

}



def recommend_careers(user_message):
    message = preprocess_text(user_message)

    matched_domains = []

    for domain, details in CAREERS.items():
        matched_keywords = []

        for keyword in details["keywords"]:
            if keyword in message:
                matched_keywords.append(keyword)

        if matched_keywords:
            matched_domains.append({
                "domain": domain.title(),
                "careers": details["careers"],
                "reason": details["reason"],
                "matched_keywords": matched_keywords
            })

    return matched_domains


import nltk
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r"\w+")

STOP_WORDS = {
    "i", "am", "a", "an", "the", "and", "or",
    "is", "are", "was", "were", "to", "of",
    "my", "me", "in", "on", "for", "with",
    "have", "has", "it", "that", "this"
}

def preprocess_text(text):
    text = text.lower()
    words = tokenizer.tokenize(text)

    cleaned_words = [
        word for word in words
        if word not in STOP_WORDS
    ]

    return " ".join(cleaned_words)