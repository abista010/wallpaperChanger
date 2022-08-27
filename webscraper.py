from fileinput import filename
import os
import shutil
import ctypes
import requests
from urllib import response
from email.mime import image                    #Needed to mkdir#Needed to download image
from selenium import webdriver

def imageDownloader(url):
    fileName=url.split("/")[-1]
    response=requests.get(url,stream=True)
    if response.status_code==200:
        with open(fileName,'wb') as file:
            shutil.copyfileobj(response.raw,file)
            return(fileName)

def wallpaperChanger(imgName):
    slash="\\"
    imgDir=imagesFolderPath+slash+imgName
    print(imgDir)
    ctypes.windll.user32.SystemParametersInfoW(20,0,imgDir,0)

                 
url='https://apod.nasa.gov/apod/astropix.html'  #NASA APOD website URL
imagesFolderPath=r'C:\Users\ayush\Pictures\NASA APOD images'
driver=webdriver.Edge()                         #Using the Edge Webdriver
driver.get(url)                                 #Launces Edge and goes to "url"

driver.find_element("xpath",'/html/body/center[1]/p[2]/a/img').click()  #Locates the image using XPATH and clicks image
apodUrl=driver.current_url                         #Loads full size image and returns URL
folderName='NASA APOD images'
os.chdir(r'C:\Users\ayush\Pictures')
if not os.path.isdir(folderName):               #Specifying where to place downloaded images
    os.makedirs(folderName)
os.chdir(imagesFolderPath)
wallpaperChanger(imageDownloader(apodUrl))
driver.quit()