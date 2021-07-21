# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:34:14 2021

@author: hosam
"""

import requests
from datetime import date
import time
import json
from selenium import webdriver

# header={'Host': 'cdn-api.co-vin.in',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
# 'Accept': 'application/json, text/plain, */*',
# 'Accept-Language': 'en-US,en;q=0.5',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Origin': 'https://www.cowin.gov.in',
# 'Connection': 'keep-alive',
# 'Referer': 'https://www.cowin.gov.in/',
# 'If-None-Match': 'W/"8fd-4e0NuSYNIexiJv20OxdTje106xQ"',
# 'TE': 'Trailers'
# }
#Function which receives the Telegram chat ID and district code and message is sent to telegram channel for 18-44 and capacity is not zero
def fetch_data(c,channelID,alreadySent):
    try:
    
        url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(c)+"&date="+date.today().strftime("%d-%m-%Y")
        # a=requests.get(url, headers=header).json()["centers"]
        
        driver.get(url)
        pre = driver.find_element_by_tag_name("pre").text
        a=json.loads(pre)       
        for x in a['centers']:
            for y in x["sessions"]:
                if y["min_age_limit"]==18 and y["available_capacity"]>2 and y["date"]=='13-05-2021':
                    out="Name of the Hospital:"+str(x["name"])+"\nDistrict Name:"+str(x["district_name"])+"\nPincode:"+str(x["pincode"])+"\nCapacity:"+str(y["available_capacity"])+"\nVaccine:"+str(y["vaccine"])+"\nDate:"+str(y["date"])+"\n"+x["fee_type"]+"\n\n\nBook slots in https://selfregistration.cowin.gov.in/"
                    sent=[x["name"],x["district_name"], x["pincode"], y["vaccine"],y["date"]]
                    
                    
                    
                    if sent not in alreadySent:
                        requests.post("https://api.telegram.org/bot1732618443:AAHPI29hCULVLh9rCxEv6cOXieWGaMXyb8o/sendMessage?chat_id="+channelID+"&text="+out)
                        print(out)
                        alreadySent.append(sent)
                    
        return alreadySent
                    
    except json.decoder.JSONDecodeError:
        print("Retrying")
        time.sleep(30)
    
        
driver=webdriver.Chrome('C:\\Users\hosam\Documents\Project\CoWin\chromedriver.exe')
numberOfRuns=0
alreadySent=[['GGH Shorapur', 'Yadgir', 585224, 'COVISHIELD', '13-05-2021'],
 ['GGH Shorapur', 'Yadgir', 585224, 'COVISHIELD', '14-05-2021'],
 ['GGH Shorapur', 'Yadgir', 585224, 'COVISHIELD', '15-05-2021'],
 ['GGH Shorapur', 'Yadgir', 585224, 'COVISHIELD', '16-05-2021'],
 ['GGH Shorapur', 'Yadgir', 585224, 'COVISHIELD', '17-05-2021'],
 ['GGH Shorapur', 'Yadgir', 585224, 'COVISHIELD', '18-05-2021'],
 ['Old District Hospital Yadgir',
  'Yadgir',
  585201,
  'COVISHIELD',
  '13-05-2021'],
 ['Old District Hospital Yadgir',
  'Yadgir',
  585201,
  'COVISHIELD',
  '14-05-2021'],
 ['Old District Hospital Yadgir',
  'Yadgir',
  585201,
  'COVISHIELD',
  '15-05-2021'],
 ['Old District Hospital Yadgir',
  'Yadgir',
  585201,
  'COVISHIELD',
  '16-05-2021'],
 ['Old District Hospital Yadgir',
  'Yadgir',
  585201,
  'COVISHIELD',
  '17-05-2021'],
 ['Old District Hospital Yadgir',
  'Yadgir',
  585201,
  'COVISHIELD',
  '18-05-2021'],
 ['GGH Shahapur', 'Yadgir', 585223, 'COVISHIELD', '13-05-2021'],
 ['GGH Shahapur', 'Yadgir', 585223, 'COVISHIELD', '14-05-2021'],
 ['GGH Shahapur', 'Yadgir', 585223, 'COVISHIELD', '15-05-2021'],
 ['GGH Shahapur', 'Yadgir', 585223, 'COVISHIELD', '16-05-2021'],
 ['New District Hospital Yadgir',
  'Yadgir',
  585202,
  'COVISHIELD',
  '13-05-2021'],
 ['New District Hospital Yadgir',
  'Yadgir',
  585202,
  'COVISHIELD',
  '14-05-2021'],
 ['New District Hospital Yadgir',
  'Yadgir',
  585202,
  'COVISHIELD',
  '16-05-2021'],
 ['New District Hospital Yadgir',
  'Yadgir',
  585202,
  'COVISHIELD',
  '17-05-2021'],
 ['New District Hospital Yadgir',
  'Yadgir',
  585202,
  'COVISHIELD',
  '18-05-2021'],
 ['HONNALI TH COVISHIELD', 'Davanagere', 577217, 'COVISHIELD', '13-05-2021'],
 ['Jagalur TH COVISHIELD', 'Davanagere', 577528, 'COVISHIELD', '13-05-2021'],
 ['DH Koppal 18 Plus', 'Koppal', 583231, 'COVISHIELD', '14-05-2021'],
 ['CHIGATERI COVISHIELD', 'Davanagere', 577004, 'COVISHIELD', '13-05-2021'],
 ['New District Hospital Yadgir',
  'Yadgir',
  585202,
  'COVISHIELD',
  '15-05-2021'],
 ['CHIGATERI COVISHIELD', 'Davanagere', 577004, 'COVISHIELD', '14-05-2021'],
 ['HUMNABAD GH CVC', 'Bidar', 585330, 'COVISHIELD', '14-05-2021'],
 ['Tiptur TH', 'Tumkur', 572201, 'COVISHIELD', '13-05-2021'],
 ['Krishnarajapet TH', 'Mandya', 571426, 'COVISHIELD', '13-05-2021'],
 ['Maddur TH', 'Mandya', 571428, 'COVISHIELD', '13-05-2021'],
 ['Malavalli TH', 'Mandya', 571430, 'COVISHIELD', '13-05-2021'],
 ['Srirangapatana TH', 'Mandya', 571438, 'COVISHIELD', '13-05-2021'],
 ['Pandavapura TH', 'Mandya', 571434, 'COVISHIELD', '13-05-2021'],
 ['Chincholi TH CVC', 'Gulbarga', 585307, 'COVISHIELD', '15-05-2021'],
 ['Sidlaghatta TH', 'Chikkaballapur', 562105, 'COVISHIELD', '15-05-2021'],
 ['Bowring Hospital Covishield 18',
  'BBMP',
  560001,
  'COVISHIELD',
  '14-05-2021'],
 ['GGH Shorapur', 'Yadgir', 585224, 'COVISHIELD', '19-05-2021'],
 ['GGH Shahapur', 'Yadgir', 585223, 'COVISHIELD', '19-05-2021'],
 ['Old District Hospital Yadgir',
  'Yadgir',
  585201,
  'COVISHIELD',
  '19-05-2021'],
 ['New District Hospital Yadgir',
  'Yadgir',
  585202,
  'COVISHIELD',
  '19-05-2021']]
while True:
    numberOfRuns+=1 
    data={"-1001377841541":[265, 276, 294],"-1001193151300":[267, 272, 274, 284, 282, 285], "-1001214506031":[270, 264, 278, 280, 279, 293], "-1001318151983":[273, 289, 283],  "-1001425888973":[269, 286, 281], "-1001259097648":[271, 291, 268, 277, 290, 266, 292, 288, 275], '-504177321':[7, 13] }
    #"-1001259097648":[271, 291, 268, 275, 277, 290, 266, 292, 288], Coastal  "-1001425888973":[269, 286, 281] 
    #Conpleted South Karnataka'-1001259097648"': need to check, "-1001318151983":287
    #not working 275 in south karnataka
    for channelID,districtCode in data.items():
        numberOfRuns+=1
        print(numberOfRuns)
        if type(districtCode)=="int":
            alreadySent=fetch_data(districtCode,channelID,alreadySent)
        else:
            for e in districtCode:
                alreadySent=fetch_data(e, channelID,alreadySent)
    time.sleep(120)
    
