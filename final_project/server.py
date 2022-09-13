from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", static_folder="templates")

@app.route("/englishToFrench")
def englishToFrench(englishText):
    textToTranslate = request.args.get(englishText)
    frenchText = translator.english_to_french(textToTranslate)
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish(frenchText):
    textToTranslate = request.args.get(frenchText)
    englishText = translator.french_to_english(textToTranslate)
    return englishText

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)