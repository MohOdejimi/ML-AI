from nltk.chat.util import Chat, reflections
from ml import ml
from ci_cd import cicd
from python import python


pairs = (
    (
        r"(?:hi|hello|hey)[!. ]*", 
        (
            "Hello! Ask me about ML, Python, CI/CD, system design, or software engineering.",
        )
    ),
    (
        r"(?:what is your name|who are you)[?.! ]*", 
        (
            "I'm an engineering study chatbot built with predefined NLTK rules.",
        )
    ),
    (
        r"(?:what can you do|help)[?.! ]*", 
        (
            "Ask me to explain a concept in ML, CI/CD, Python, system design, or software engineering. Try 'What is overfitting?'",
            )
    ),
    (
        r"(?:thanks|thank you)[!. ]*", 
        (
            "You're welcome! What topic should we explore next?",
        )
    ),
    (
        r"(?:bye|goodbye|quit)[!. ]*", 
        (
            "Goodbye, and keep building!",
        )
    ),
)



def topics_category(topic):
    return [(pattern, (answer,)) for pattern, answer in topic]

for topic in (ml, cicd, python):
    pairs += tuple(topics_category(topic))

engineering_chatbot = Chat(pairs, reflections)

def engineering_chat():
    print("Hi! I'm an engineering study chatbot.")
    print("Ask me about machine learning, Python, CI/CD,")
    print("or software engineering. For example: What is overfitting?")
    print("Type 'quit' to end the conversation.")
    print("=" * 72)

    engineering_chatbot.converse(quit="quit")

engineering_chat()