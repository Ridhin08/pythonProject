#pip install googletrans==4.0.0-rc1

from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

if __name__ == "__main__":
    input_text = input("Enter the text to translate: ")
    target_language = input("Enter the target language code (e.g., 'fr' for French): ")

    translated_text = translate_text(input_text, target_language)
    print(f"Translated text: {translated_text}")


