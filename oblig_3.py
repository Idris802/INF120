__author__ = "Idris Omar"
__email__ = "mohammed.idris.omar@nmbu.no"

#%%

def loadBook(fileName):
    """
    This function loads a book from file from the Gutenburg project and strips 
    away information at the start and end of the book.
    
    Input: 
    ------
    fileName: type <str>   File name or path to file.
    
    
    Output:
    -------
    trimmedText: type <list>  Each element in list is a string and represents
                              one line in book.
    """
    with open(fileName) as file_object:
        trimmedText = file_object.readlines()
    return trimmedText[39:19969]



def removeNL_and_doLowerCase(liste_NL):
    """
    This function does three things:
        1. remove newline character ('\n') from each string
        2. remove empty book lines
        3. make all strings lowercase
    
    All strings are collected in  a new list.
    
    
    Input: 
    ------
    textList: type <list>   Each element in list is a string and represents
                            one line in book 
    
    
    Output:
    -------
    newTextList: type <list>  Each element in list is a string
    """
  
    items = []
    for i in liste_NL:
       items.append(i)
    removing_n = [x[:-1] for x in items]
    removing_n[:] = [x for x in removing_n if x] # removing empty lines
    newTextList = [string.lower() for string in removing_n]
    return newTextList
    


    
def doubleDashToSpace(liste_DD):
    """
    This function replaces double dash ('--') in the strings with one space and 
    collects all strings in a new list.
    
    Input: 
    ------
    textList: type <list>   Each element in list is a string  
    
    
    Output:
    -------
    newTextList: type <list>  Each element in list is a string
    """
    newTextList = []
    for string in liste_DD:
        replacement = string.replace('--', ' ')
        
        newTextList.append(replacement)
        
    return newTextList
            




def deleteSpecChar(liste, spec_char):
    """
    This function removes special characters from strings and collects all
    strings in a new list.
    
    Input: 
    ------
    textList: type <list>      Each element in list is a string
    specialChar: type <str>    A string representing the special character
    
    
    Output:
    -------
    newTextList: type <list>  Each element in list is a string
    """
    newTextList = []
    for k in liste:
        take_away_char = k.replace(spec_char, '')
            
        newTextList.append(take_away_char)
    return newTextList



def splitter(liste_splt):
    """
    This function splits each string into words and collects all words in a
    new list. 
    
    Input: 
    ------
    textList: type <list>      Each element in list is a string
    
    
    Output:
    -------
    wordList: type <list>  Each element in list is a string. Each string is one
                           word.
    """
    wordList = []
    wordList = ' '.join(liste_splt)
    return wordList.split()
        

def countWords(wordList):
    """
    This function counts how many times each word appears in book and collects
    results in a dictionary. 
    
    Input: 
    ------
    wordList: type <list>  Each element in list is a string. Each string is one
                           word.   
    
    
    Output:
    -------
    counts: type <dictionary>  Keys represent words and values represent number
                               of time a word has been counted.
    """
    counts = {}
    for word in wordList:
        counts[word] = counts.get(word, 0) + 1
        
    return counts


        
def getMostFrequent(counts, exclWordList, topNumber):
    """
    This function takes dictionaries of word counts and returns the most 
    frequent ones. The user defines how many of the most frequent words are 
    returned.
    
    Input: 
    ------
    counts: type <dictionary>  Keys represent words and values represent number
                               of time a word has been counted.
    exclWordList: type <list>  A list of words to be excluded from 
                               consideration (shall not be in top list)
    topNumber: type <int>      Number of top freqent words to be extracted. 
                               topNumber=10 extracts top 10 frequent words, 
                               topNumber=20 extracts top 20 frequent words,
    
    
    Output:
    -------
    topFreqWords: type <dictionary>  Keys represent words and values represent 
                                     number of time a word has been counted.
    """
    topFreqWords = []
    for key, value in counts.items():
        if key in exclWordList:
            continue
        else:
            topFreqWords.append((value, key))
    
    topFreqWords.sort(reverse=True)
    top_50 = topFreqWords[:topNumber]
    
    dictionary = {}
    
    for val, key in top_50:
        dictionary[key] = val
    
    return dictionary





if __name__ == "__main__":
    textList = loadBook('analyse_boktekst.txt')
    textList_2 = removeNL_and_doLowerCase(textList)
    newTextList = doubleDashToSpace(textList_2)
    
    
            
    specialChars = ['.', ',', ':', ';',  '[', ']', '(', ')', "'s", '"',
                    '*', '&', '!', '?']

    newTextList = deleteSpecChar(newTextList, '.')
    newTextList = deleteSpecChar(newTextList, ',')
    newTextList = deleteSpecChar(newTextList, ':')
    newTextList = deleteSpecChar(newTextList, ';')
    newTextList = deleteSpecChar(newTextList, '[')
    newTextList = deleteSpecChar(newTextList, ']')
    newTextList = deleteSpecChar(newTextList, '(')
    newTextList = deleteSpecChar(newTextList, ')')
    newTextList = deleteSpecChar(newTextList, "'s")
    newTextList = deleteSpecChar(newTextList, '"')
    newTextList = deleteSpecChar(newTextList, '*')
    newTextList = deleteSpecChar(newTextList, '&')
    newTextList = deleteSpecChar(newTextList, '!')
    newTextList = deleteSpecChar(newTextList, '?')
    
    wordList = splitter(newTextList)
    
    countedWords = countWords(wordList)
    

    # Find most fequent words that are not English prepositions, not English
    # conjunctions, not English pronouns and not "special" words.
    englPrep = ['about', 'beside', 'near', 'to', 'above', 'between', 'of', 
                'towards', 'across', 'beyond', 'off', 'under', 'after', 'by',
                'on', 'underneath', 'against', 'despite', 'onto', 'unlike', 
                'along', 'down', 'opposite', 'until', 'among', 'during', 'out', 
                'up', 'around', 'except', 'outside', 'along', 'as', 'for', 
                'over', 'via', 'at', 'from', 'past', 'with', 'before', 'in', 
                'round', 'within', 'behind', 'inside', 'since', 'without', 
                'below', 'into', 'than', 'beneath', 'like', 'through']
    
    englConj = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
    
    englPronouns = ['you', 'he', 'she', 'him', 'her', 'his', 'hers', 'yours']
    
    specialWords = ['the']
    
    alle_words = englPrep + englConj + englPronouns + specialWords
    
    the_most_freq = getMostFrequent(countedWords, all_words, 50)
    
    
    
    
    
    


    


    
