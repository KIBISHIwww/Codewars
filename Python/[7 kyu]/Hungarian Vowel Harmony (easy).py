def dative(word):
    word1 = ''.join(reversed(word))
    vowel1 = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']
    vowel2 = ['a', 'á', 'o', 'ó', 'u', 'ú']
    i = 0
    while i < len(list(word)):
        if (list(word1)[i]) in vowel1:
            return "".join((word, 'nek'))
        if (list(word1)[i]) in vowel2:
            return "".join((word, 'nak'))
        i+=1
