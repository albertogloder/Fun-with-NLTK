# -*- coding: utf-8 -*-
#'''
#               (`.         ,-,
#               `\ `.    ,;' /
#                \`. \ ,'/ .'
#          __     `.\ Y /.'
#       .-'  ''--.._` ` (
#     .'            /   `
#    ,           ` '   Q '
#    ,         ,   `._    \
#    |         '     `-.;_'
#    `  ;    `  ` --,.._;
#    `    ,   )   .'
#     `._ ,  '   /_
#        ; ,''-,;' ``-
#         ``-..__\``--`  ag
#'''
# Uni NLTK Project, will do some simple NLTKISH tasks.


import nltk
#Wall Street Journal tags, treebank
#from nltk.tag.simplify import simplify_wsj_tag
#Importing OrderedDict (kinda array dictionary), remembers order items are put into it
from collections import OrderedDict


while True:
    fw = raw_input("\nFile or webpage? (f/w) ")
    if (fw == 'f'):
        #Reading file, creating so many variables cause I don't know yet what this program will do in the end.. (raw, textfile)
        #this will keep asking for the file if the file is not found..
        #while True:
        file_name = raw_input("Enter the file you'd like to play with. ")
        try:
            textfile = open(file_name,'r')
            raw = textfile.read()
            break
        except IOError: #truly gracious exception handling
            print('I could not find any file named: <{}>'.format(file_name))
            pass
    elif (fw == 'w'):
        from urllib import urlopen
        from socket import timeout
        #this will keep asking for a website url if the file is not found..
        #while True:
        url = raw_input("Enter the url: ")
        try:
            site = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
            raw = nltk.clean_html(site)
            break
        except (HTTPError, URLError) as error: #truly gracious exception handling
            logging.error('Data not retrieved because %s\nURL:%s', error, url)
        #break
    else:
        print "Please Enter a valid choice"
    
    
#Tokenizing
print "Tokenizing.."
fancydata = nltk.word_tokenize(raw)
#print "PosTaggin.."
#p = nltk.pos_tag(fancydata)
#fancytext = [] #see 5

#loopy loopy menu
loop = 'y'
while (loop == 'y'):
    #fancy menu
    print "--"*21
    print "**"*9, "Menu", "**"*9
    print "1.Search words for Startswith"
    print "2.Search words for Endswith"
    print "3.Search words for Containing substring"
    print "4.Simply search a word"
    print "5.Clean from articles, conjunctions and more useless stuff"
    print "--"*21
    choice = input("Choose from the Menu! ")
    
    
    #Startswith
    if (choice == 1):
        strng = raw_input("Enter the Startswith string ")
        setw = set([word for word in fancydata if word.startswith(strng)])
        if (not setw == set([])):
            for i in setw:
                print i,
            print "--"*21
        else:
            print "I found no words matching the description"
            print "--"*21
            print "\n"
            
    #Endswith     
    elif (choice == 2):
        strng = raw_input("Enter the Endswith string ")
        sw = set([word for word in fancydata if word.endswith(strng)])
        if (not setw==set([])):
            for i in setw:
                print i,
        else:
            print "I found no words matching the description"
            print "--"*21
            print "\n"
            
    #Containing       
    elif (choice == 3):
        strng = raw_input("Enter the string the word has to contain ")
        sw = set([word for word in fancydata if (strng in word)])
        if (not setw == set([])):
            for i in setw:
                print i,
        else:
            print "I found no words matching the description"
            print "--"*21
            print "\n"
            
    #WordConcordanceSearch
    elif (choice == 4):
        text = nltk.Text(fancydata)
        strng = raw_input("Enter the string ")
        #Doing concordance
        if strng in fancydata:
            text.concordance(strng)
        else:
            print "I could not find the word", strng, "in the text" 
    
    elif (choice == 5):
        for line in textfile:
            fancytext.append(line[6:].lower())
        #list of what we don't need
        # CNJ conjunction, DET determiner, article, PRO pronoun, P proper nouns, V verbs, punct
        blacklist = ['CNJ', 'DET', 'PRO', 'P', 'TO', 'WH', 'V', 'VD', 'VG', 'VN', '.', ',', '?']

        def getFreqDistOfUsefulWords(sentences):
            wordFreq = {}
	
            for sent in sentences:
                #1. 
                #2. 
                #3. test if s is non-empty and all characters in s are alphanumeric
                clean_sent = ''.join(e for e in sent if e.isalnum() or e == ' ')
                #tokenizing
                tokens = nltk.word_tokenize(clean_sent)
                #postagging
                tagged_tokens = nltk.pos_tag(tokens)
                simplified = [(word, simplify_wsj_tag(tag)) for word, tag in tagged_tokens]
                words_req = [key for key, val in simplified if val not in blacklist]

                for word in words_req:
                    if word in wordFreq:
                        wordFreq[word] += 1
                    else:
                        wordFreq[word] = 1

            wordFreqOD = OrderedDict(sorted(wordFreq.items(), key=lambda t: t[1], reverse=True))

            for key, value in wordFreqOD.items():
                print key + " : " + str(value)

            return wordFreqOD

        getFreqDistOfUsefulWords(fancytext)
    else:
        print "Please Enter a valid choice"
    loop = raw_input("\nDo you wish to continue (y/n)? ")
    
    
    
