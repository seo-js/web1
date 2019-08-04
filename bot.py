import urllib.repuest as req
import json

baseURL='https://api.telegram.org/bot982668519:AAGz0lvnGgPdKufSPO3Rr4up13EMj2UYEos/'
command="getupdates"
res=req.urlopen('baseURL+commmand')
print(res.read())
