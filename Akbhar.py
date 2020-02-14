# Akhbarr padke sunaao
# install "pywin32" module

import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == "__main__":
    # speak("Hello How Are You")
    key = "b77c29cd4a8d4c80b292a01e20bb80c4"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={key}"

    import requests
    news = requests.get(url).text

    news_json = json.loads(news)
    print("Status : ",news_json['status'])
    # print(new_json)
    print(type(news_json))
    
    for k,v in news_json.items():
        print(f"key :{k} ")
        
    print(type(news_json['articles']) )  

    
    # for i in range(0,1):
    #     speak(news_json['articles'][i]['title'])
    
    
    for i in news_json['articles']:
        print(i['title'])
        speak(i['title'])
        speak("Moving to the Next news..")

    speak("Thanks for listening")    