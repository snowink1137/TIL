import webbrowser

keywords = [
    'python',
    'javascript',
    '농구',
    '축구'
]

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open_new(url)


    