#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool


f=open("movies.txt","r")
g = f.read().splitlines()
g = filter(None, g)
g=set(g)

f.close()

def newfindurl(name):
    try:
        name = name.replace(" ","%20")
        urla="http://www.imdb.com/find?q="+str(name)+"&s=tt&ttype=ft"
        ra = requests.get(urla)
        soup = BeautifulSoup(ra.text, "html.parser")
        tag = soup.find("td", {"class": "result_text"})
        print(str(tag.a["href"]))
        return str(tag.a["href"])
    except:
        print(name)


with Pool(8) as p:
    records = p.map(newfindurl, g)

url = "http://www.imdb.com"

for i in range(len(records)):
    records[i]=url+records[i]



def runtime(soup):
    try:
        tag = soup.find("time", {"itemprop": "duration"})
        return str(tag.string).replace("\n","").strip()
    except:
        return("data not available")

def ratings(soup):
    try:
        tag = soup.find("span", {"itemprop": "ratingValue"})
        if tag:
            return str(tag.string)
    except:
        return("data not available")

def title(soup):
    try:
        tag = soup.find("h1", {"itemprop": "name"})
        return tag.contents[0][:-1]
    except:
        return("data not available")

def genre(soup):
    try:
        tag = soup.findAll("span", {"itemprop": "genre"})
        text=""
        for i in tag:
            text = text + str(i.string) + " ,"
        return text[:-2]
    except:
        return("data not available")

def contentRating(soup):
    try:
        tag = soup.find("meta", {"itemprop": "contentRating"})
        return str(tag["content"])
    except TypeError:
        return ('Data not availabe')

def releaseDate(soup):
    try:
        tag = soup.find("a", {"title": "See more release dates"})
        return tag.contents[0][:-1]
    except:
        return("data not available")


def mai(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    data = [title(soup),ratings(soup),runtime(soup),genre(soup),contentRating(soup),releaseDate(soup)]
    print(data)
    return data

with Pool(8) as p:
    final = p.map(mai, records)

print(final)
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

for i, l in enumerate(final):
    for j, col in enumerate(l):
        sheet1.write(i, j, col)
book.save("imdbdata.xls")
