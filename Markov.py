import random
def markov():
    startIndex = random.randint(0,len(text))
    currentGram = text[startIndex:startIndex+order]
    
    # Make sure it starts with a capital letter
    while not currentGram.istitle(): 
        startIndex = random.randint(0,len(text))
        currentGram = text[startIndex:startIndex+order]

    result = currentGram
    for i in range(200-order):
        possible = ngrams[currentGram]

        n = random.choice(possible)
        result += n
        currentGram = result[len(result)-order:len(result)]
    return result

text = ""

order = 5
ngrams = {}


for c in range(len(text)-(order-1)):
    gram = text[c:c+order]

    if not gram in ngrams:
        ngrams[gram] = []

    ngrams[gram].append(text[c+order:c+order+1])

print(markov())
