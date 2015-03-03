#!/usr/local/bin/python3

import requests
import json
import datetime
from newspaper import Config, Article, Source
import smtplib

PB_USERNAME = "******"
PB_PASSWORD = "*****"
PB_URL = "https://api.pinboard.in/v1/posts/all?format=json"

class Connection:
  def __init__(self):
    self.data = requests.get(PB_URL, auth=(PB_USERNAME, PB_PASSWORD))
    self.links = self.create_pinboard_links()
    self.today = self.pintime_today()

  def pintime_today(self):
    today = datetime.date.today()
    format = "%Y-%m-%d"
    return today.strftime(format)

  def create_pinboard_links(self):
    pinboard_json = self.convert_pins_to_json()
    for pin in pinboard_json:
      if self.pintime_today() in pin['time']:
        yield(pin['href'])

  def convert_pins_to_json(self):
    pin_articles = ''
    pinboard_json = json.loads(self.data.text)
    return pinboard_json

class Articles_Info(Connection):

  def articles(self):
    for link in self.links:
      pin_article = Article(link)
      pin_article.download()
      pin_article.parse()
      yield(pin_article.html)



pinboard_articles = Articles_Info()
for p in pinboard_articles.articles():
  print(p)
