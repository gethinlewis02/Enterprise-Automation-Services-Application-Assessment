# -*- coding: utf-8 -*-

import requests
import json
from googletrans import Translator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def CountPostComments():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    Posts = response.json()
    
    response = requests.get("https://jsonplaceholder.typicode.com/comments")
    Comments = response.json()
    
    PostIds = []
    for Post in Posts:
        PostIds.append(Post['id'])
    PostCount = max(PostIds)
    
    PostCommentCount = [0]*PostCount
    for Comment in Comments:
        PostCommentCount[Comment['postId']-1] += 1
        
        
    print(PostCommentCount)


def SavePostsByUsersInApertments():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    Posts = response.json()
    
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    Users = response.json()
    
    AptUserIds = []
    for User in Users:
        if 'Apt.' in User['address']['suite']:
            AptUserIds.append(User['id'])
    
    AptUserPosts = []
    for Post in Posts:
        if Post['userId'] in AptUserIds:
            AptUserPosts.append(Post)
    
    AptUserPostsJSON = json.dumps(AptUserPosts, indent = 2)
    with open("AptUserPosts.txt", "w") as OutFile:
        OutFile.write(AptUserPostsJSON)
        
def ListPopularWords():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    Posts = response.json()
    
    GoogleTranslator = Translator()
    
    PostBodies = []
    
    for Post in Posts:
        PostText = Post['body'].replace('\n', ' ')
        Translation = GoogleTranslator.translate(PostText)
        PostBodies.append(Translation.text)
        
    AllBodyText = ' '.join(PostBodies)
    AllBodyText = AllBodyText.replace(',', '')    

    BodyWords = word_tokenize(AllBodyText, preserve_line=False)
    StopWords = set(stopwords.words("english"))
    
    FilteredBodyWords = [Word for Word in BodyWords if Word.casefold() not in StopWords]

    lemmatizer = WordNetLemmatizer()
    LemmatizedWords = list(map(lemmatizer.lemmatize, FilteredBodyWords))

    WordDict = {Word:LemmatizedWords.count(Word) for Word in LemmatizedWords}
    SortedWords = dict(sorted(WordDict.items(), key = lambda Word:Word[1], reverse=True))
    
    WordFrequencyJSON = json.dumps(SortedWords, indent = 2)
    with open("WordFrequency.txt", "w") as OutFile:
        OutFile.write(WordFrequencyJSON)