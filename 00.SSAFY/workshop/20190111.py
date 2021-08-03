import random
from flask import Flask, jsonify

app = Flask(__name__)

## variable
my_dict = {
    'apple': '사과',
    'banana': '바나나',
    'grape': '포도'
}


## route
@app.route('/')
def root():
    return 'Hi!'


@app.route('/dictionary/<string:word>')
def dictionary(word):
    
    if word in my_dict:
        result = f'{word}은(는) {my_dict[word]}'
    else:
        result = f'{word}은(는) 나만의 단어장에 없는 단어입니다!'

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)

    