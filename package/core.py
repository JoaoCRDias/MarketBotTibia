import pytesseract
import cv2
import pyautogui
import datetime
import numpy as np
from PIL import ImageGrab
from package.rastreamentoDeImagens import openMarket
from package.rastreamentoDeImagens import configureCoords
from package.items import getItems, Item

coordenadas = None


def coreInit():
  openMarket()
  configureCoords()
  # try:
  #   global coordenadas
  #   coordenadas = configureCoords()
  # except:
  #   print("Não foi possivel configurar as coordenadas, o programa será finalizado")
  #   exit() 
  # for item in getItems():
  #   print(item.nome)
  #   checkitem(item)
  #   pyautogui.sleep(1)
  #   lertela()
  
  # lertela()
  # if((((str(lertela.valestoque)) != '0') and (lertela.valcompra > 45000))):
  #    pass
  # else:
  #    comprar()
  # if(((str(lertela.valestoque)) == '0')):
  #    pass
  # else:
  #    vender()



# report.close()

# f = open('CurrentValues.txt', 'r+')
# f.truncate(0)


# dt = datetime.date.today()
# dt = datetime.datetime(dt.year, dt.month, dt.day)
# print(dt)
# dt = str(dt)

contadorgeral = 0

def checkitem(item):
  print(item)
  print('Nome dessa merda ', item.nome)
  pyautogui.leftClick(coordenadas['clearSearchBar']['left'], coordenadas['clearSearchBar']['top'])
  pyautogui.leftClick(coordenadas['searchBar']['left'], coordenadas['searchBar']['top'])
  pyautogui.typewrite(item.nome, interval=0.005)
  pyautogui.leftClick(coordenadas['searchResultList']['left'], coordenadas['searchResultList']['top'])
  pyautogui.sleep(1.5)

  print('O item avaliado agora é o: ' + item.nome)
  print('Venderei quando acima de: ' + str(item.tetoVenda) + 'gps')
  print('Comprarei quando abaixo de: ' + str(item.tetoCompra) + 'gps')
  print('---')

def lertela():
    report = open('CurrentValues.txt', 'a')
    # -| Bloco de captura das ofertas |-#
    imagecompra = ImageGrab.grab(bbox=(405, 372, 485, 385))
    imagevenda = ImageGrab.grab(bbox=(410, 190, 485, 205))
    imageestoque = ImageGrab.grab(bbox=(380, 330, 421, 350))

    # # -| Movimentação para leitura de histórico do item |-#
    # pyautogui.leftClick(561, 621)
    # pyautogui.sleep(1.5)
    # histcompra = ImageGrab.grab(bbox=(385, 355, 425, 367))
    # histvenda = ImageGrab.grab(bbox=(385, 420, 425, 432))
    # pyautogui.leftClick(481, 624)

    # -| DEBUGGER - Visualização da captura de tela |-#
    cv2.imshow("Imagecompra", np.array(imagecompra))
    cv2.imshow("Imagevenda", np.array(imagevenda))
    cv2.imshow("Imageestoque", np.array(imageestoque))
    # cv2.imshow("histcompra", np.array(histcompra))
    # cv2.imshow("histvenda", np.array(histvenda))
    cv2.waitKey(0)

    # txtcompra = pytesseract.image_to_string(imagecompra, lang='tibia',
    #                                         config='--psm 7 -c tessedit_char_whitelist=0123456789,')
    # txtvenda = pytesseract.image_to_string(imagevenda, lang='tibia',
    #                                        config='--psm 7 -c tessedit_char_whitelist=0123456789,')
    # textestoque = pytesseract.image_to_string(imageestoque, lang='tibia',
    #                                           config='--psm 7 -c tessedit_char_whitelist=0123456789,')
    # texthistcompra = pytesseract.image_to_string(histcompra, lang='tibia',
    #                                              config='--psm 7 -c tessedit_char_whitelist=0123456789,')
    # texthistvenda = pytesseract.image_to_string(histvenda, lang='tibia',
    #                                             config='--psm 7 -c tessedit_char_whitelist=0123456789,')

    # # -| Tratamento e transformação da leitura para número inteiro |-#
    # txtcompra = txtcompra.replace('\n', '')
    # txtcompra = txtcompra.replace('\f', '')
    # txtcompra = txtcompra.replace(',', '')
    # txtcompra = txtcompra.replace(' ', '')
    # if ((txtcompra) == ('')):
    #     txtcompra = 00
    # txtcompra = int(txtcompra)

    # # -| Tratamento e transformação da leitura para número inteiro |-#
    # txtvenda = txtvenda.replace('\n', '')
    # txtvenda = txtvenda.replace('\f', '')
    # txtvenda = txtvenda.replace(',', '')
    # txtvenda = txtvenda.replace(' ', '')
    # if ((txtvenda) == ('')):
    #     txtvenda = 00
    # txtvenda = int(txtvenda)

    # # -| Tratamento e transformação da leitura para número inteiro |-#
    # textestoque = textestoque.replace('\n', '')
    # textestoque = textestoque.replace('\f', '')
    # textestoque = textestoque.replace(',', '')
    # textestoque = textestoque.replace(' ', '')
    # if ((textestoque) == ('')):
    #     textestoque = 00
    # txtestoque = int(textestoque)

    # # -| Tratamento e transformação da leitura para número inteiro |-#
    # texthistcompra = texthistcompra.replace('\n', '')
    # texthistcompra = texthistcompra.replace('\f', '')
    # texthistcompra = texthistcompra.replace(',', '')
    # texthistcompra = texthistcompra.replace(' ', '')
    # if ((texthistcompra) == ('')):
    #     texthistcompra = 00
    # texthistcompra = int(texthistcompra)

    # # -| Tratamento e transformação da leitura para número inteiro |-#
    # texthistvenda = texthistvenda.replace('\n', '')
    # texthistvenda = texthistvenda.replace('\f', '')
    # texthistvenda = texthistvenda.replace(',', '')
    # texthistvenda = texthistvenda.replace(' ', '')
    # if ((texthistvenda) == ('')):
    #     texthistvenda = 00
    # texthistvenda = int(texthistvenda)

    # report.write((itens[i].name) + ';' + str(txtvenda) + ';' + str(txtcompra) + ';' + str(texthistcompra) + ';' + str(texthistvenda) + '\n')

    # # -| Impressão do valor de compra |-#
    # print("Compra: " + (str(txtcompra)))
    # print("Venda: " + (str(txtvenda)))
    # print("Estoque: " + (str(textestoque)))
    # print("Qtd comprado: " + (str(texthistcompra)))
    # print("Qtd vendido: " + (str(texthistvenda)))
    # if ((txtvenda)==00 and (txtcompra)==00):
    #     #print('Oferta situacional!')
    #     lertela.valvenda = int(txtvenda)-1
    #     lertela.valcompra = int(txtcompra)+1
    #     lertela.valestoque = str(txtestoque)
    # else:
    #     #print('A diferença total entre eles é de:', textvenda - textcompra)
    #     lertela.valvenda = int(txtvenda)
    #     lertela.valcompra = int(txtcompra)
    #     lertela.valestoque = str(textestoque)

