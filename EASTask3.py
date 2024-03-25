import requests
import json
import tabulate as tb
from googletrans import Translator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def CountPostComments():
    #This Function Counts and displays the number of comments for each post in the dataset
    
    #Import post and comment data from the JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    Posts = response.json()
    
    response = requests.get('https://jsonplaceholder.typicode.com/comments')
    Comments = response.json()

    
    CommentPostIds = [] #Initialise list to store Post Id values of comments
    
    #Iterate over each comment to populate PostIds list
    for Comment in Comments:
        CommentPostIds.append(Comment['postId'])
    
    PostCommentCount = [] #Initialise list to store number of comments for each post
    PostIds = [] #Initialise list to store Ids of each post
    
    #Iterate over each post to count and store number of comments for each post and respective post Id
    for Post in Posts:
        PostIds.append(Post['id'])
        PostCommentCount.append(CommentPostIds.count(Post['id']))
    
    #Create a 2-dimensional list of lists to be displayed in a table
    TableData = zip(PostIds,PostCommentCount)
    
    #Display TableData in the console
    print(tb.tabulate(TableData, headers = ['Post ID','Number of Comments'], tablefmt = 'fancy_grid'))


def SavePostsByUsersInApertments():
    #This function creates a text file containing all of the posts written by users who live in apartments.
    
    #Import post and user data from the JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    Posts = response.json()
    
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    Users = response.json()
    
    AptUserIds = [] #Initialise AptUserIds list to store IDs of users living in apartments
    
    #Iterate over Users to populate AptUserIds list
    for User in Users:
        if 'Apt.' in User['address']['suite']:
            AptUserIds.append(User['id'])
    
    AptUserPosts = [] #Initialise AptUserPosts list to store post data
    
    #Iterate over Posts to populate AptUserPosts list
    for Post in Posts:
        if Post['userId'] in AptUserIds:
            AptUserPosts.append(Post)
    
    AptUserPostsJSON = json.dumps(AptUserPosts, indent = 2) #Convert AptUserPosts list to JSON format
    
    #Save post data in a text file called AptUserPosts.txt in JSON format
    with open('AptUserPosts.txt', 'w') as OutFile:
        OutFile.write(AptUserPostsJSON)
        
def ListPopularWords():
    #This function translates the text contained in all posts from latin to english
    #it then converts every word into its lemma form and counts the number of
    #occurances of each word, storing a dictionary of each word and its frequency in
    #a text file and displaying a table of this data in the console.
    
    #Import post data from the JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    Posts = response.json()
    
    
    GoogleTranslator = Translator() #Initialise Translator variable
    
    PostBodies = [] #Initialise PostBodies list to store the text body of every post
    
    #Iterate over every post, replacing newline characters with spaces then translating
    #the post body from latin into english and adding the english text to the PostBodies list
    for Post in Posts:
        PostText = Post['body'].replace('\n', ' ')
        Translation = GoogleTranslator.translate(PostText)
        PostBodies.append(Translation.text)
        
    AllBodyText = ' '.join(PostBodies) #Concatenate all the strings in PostBodies into AllBodyText
    
    #Remove punctuation which would otherwise be tokenized as words
    AllBodyText = AllBodyText.replace(',', '') 
    AllBodyText = AllBodyText.replace("'s", '')
    
    #Tokenize the AllBodyText string
    BodyWords = word_tokenize(AllBodyText, preserve_line=False)
    
    #Create a list of stopwords to be removed from the tokenized BodyWords list
    StopWords = set(stopwords.words('english'))
    
    #Remove stopwords from BodyWords list
    FilteredBodyWords = [Word for Word in BodyWords if Word.casefold() not in StopWords]
    
    #Lemmatize all words in FilteredBodyWords list
    lemmatizer = WordNetLemmatizer()
    LemmatizedWords = list(map(lemmatizer.lemmatize, FilteredBodyWords))

    #Create a dictionary of lemmatized words and their frequency, sorted from most used to least
    WordDict = {Word:LemmatizedWords.count(Word) for Word in LemmatizedWords}
    SortedWords = dict(sorted(WordDict.items(), key = lambda Word:Word[1], reverse=True))
    
    #Convert SortedWords list to JSON format
    WordFrequencyJSON = json.dumps(SortedWords, indent = 2)
    
    #Save word frequency data in a text file called WordFrequency.txt in JSON format
    with open('WordFrequency.txt', 'w') as OutFile:
        OutFile.write(WordFrequencyJSON)
    
    #Displat word frequency data in a table in the console
    print(tb.tabulate(SortedWords.items(), headers = ['Word', 'No. Of Uses'], tablefmt = 'fancy_grid'))
    
ListPopularWords()