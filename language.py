import os
import google.generativeai as genai

def translate_text(text, target_language):
    # Use API key directly
    api_key = "AIzaSyDROwYZteldsAG4tscPig5rhvNX6iZZiys"
    
    # Configure the Gemini API
    genai.configure(api_key=api_key)
    
    # Create the model
    model = genai.GenerativeModel('gemini-1.5-pro')

    prompt = f"Translate the following text to {target_language}: {text}"
    
    # Generate the response
    response = model.generate_content(prompt)
    
    return response.text

def main():
    print("Welcome to the Language Translator!")
    print("-----------------------------------")
    
    while True:
        text = input("\nEnter the text to translate (or 'quit' to exit): ")
        if text.lower() == 'quit':
            break
            
        target_language = input("Enter the target language (e.g., Spanish, French, German): ")
        
        try:
            translated_text = translate_text(text, target_language)
            print("\nTranslation:")
            print(translated_text)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
