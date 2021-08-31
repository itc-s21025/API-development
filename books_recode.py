import requests
import datetime

#google books api からデータを入手
url = 'https://www.googleapis.com/books/v1/volumes?q=intitle:'
maxresults = '&maxresults=3'
now = datetime.datetime.now()
recode = now.year,now.month,now.day

#入手したデータからほしいいデータを抽出
def main(title):
    req_url = url + title + maxresults
    response = requests.get(req_url).json()['items']
    res1 = response[0]
    bookname = res1['volumeInfo']['title']
    authors = res1['volumeInfo']['authors']
    description = res1['volumeInfo']['description']
    image = res1['volumeInfo']['imageLinks']['smallThumbnail']
    result = [' ', str(recode), '作品名: ' + str(bookname), '著者: ' + str(authors), '概要: ' + str(description), '画像リンク: ' + str(image), ' ',]
    
    return '\n'.join(result)

#入手したデータを保存する関数
def keep(title_input, thoughts):
    print(main(title_input), file=f) 
    print("<簡単な感想>",file=f)
    print(thoughts, file=f)
    return "記録しました"

if __name__=="__main__":
        title_input = input("本のタイトルを入力してください: ")
        print(main(title_input))

if __name__=="__main__":
    thoughts = input("簡単な感想を書いてください: ") 
    with open('recode.txt', 'a') as f:
        print(keep(title_input, thoughts))
