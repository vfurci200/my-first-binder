#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:06:59 2020

@author: vince
"""
# def scraper(flight_number,date):
import requests
import json
import datetime
import pandas as pd
from bs4 import BeautifulSoup

myfile = open("./output/boardingpic.txt","rt") 
contents = myfile.read()         # read the entire file to string
myfile.close()                   # close the file

mylines = []                              # Declare an empty list
with open ("./output/boardingpic.txt","rt") as myfile:  # Open l.txt for reading text.
    for line in myfile:                   # For each line of text,
        mylines.append(line)              # add that line to the list.
    for element in mylines:    
        # if element.find("FR") == 1:         # For each element in the list,
        print(element, end='')                   # print it.               # print string contents
        


flight_number = 'FR1455'
date = '18 Oct 2020'
time = ''
# myProxy = {"http"  : "http://10.120.118.49:8080", "https"  : "https://10.120.118.49:8080"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0"}

s = requests.session()
response = s.get('https://www.flightradar24.com/data/flights/' + flight_number, headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')


class flight:
    date = None
    dep_city = None
    dest_city = None
    std = None
    atd = None
    sta = None
    status = None

flights = []

divs = soup.findAll("tr", {"class": "data-row"})


j=-1
for div in divs:
    row = ''
    rows = div.findAll('td')
    i=1
    for row in rows:
        # if(row.text.find("PHONE") > -1):
        # print(i)
        if i == 3:
            j=j+1
            flights.append(flight())
            flights[j].date = row.text[1:-1]
        elif i==4:
            flights[j].dep_city = row.text
        elif i==5:
            flights[j].dest_city   = row.text
        elif i==8:
            flights[j].std   = row.text
        elif i==9:
            flights[j].atd  = row.text
        elif i==10:
            flights[j].sta  = row.text
        elif i==12:
            flights[j].status   = row.text
        # print(row.text)
        i=i+1
        # if j>-1:
        #     print(flights[j].date)

for Flight in flights:
    if Flight.date == date:
        if Flight.status.find("Landed")>0:
            print(Flight.status)
            time = Flight.status[-6:]
            print(time)

# return time
