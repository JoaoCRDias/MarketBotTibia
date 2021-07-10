import pyautogui
from PIL import ImageGrab, Image
import glob
import math
import cv2
import numpy as np

def openMarket():
  screenshot = ImageGrab.grab()

  marketImage = Image.open('package\images\market.png')
  marketCoords = pyautogui.locate(marketImage, screenshot)
  if(marketCoords == None):
    print('Não foi possivel abrir o market, programa finalizado')
    exit()
  else:
    pyautogui.rightClick((marketCoords.left + marketCoords.width/2), (marketCoords.top + marketCoords.height/2))

def configureCoords():
  screenshot = ImageGrab.grab()
  retorno = dict()
  for val in glob.glob('package\images\*.png'):
    dictProp = val.split('\\')
    if(dictProp[len(dictProp)-1] == 'firstOffert.png'):
      image = Image.open(val)
      coords = pyautogui.locateAllOnScreen(image)
      i = 0
      for pos in coords:
        print(pos)
        if(i == 0):
          retorno['firstOffertSell'] = {
            'left': (pos.left + (pos.width/2)),
            'top': (pos.top + (pos.height/2)),
            'width': (pos.left + pos.width),
            'height': (pos.top + pos.height)
          }
        if(i == 1):
          retorno['firstOffertBuy'] = {
            'left': (pos.left + (pos.width/2)),
            'top': (pos.top + (pos.height/2)),
            'width': (pos.left + pos.width),
            'height': (pos.top + pos.height)
          }
    if(dictProp[len(dictProp)-1] != 'market.png'):
      image = Image.open(val)
      coords = pyautogui.locate(image, screenshot)
      retorno[dictProp[len(dictProp)-1].split('.')[0]] = {'left': math.ceil(coords.left + coords.width/2), 'top': math.ceil(coords.top + coords.height/2)}
    
  return retorno



