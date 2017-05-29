import os
data=[]
for root, dirs, files in os.walk(".", topdown=False):
    if "venv" in root.split("/"):
        continue
    for name in files:
        if name=="venv":
            continue
        data.append(name)

movies=[]
for movie in data:
    if movie.split(".")[-1] in ["mkv","mp4","avi"]:
        movies.append(movie)

def finder(name):
    replace = ["m-HD",".avi","1.4","fmovies to","5.1","-","m-HD","Chromium","{+18}","DVDRip","BRRip","XviD","1CDRip","aXXo","[","]","(",")","{","}","{{","}}"
    "x264","720p","StyLishSaLH (StyLish Release)","DvDScr","MP3","HDRip","WebRip","CHROMIUM","m-HD","fmovies",
    "ETRG","YIFY","StyLishSaLH","StyLish Release","TrippleAudio","EngHindiIndonesian","disc 1","disc 2","disc 3","disc 4"
    "385MB","CooL GuY","a2zRG","x264","Hindi","AAC","AC3","MP3"," R6","HDRip","H264","ESub","AQOS",
    "ALLiANCE","UNRATED","ExtraTorrentRG","BrRip","mkv","mpg","DiAMOND","UsaBitcom","AMIABLE",
    "BRRIP","XVID","AbSurdiTy","DVDRiP","TASTE","BluRay","HR","COCAIN","_",".","BestDivX","MAXSPEED",
    "Eng","500MB","FXG","Ac3","Feel","Subs","S4A","BDRip","FTW","Xvid","Noir","1337x","ReVoTT",
    "GlowGaze","mp4","Unrated","hdrip","ARCHiViST","TheWretched","www","torrentfive","com",
    "1080p","1080","SecretMyth","Kingdom","Release","RISES","DvDrip","ViP3R","RISES","BiDA","READNFO",
    "HELLRAZ0R","tots","BeStDivX","UsaBit","FASM","NeroZ","576p","LiMiTED","Series","ExtraTorrent","DVDRIP","~",
    "BRRiP","699MB","700MB","greenbud","B89","480p","AMX","007","DVDrip","h264","phrax","ENG","TODE","LiNE",
    "XVid","sC0rp","PTpower","OSCARS","DXVA","MXMG","3LT0N","TiTAN","4PlayHD","HQ","HDRiP","MoH","MP4","BadMeetsEvil",
    "XViD","3Li","PTpOWeR","3D","HSBS","CC","RiPS","WEBRip","R5","PSiG","'GokU61","GB","GokU61","NL","EE","Rel","NL",
    "PSEUDO","DVD","Rip","NeRoZ","EXTENDED","DVDScr","xvid","WarrLord","SCREAM","MERRY","XMAS","iMB","7o9",
    "Exclusive","171","DiDee","v2","SaMple","Blu","Ray","Dual","Audio","English","+","Mafiaking","lish","SAMPLE",
    "By","Mx","HDDR","YIFY","PSK","chromium","WEB","DL","HD","DrC","bitloks","080p","201","x265","MgB","Sample",
    "DTS","BRrip","GAZ","CH","DD","Ch","PyZ","Agent47","CyBorG","SaMpLe","BHATTI87","Chromium","Sample",
    "aac","vice","CyBorG","F! @$H","Director Cut","Director","PROPER","TehMovies Com","TehMovies","WarLord","Half SBS","SBS",
    "Bia2Movies","ray","EmEm","EVOYoungSkywalker","ShAaNiG","WEBRiP","by Trigger","FardaDownload ir","Hive CM8",
    "Scr","Dir Cut","muxed","JYK","WEB DL","UnRated","Khiladi786","RARBG","RiP","X264","MA","HC","MKV"

    ]

    year=0
    for y in range(1900,2018):
        if str(y) in name:
            name = name.replace(str(y)," ")
            year = y
            break

    for value in replace:
        name = name.replace(value," ")

    name = name.strip()
    return name

final=[]
for i in movies:
    final.append(finder(i))

to_be_removed = {"disc 2","disc 1","disc 3","disc 4"}
final=[item for item in final if item not in to_be_removed ]




g=open("text1.txt","w")
g.write(str("\n".join(final)))
g.close()
