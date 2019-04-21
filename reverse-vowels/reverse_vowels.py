def reverseVowels(word):
    if isinstance(word, str):
        word = list(word)
        
        #list of tuples containing vowels and their index
        vowels_and_their_positions = [ (word[index], index) for index in
                              range(len(word))  if
                              word[index].lower() in "aeiou" ]

        last_char_index = -1
        #Reverse vowels
        for pair in vowels_and_their_positions:
            word[pair[1]] = vowels_and_their_positions[last_char_index][0]
            last_char_index -= 1
        return "".join(word)
