import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API_URL = "https://kbbi.web.id/air/ajax_submit16con"

def check_word(word):
    word = word.strip()
    if not word:
        return (word, False)
    
    url = API_URL.replace("/air/", f"/{word}/")

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and response.text.strip():
            return (word, True)
        else:
            return (word, False)
    except Exception as e:
        print(f"[ERROR] {word}: {e}")
        return (word, False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_words():
    data = request.get_json()
    text = data.get('text', '')
    
    # Split by newline or comma
    words = [w.strip() for w in text.replace(',', '\n').split('\n') if w.strip()]
    
    results = {'baku': [], 'tidak_baku': []}
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_word, word): word for word in words}
        
        for future in as_completed(futures):
            word, found = future.result()
            if found:
                results['baku'].append(word)
            else:
                results['tidak_baku'].append(word)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
