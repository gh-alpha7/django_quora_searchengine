from bs4 import BeautifulSoup
import requests
import webbrowser
from selenium import webdriver

def f(ques):
    string="https://www.google.co.in/search?q=quora"+ques
    r=requests.get(string)
    soup=BeautifulSoup(r.content,'lxml')
    cite=soup.find_all('cite')
    ans=cite[0].text
    return ans



