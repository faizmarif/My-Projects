import csv

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  

name=input("Input name of person: ")
query = name + " twitter"
  
for j in search(query, tld="co.in", num=10,stop=1):
    handle=j
    
from bs4 import BeautifulSoup
import requests

temp = requests.get(handle)
bs = BeautifulSoup(temp.text,'lxml')
try:
    follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of followers: {} ".format(followers.get('data-count')))
    
    following_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--following'})
    following = following_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("{} is following {} people.".format(name,following.get('data-count')))
    
    favorite_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--favorites'})
    favorite = favorite_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of post {}  liked are {}: ".format(name,favorite.get('data-count')))
    
    tweet_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--tweets is-active'})
    tweets= tweet_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("{} tweets {} number of tweets.".format(name,tweets.get('data-count')))
    
    ctr = int(input('Input number of tweets to scrape: '))
    all_tweets = bs.find_all('div',{'class':'tweet'})
    if all_tweets:
        for tweet in all_tweets[:ctr]:
            context = tweet.find('div',{'class':'context'}).text.replace("\n"," ").strip()
            content = tweet.find('div',{'class':'content'})
            header = content.find('div',{'class':'stream-item-header'})
            user = header.find('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
            time = header.find('a',{'class':'tweet-timestamp js-permalink js-nav js-tooltip'}).find('span').text.replace("\n"," ").strip()
            message = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
            footer = content.find('div',{'class':'stream-item-footer'})
            stat = footer.find('div',{'class':'ProfileTweet-actionCountList u-hiddenVisually'}).text.replace("\n"," ").strip()
            if context:
                print(context)
            print(user,time)
            print(message)
            print(stat)
            print()
            
            
            with open('tweet.csv','w') as f:
                thewriter=csv.writer(f)
                
                thewriter.writerow([name])
                thewriter.writerow(['followers','followings','liked','tweets'])
                thewriter.writerow([followers.get('data-count'),following.get('data-count'),favorite.get('data-count'),tweets.get('data-count')])
            
            
            
    else:
        print("List is empty/account name not found.")

except:
    print('Account name not found...')
    
