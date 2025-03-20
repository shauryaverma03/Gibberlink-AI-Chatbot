import os
import random
import pyttsx3
import openai

# Set OpenRouter API base URL
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = os.getenv("OPENROUTER_API_KEY")  # Load API key from environment variable

if not openai.api_key:
    print("❌ Error: OpenRouter API key is missing. Set it using an environment variable.")
    exit(1)

# Predefined gibberish responses
gibberish_responses = [
    "Blorp wibble flibber nugget",
    "Snarfle dingle womp",
    "Zibble fronk snerkle",
    "Flabble snizzle worp",
    "Glibber glop snorfle"
]

# Convert text to gibberish
def text_to_gibberish(text):
    words = text.split()
    gibberish_words = [
        random.choice(gibberish_responses).split()[i % len(random.choice(gibberish_responses).split())]
        for i, _ in enumerate(words)
    ]
    return ' '.join(gibberish_words)

# Generate structured gibberish
def generate_gibberish():
    response = random.choice(gibberish_responses)
    next_word = random.choice(response.split())
    return f"{response} {next_word}"

# Get response from DeepSeek AI via OpenRouter
def get_normal_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a fun AI that answers normally."},
                {"role": "user", "content": user_input}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.OpenAIError as e:
        return f"(Error: {e})"

# Text-to-speech function
def speak_gibberish(gibberish_text):
    engine = pyttsx3.init()
    engine.say(gibberish_text)
    engine.runAndWait()

# Main loop
def main():
    print("🎉 Welcome to Gibberlink AI! Type 'exit' or 'quit' to stop.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break

        gibberish_text = text_to_gibberish(user_input)
        structured_gibberish = generate_gibberish()
        normal_response = get_normal_response(user_input)

        print(f"Gibberlink AI (Gibberish): {gibberish_text}")
        print(f"Gibberlink AI (Structured Gibberish): {structured_gibberish}")
        print(f"Gibberlink AI (Normal): {normal_response}")

        speak_gibberish(structured_gibberish)

if __name__ == "__main__":
    main()
