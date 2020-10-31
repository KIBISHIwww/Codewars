def spin_words(sentence):
    s = sentence.split(' ')
    ans = []
    for i in s:
        if len(i)>4:
            ans.append(i[::-1])
        else:
            ans.append(i)
    return ' '.join(ans)
