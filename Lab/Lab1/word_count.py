with open('testcase1-2.txt') as f:
    text = f.read()
    text = text.strip('\n').split('|')
    text = [c for c in text if c not in '\n\"\' ']

words = {}

for t in text:
    if t not in words:
        words[t] = 1
    elif t in words:
        words[t] += 1

sorted_words = sorted(words.items(), key=lambda kv : kv[1], reverse=True)

for i in sorted_words[:10]:
    print(i)