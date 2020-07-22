from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__, static_url_path='/static')
books = []
books.append('teach/hp1.txt')
books.append('teach/hp2.txt')
#books.append('teach/hp3.txt')
#books.append('teach/hp4.txt')
#books.append('teach/hp5.txt')
#books.append('teach/hp6.txt')
#books.append('teach/hp7.txt')

def get_wordlist(books, lower=False):
    '''Return complete book in form of list, each entry containing one word
    '''
    wordlist = []
    print("Book reading initiated...")
    for b in books:
        with open(b, errors='ignore') as f:
            raw_f = f.read()
            if lower:
                raw_f = raw_f.lower()
    
            print("Writing down wordlist for "+b+"....")
            for word in raw_f.split():
                wordlist.append(word)
            print("Wordlist prepared for "+b+"!")

    return wordlist

wordlist = get_wordlist(books)
order = 2 #In future, let user set this

    worddict = {} #Each key is string representing word, value will be list of words appearing after string in key

    for i, word in enumerate(wordlist):
        if (i+order) < len(wordlist):
            key = ' '.join(wordlist[i:i+order])
            append_to_value = ' '.join(wordlist[i+order:i+order+order])
            worddict[key] = worddict.get(key, []) + [append_to_value]
    
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/res', methods=['POST'])
def res():
    req = ''
    req = request.get_json()
    #print(type(req))
    
    if req == '':
        pick_key = random.choice(list(worddict))
    else:
	    pick_key = req
    #print(pick_key)
    choices = []
    for _ in range(12):
        choices.append(random.choice(worddict[pick_key]))
    #print(choices)
    res = jsonify(choices), 200
    return res
    
