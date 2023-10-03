from django.shortcuts import render
from googletrans import Translator


def trans(request):
    translated_text = ""
    word_meanings = []

    if request.method == 'POST':
        text = request.POST.get('text', '')

        try:
            translator = Translator()
            word_meanings = []
            for word in text.split():
                word_translation = translator.translate(word, dest="hi")
                if word_translation and word_translation.text:  # Check if translation is not None or empty
                    word_meanings.append(f'{word} ({word_translation.text})')
            translation = translator.translate(text, dest='hi')
            translated_text = translation.text
        except Exception as e:
            translated_text = f"Translation Error: {str(e)}"

    return render(request, 'index.html', {'translated_text': translated_text, 'word_meanings': word_meanings})
