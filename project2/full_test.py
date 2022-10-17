from google_nlp_test import analyze_text_sentiment
from twitter_api_test import search

def city_sentiment(city):
    try:
        tweet = search(city)
    except:
        print("Cannot get tweets")
        return 0
    sco = 0
    mag= 0
    n = 0
    for tt in tweet:
        try:
            i,m = analyze_text_sentiment(tt.text)
        except:
            print("Cannot connect to Google")
            return 0
        if m< 0.2:
            continue
        else:
            sco += i
            mag += abs(i)
            n += 1
    #print(mag/n)
    #print(sco/n)
    if sco>0:
        print("People feel positive about"+city,end='.')

    else:
        print("People feel positive about" + city, end='.')
    print('The sentiment score is ' + str("%.2f" % sco))

city_sentiment('Boston')