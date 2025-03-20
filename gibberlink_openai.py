import random
import pyttsx3
import openai

# Predefined dataset of gibberish responses
gibberish_responses = [
    "Blorp wibble flibber nugget",
    "Snarfle dingle womp",
    "Zibble fronk snerkle",
    "Flabble snizzle worp",
    "Glibber glop snorfle"
]

# Function to convert text to gibberish
def text_to_gibberish(text):
    words = text.split()
    gibberish_sentence = []
    
    for word in words:
        gibberish_words = random.choice(gibberish_responses).split()
        gibberish_sentence.append(random.choice(gibberish_words))  # Pick a random gibberish word

    return ' '.join(gibberish_sentence)

# Simple Markov Chain for generating structured gibberish
def generate_gibberish():
    response = random.choice(gibberish_responses)
    next_word = random.choice(response.split())
    return f"{response} {next_word}"

# Function to get a normal response using OpenAI's GPT
def get_normal_response(user_input):
    openai.api_key = 'OpenAI-API-Key'  # Replace with your OpenAI API key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a fun and playful AI that sometimes responds in gibberish."},
                {"role": "user", "content": user_input}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"(Error: {str(e)})"

# Text-to-speech function
def speak_gibberish(gibberish_text):
    try:
        engine = pyttsx3.init()
        engine.say(gibberish_text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in TTS: {e}")

def main():
    print("Welcome to Gibberlink AI! Type 'exit' or 'quit' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        gibberish_text = text_to_gibberish(user_input)
        structured_gibberish = generate_gibberish()
        normal_response = get_normal_response(user_input)
        
        print(f"\nGibberlink AI (Gibberish): {gibberish_text}")
        print(f"Gibberlink AI (Structured Gibberish): {structured_gibberish}")
        print(f"Gibberlink AI (Normal): {normal_response}\n")

        # Enable TTS only for structured gibberish (optional)
        speak_gibberish(structured_gibberish)

if __name__ == "__main__":
    main()

