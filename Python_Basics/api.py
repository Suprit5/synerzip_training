# import requests
# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)
# if __name__ == '__main__':
#     speak("")
# def modules():
#     queries={
#         "source":"Tesla news",
#         "sortby":"top",
#         "apikey":"390ca346f5d5490d872d16e1ebf35eae"
#     }
#     url ="https://newsapi.org/v2/everything?q=tesla&from=2021-07-17&sortBy=publishedAt&apiKey=390ca346f5d5490d872d16e1ebf35eae"
#     rada=requests.get(url,params=queries)
#     open_page=rada.json()
#     article=open_page["articles"]
#     result=[]
#     for ar in article:
#         result.append(ar["title"])
#     for i in range(len(result)):
#         print(i+1,result[i])
#     speak(result)
# if __name__ == '__main__':
#     modules()

def calculate():
    array=[3,5,4,-1,0,3]
    for i in array:
        if i > 0 and i%2 != 0:
            print(i)
        else:
            break

calculate()