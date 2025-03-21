import random
import pyttsx3
import google.generativeai as genai

# 🔹 Set up your Gemini API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your Gemini API Key

# ✅ Use an available model from your list
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# 🎭 Predefined gibberish dataset
gibberish_responses = [
    "Blorp wibble flibber nugget",
    "Snarfle dingle womp",
    "Zibble fronk snerkle",
    "Flabble snizzle worp",
    "Glibber glop snorfle"
]

# 🔹 Convert text to gibberish
def text_to_gibberish(text):
    words = text.split()
    gibberish_sentence = [random.choice(random.choice(gibberish_responses).split()) for _ in words]
    return ' '.join(gibberish_sentence)

# 🔹 Simple Markov Chain for structured gibberish
def generate_gibberish():
    response = random.choice(gibberish_responses)
    next_word = random.choice(response.split())
    return f"{response} {next_word}"

# 🔹 Get normal response using Gemini AI
def get_normal_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text if response and response.text else "(Error: No response from Gemini AI)"
    except Exception as e:
        return f"(Error: {str(e)})"

# 🔹 Convert gibberish text to speech
def speak_gibberish(gibberish_text):
    try:
        engine = pyttsx3.init()
        engine.say(gibberish_text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in TTS: {e}")

# 🔹 Main chatbot loop
def main():
    print("🎉 Welcome to Gibberlink AI (Gemini)! Type 'exit' or 'quit' to stop.")
    
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

        # 🔊 Enable TTS for structured gibberish (optional)
        speak_gibberish(structured_gibberish)

if __name__ == "__main__":
    main()
