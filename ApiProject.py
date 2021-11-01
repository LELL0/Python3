import requests
import urllib, json

def intInput(text):
    print(text,end='')
    v=0
    while v==0:
        try:
            x=int(input())
            v=1
        except ValueError:
            print("Input a number !!!")
            v=0
    return x

############################################################################################################################################################################################
def containsJoke(keyword):
    r=requests.get('https://v2.jokeapi.dev/joke/Any?contains={}'.format(keyword))
    r=r.json()
    print('\n{0}\n{1}'.format(r['setup'],r['delivery']))

def randomJoke():
    r = requests.get('https://official-joke-api.appspot.com/random_joke')
    r=r.json()
    print('\n{0}\n{1}'.format(r['setup'],r['punchline']))


def nRandomJokes(num):
    r = requests.get('https://official-joke-api.appspot.com/jokes/programming/ten')
    r=r.json()
    for i in range(0,num):
        print('\n{0}\n{1}\n'.format(r[i]['setup'],r[i]['punchline']))

def insultGenerator():
    r = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    r=r.json()
    print("\n"+r['insult'])

############################################################################################################################################################################################
def numberFact(num):
    r = requests.get('http://numbersapi.com/{}'.format(num))
    print(r.text)

def randomNumberFact():
    r = requests.get('http://numbersapi.com/random/math')
    print(r.text)
    
def randomYearFact():
    r = requests.get('http://numbersapi.com/random/year')
    print(r.text)

def randomDateFact():
    r = requests.get('http://numbersapi.com/random/Date')
    print(r.text)

def randomTriviaFact():
    r = requests.get('http://numbersapi.com/random/trivia')
    print(r.text)


def yearFact(num):
    r = requests.get('http://numbersapi.com/{}/year'.format(num)).text
    print(r)

def dateFact(num1,num2):
    r = requests.get('http://numbersapi.com/{0}/{1}/Date'.format(num1,num2)).text
    print(r)

def triviaFact(num):
    r = requests.get('http://numbersapi.com/{}/trivia'.format(num)).text
    print(r)

############################################################################################################################################################################################
def maxHackerNews():
    max=int(requests.get('https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty').text)
    return max

def idHackerNews(id):
    id=int(id)
    r = requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(id)).json()
    keys=list(r.keys())
    ListLength=len(keys)
    for i in range(0,ListLength):
        print("{0}: {1}".format(keys[i],r[keys[i]]))
        
def top10HackerNews():
    r = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'.format(id)).json()
    print(r[:10])

############################################################################################################################################################################################
def wanted(id):
    response = requests.get('https://api.fbi.gov/wanted/v1/list')
    data = json.loads(response.content)
    
    if id==-1:
        for i in range(0,10):
            print(data['items'][i]['title'])
    else:
        print(data['total'])
        print(data['items'][id]['title'])

############################################################################################################################################################################################
def shortenUrl(url):
    r = requests.get('https://shortlink.api.fayas.me/?query={}'.format(url)).json()
    keys=list(r.keys())
    ListLength=len(keys)
    for i in range(0,ListLength):
        print("{0}: {1}".format(keys[i],r[keys[i]]))

############################################################################################################################################################################################
        
def randomQuotesGOT():
    r = requests.get('https://game-of-thrones-quotes.herokuapp.com/v1/random').json()
    print('{}\n ~{}\n From: {}'.format(r['sentence'],r['character']['name'],r['character']['house']['name']))


def characterQuotesGOT(character):
    r = requests.get('https://game-of-thrones-quotes.herokuapp.com/v1/author/{}'.format(character)).json()
    print('{}\n ~{}\n From: {}'.format(r['sentence'],r['character']['name'],r['character']['house']['name']))
    
############################################################################################################################################################################################
############################################################################################################################################################################################

def menu():
    option=-1
    while option<0 or option>6:
        option=intInput(
              "\n###############################################\n"
              "enter the option you wish to try.\n"
              "*0 to exit the app\n"
              "*1 for Random jokes and insults\n"
              "*2 for some Facts about numbers\n"
              "*3 for Hacking News\n"
              "*4 for FBI wanted criminals \n"
              "*5 to shorten a URL link\n"
              "*6 for some quotes on GOT series\n"
              "###############################################\n"
              "input: ")
    return option

def menuJokes():
    option=-1
    while option<0 or option>4:
        option=intInput(
              "\n###############################################\n"
              "enter the option you wish to try.\n"
              "*0 to exit to the main app\n"
              "*1 for a random Joke \n"
              "*2 for n number of random jokes\n"
              "*3 for a joke containing a word of your choice\n"
              "*4 for an insult\n"
              "###############################################\n"
              "input: ")
    return option

