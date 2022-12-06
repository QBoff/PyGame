import sys


s = '\n '.join([line.strip() for line in sys.stdin])

ss = []
while s:
    new_s = ""
    for i in range(len(s)):
        if s[i] == '.' or s[i] == '?' or s[i] == '!':
            new_s += s[:i + 1]
            new_s = new_s.replace("\n", "")
            ss.append(new_s)
            s = s[i + 2:]
            break


# print(ss)

sentence_pattern = r'[.?!]'
sentences = {'.': set(), '?': set(), '!': set()}

for sentence in ss:
    # print(sentence)
    punctuation = sentence[-1]
    sentence = sentence[:-1]
    # print(sentence.split())
    for word in sentence.split():
        sentences[punctuation].add(word.lower())

result = (sentences['.'] - sentences['!']) & (sentences['?'] - sentences['!'])
print(' '.join(sorted(result)))
