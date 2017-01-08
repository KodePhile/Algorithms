def reverseVowels(word):
    if isinstance(word, str):
        word = list(word)
        
        #list of tuples containing vowels and their index
        vowelsAndPosition = [ (word[index], index) for index in
                              range(len(word))  if
                              word[index].lower() in "aeiou" ]

        lastCharIndex = -1
        for pair in vowelsAndPosition:
            word[pair[1]] = vowelsAndPosition[lastCharIndex][0]
            lastCharIndex -= 1
        return "".join(word)