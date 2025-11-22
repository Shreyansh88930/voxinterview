# core/config.py

ROLES = {
    "Software Engineer": {
        "description": "Focus on coding, problem-solving, and system design.",
        "levels": ["Fresher", "Junior", "Mid-level", "Senior"],
        "question_categories": ["Behavioral", "Technical", "System Design"]
    },
    "Data Analyst": {
        "description": "Focus on data analysis, SQL, and business understanding.",
        "levels": ["Fresher", "Junior", "Mid-level"],
        "question_categories": ["Behavioral", "Technical", "Case Study"]
    },
    "Sales Associate": {
        "description": "Focus on communication, negotiation, and client handling.",
        "levels": ["Fresher", "Junior", "Mid-level"],
        "question_categories": ["Behavioral", "Situational", "Roleplay"]
    }
}

PERSONAS = {
    "Friendly": {
        "tone": "warm, encouraging, and supportive",
        "style_hint": "Give positive reinforcement and gentle suggestions."
    },
    "Neutral": {
        "tone": "professional and neutral",
        "style_hint": "Keep responses concise and objective."
    },
    "Stress Interviewer": {
        "tone": "challenging and direct",
        "style_hint": "Be tougher, ask probing questions, but stay respectful."
    },
}

# A small base question bank to mix with LLM-generated content.
BASE_QUESTIONS = {
    "Software Engineer": {
        "Behavioral": [
            "Tell me about a challenging bug you fixed.",
            "Describe a time when you had to work under a tight deadline."
        ],
        "Technical": [
            "Explain the difference between a process and a thread.",
            "What is the time complexity of binary search?"
        ],
        "System Design": [
            "How would you design a URL shortener?",
            "Design a simple chat application."
        ]
    },
    "Data Analyst": {
        "Behavioral": [
            "Tell me about a time when you used data to convince someone.",
        ],
        "Technical": [
            "Explain the difference between INNER JOIN and LEFT JOIN.",
            "What is the p-value in hypothesis testing?"
        ],
        "Case Study": [
            "You notice a sudden drop in user engagement. How would you investigate?",
        ]
    },
    "Sales Associate": {
        "Behavioral": [
            "Tell me about a time you dealt with a difficult customer.",
        ],
        "Situational": [
            "What would you do if a client is unhappy with the product?",
        ],
        "Roleplay": [
            "Sell me this pen.",
        ]
    }
}
