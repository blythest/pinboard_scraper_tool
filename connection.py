import yaml
import json
import requests

class Connection:
  def __init__(self):
    self.connected = self.__is_connected__()
    self.data = self.__get_json_data__()

  def __secret__(self):
    user_info = (yaml.load(open('secret.yaml','r')))
    creds = {"url":user_info['PB_URL'], "pw":user_info['PB_PASSWORD'], "user":user_info['PB_USERNAME']}
    return(creds)

  def __is_connected__(self):
    creds = self.__secret__()
    data = requests.get(creds['url'], auth=(creds['user'], creds['pw']))
    if data:
      return(data)
    else:
      return("<Response [400]> Error.")

  def __get_json_data__(self):
    data = self.__is_connected__()
    pinboard_json = json.loads(data.text)
    return(pinboard_json)