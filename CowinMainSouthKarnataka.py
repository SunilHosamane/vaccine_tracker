# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:23:31 2021

@author: hosam
"""

import json
from selenium import webdriver
token="1732618443:AAHPI29hCULVLh9rCxEv6cOXieWGaMXyb8o"
b=[301, 307, 306, 297, 295, 298, 304, 305, 302, 308, 300, 296, 303, 299, 270, 276, 265, 294, 264, 274, 272, 271, 273, 291, 268, 269, 275, 278, 280, 267, 289, 279, 283, 277, 282, 290, 266, 284, 292, 287, 288, 286, 281, 293, 285, 9, 10, 11, 5, 4, 7, 12, 13, 14, 8, 15, 16, 6, 582, 583, 581, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 612, 597, 598, 613, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 779, 555, 578, 565, 571, 778, 539, 547, 566, 556, 563, 552, 557, 544, 559, 780, 562, 540, 576, 558, 577, 564, 573, 570, 575, 546, 781, 545, 561, 580, 551, 541, 569, 554, 560, 548, 550, 568, 572, 553, 574, 543, 542, 549]
driver = webdriver.Chrome('C:\\Users\hosam\Documents\Project\CoWin\chromedriver.exe')
        
for c in b:
    try:
        url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(c)+"&date=09-05-2021"
        driver.get(url)
        pre = driver.find_element_by_tag_name("pre").text
        a=json.loads(pre)
        for x in a['centers']:
            for y in x["sessions"]:
                if y["min_age_limit"]==18:
                    if y["available_capacity"]!=0:
                        out="Name of the Hospital:"+str(x["name"])+"\nDistrict Name="+str(x["district_name"])+"\nPincode="+str(x["pincode"])+"\nCapacity="+str(y["available_capacity"])+"\nVaccine="+str(y["vaccine"])+"\nDate="+str(y["date"])+"\n"+x["fee_type"]
                        print(out)  
    except json.decoder.JSONDecodeError:
        print("Retrying")