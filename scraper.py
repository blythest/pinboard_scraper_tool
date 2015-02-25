#!/usr/local/bin/python3

import requests
import json
import datetime
from newspaper import Config, Article, Source
import smtplib

PB_USERNAME = "blythest"
PB_PASSWORD = "dPYcpjHQ"
PB_URL = "https://api.pinboard.in/v1/posts/all?format=json"

class Pinboard_Connection:
  def __init__(self):
    self.data = requests.get(PB_URL, auth=(PB_USERNAME, PB_PASSWORD))
    self.links = self.create_pinboard_links()

  def pintime_today():
    today = datetime.date.today()
    format = "%Y-%m-%d"
    return today.strftime(format)

  def create_pinboard_links(self):
    pinboard_json = self.convert_pins_to_json()
    for pin in pinboard_json:
      if '2015-02' in pin['time']:
        yield pin['href']

  def convert_pins_to_json(self):
    pin_articles = ''
    pinboard_json = json.loads(self.data.text)
    return pinboard_json