import requests
from bs4 import  BeautifulSoup
import csv
date=input("please enter a data in the following format MM/DD/YYYY")
page=requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")
def main(page):
    src=page.content
    soup=BeautifulSoup(src,"lxml")
    match_details=[]
    championships=soup.find_all("div",{'class':'matchCard'})
    
    def get_match_info(championships):
        championship_title=championships.contents[1].find("h2").text.strip()
        all_matches=championships.contents[3].find_all("li")
        number_of_match=len(all_matches)
        for i in range(number_of_match):
            #get tiams
            teamA=all_matches[0].find("div",{'class':'teamA'}).text.strip()
            teamB=all_matches[0].find("div",{'class':'teamB'}).text.strip()
            #get match score
            res_match=all_matches[0].find("div",{'class':'MResult'}).find_all("span",{'class':'score'})
            score=f"{res_match[0].text.strip()}-{res_match[1].text.strip()}"
            #get match time
            time_of_match=res_match=all_matches[0].find("div",{'class':'MResult'}).find("span",{'class':'time'}).text.strip()
            match_details.append({"أسم البطولة":championship_title,"الفريق الأول":teamA,"الفريق الثاني":teamB,"ميعاد المباراة":time_of_match,"النتيجة":score})
           
    for i in range(len(championships)):
        get_match_info(championships[i])
    keys=match_details[0].keys()
    with open('C:/Users/ThinkPad/Desktop/yalashoot/match_details.csv','w', encoding='utf-8') as output_file:
        dic_writer = csv.DictWriter(output_file, keys)
        dic_writer.writeheader()
        dic_writer.writerows(match_details)
        print("File created ")

main(page)