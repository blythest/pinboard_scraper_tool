#!/usr/local/bin/python3
import datetime
from newspaper import Config, Article, Source

class Pin_Article():

  def pintime_interval(self):
    today = datetime.date.today()
    format = "%Y-%m-%d"
    return today.strftime(format)

  def __links__(self):
    pinboard_json = Connection().data
    for pin in pinboard_json:
      if self.pintime_interval() in pin['time']:
        yield(pin['href'])

  def __all_text__(self):
    for link in self.__links__():
      pin_article = Article(link)
      pin_article.download()
      pin_article.parse()
      yield(pin_article.text)


if __name__== "__main__":

  from connection import Connection

  pins = Pin_Article()
  for article in pins.__all_text__():
    print(article)