def comprar():
    i = int(contadorgeral)
    teto = int(itens[i].tetoCompra)
    if((lertela.valcompra)<=(teto*10)):
        pyautogui.leftClick(219, 537)
        pyautogui.leftClick(487, 558)
        comprando = str((lertela.valcompra)+1)
        pyautogui.typewrite(''+(comprando), interval=0.05)
        if((lertela.valcompra)<=10000):
            pyautogui.keyDown('Shift')
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.keyUp('Shift')
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(735, 579)
        elif((lertela.valcompra)>10000 and (lertela.valcompra)<=30000):
            pyautogui.keyDown('Shift')
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.keyUp('Shift')
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(735, 579)
        elif((lertela.valcompra)>30000 and (lertela.valcompra)<=40000):
             pyautogui.keyDown('Shift')
             pyautogui.PAUSE = 0.05
             pyautogui.leftClick(540, 537)
             pyautogui.keyUp('Shift')
             pyautogui.PAUSE = 0.05
             pyautogui.leftClick(735, 579)
        elif((lertela.valcompra)>40000):
           #pyautogui.leftClick(540, 537)
           pyautogui.leftClick(735, 579)
    elif():
        pass

def vender():
    i = int(contadorgeral)
    teto = int(itens[i].tetoVenda)
    if((lertela.valvenda) > (10)):
        pyautogui.leftClick(230, 522)
        pyautogui.leftClick(487, 558)
        vendendo = str((lertela.valvenda) -1)
        pyautogui.typewrite('' + (vendendo), interval=0.05)
        pyautogui.keyDown('Shift')
        pyautogui.keyDown('Ctrl')
        pyautogui.PAUSE = 0.05
        pyautogui.leftClick(545, 534)
        pyautogui.PAUSE = 0.05
        pyautogui.keyUp('Shift')
        pyautogui.keyUp('Ctrl')
        pyautogui.PAUSE = 0.05
        pyautogui.keyUp('Shift')
        pyautogui.leftClick(545, 534)
        pyautogui.leftClick(735, 579)
    else:
        pass