def menuNumbers():
    option=-1
    while option<0 or option>8:
        option=intInput(
              "\n###############################################\n"
              "enter the option you wish to try.\n"
              "*0 to exit to the main app\n"
              "*1 for facts about a random number\n"
              "*2 for some Facts about a specific number\n"
              "*3 for facts about a random Date\n"
              "*4 for some Facts about a specific Date\n"
              "*5 for facts about a random year\n"
              "*6 for some Facts about a specific year\n"
              "*7 for facts about a random trivia\n"
              "*8 for some Facts about a specific trivia\n"
              "###############################################\n"
              "input: ")
    return option

def menuNews():
    option=-1
    while option<0 or option>3:
        option=intInput(
              "\n###############################################\n"
              "enter the option you wish to try.\n"
              "*0 to exit to the main app\n"
              "*1 for the number of total news\n"
              "*2 for the Id of the top 10 news\n"
              "*3 for displaying the news of a specific id\n"
              "###############################################\n"
              "input: ")
    return option

def menuGOT():
    option=-1
    while option<0 or option>2:
        option=intInput(
              "\n###############################################\n"
              "enter the option you wish to try.\n"
              "*0 to exit to the main app\n"
              "*1 for random quotes\n"
              "*2 for a quote from a specific character\n"
              "###############################################\n"
              "input: ")
    return option
############################################################################################################################################################################################
############################################################################################################################################################################################
############################################################################################################################################################################################

while True:
    Option=menu() 
    if Option==0:
        exit()

############################################################################################################################################################################################
    elif Option == 1:
        while True:
            OptionJokes=menuJokes()
            
            if OptionJokes == 0:
                break

            elif OptionJokes ==1:
                randomJoke()

            elif OptionJokes ==2:
                NumOfJokes=intInput("enter the number of jokes you wanna generate: ")
                nRandomJokes(NumOfJokes)

            elif OptionJokes == 3:
                keyword=input("enter a word you want mentioned in the joke: ")
                containsJoke(keyword)

            elif OptionJokes == 4:
                insultGenerator()
############################################################################################################################################################################################
    elif Option == 2:
        while True:
            OptionNumbers=menuNumbers()

            if OptionNumbers == 0:
                break

            elif OptionNumbers == 1:
                randomNumberFact()
                
            elif OptionNumbers == 2:
                FactN=intInput("enter a number and get a random fact about it: ")
                numberFact(FactN)
                
            elif OptionNumbers == 3:
                    randomNumberFact()
                
            elif OptionNumbers == 4:
                FactD1=intInput("enter a date and get a random fact about it, the month: ")
                FactD2=intInput("the day: ")
                dateFact(FactD1,FactD2)
                
            elif OptionNumbers == 5:
                randomYearFact()
                
            elif OptionNumbers == 6:
                FactY=intInput("enter a Year and get a random fact about it: ")
                yearFact(FactY)

            elif OptionNumbers == 7:
                randomTriviaFact()
                
            elif OptionNumbers == 8:
                FactT=intInput("enter a number and get a random trivia fact about it: ")
                triviaFact(FactT)

                
############################################################################################################################################################################################
    elif Option == 3:
        while True:
            OptionNews=menuNews()
            if OptionNews == 0:
                break
            elif OptionNews == 1:
                print(maxHackerNews())

            elif OptionNews == 2:
                top10HackerNews()

            elif OptionNews == 3:
                LastId=str(maxHackerNews())
                text="there are "+LastId+" News about hacking pick any number from 0 to "+LastId+" to read the news: "
                NewsId=intInput(text)               
                idHackerNews(NewsId)
############################################################################################################################################################################################
    elif Option == 4:
        OptionWanted=1
        while True:
            if OptionWanted == 0:
                break
            else:
                PersonId=intInput("enter an id and view what he is wanted for by the FBI: ")
                wanted(PersonId)
                
            OptionWanted=intInput("\n###############################################\n"
                  "*0 to exit to the main app\n"
                  "\n###############################################\n")
############################################################################################################################################################################################
    elif Option == 5:
        OptionUrl=1
        while True:
            if OptionUrl == 0:
                break
            else:
                Url=input("paste a URL to shorten it: ")
                shortenUrl(Url)
            
            OptionUrl=intInput("\n###############################################\n"
                  "*0 to exit to the main app\n"
                  "\n###############################################\n")
############################################################################################################################################################################################
    elif Option == 6:
        while True:
            OptionGOT=menuGOT()
            if OptionGOT == 0 :
                break
            elif OptionGOT == 1 :
                randomQuotesGOT()

            elif OptionGOT == 2 :
                character=input("enter a character's name to lookup a quote: ")
                characterQuotesGOT(character)
############################################################################################################################################################################################    
    else:
        print("an error has occured\n exiting....")
        exit()
