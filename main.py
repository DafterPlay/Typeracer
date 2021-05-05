import keyboard
import time
import random
from PIL import ImageGrab, Image
import pytesseract
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def game():
    # Сохраняем картинку
    print("\033[34mНажмите ctrl+alt, когда сохраните картинку в буфер обмена")
    while (not (keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt'))):
        time.sleep(0.001)
    im = ImageGrab.grabclipboard()
    im.save("tmp.png")
    print("\033[32mКартинка сохранена")

    # Обработка и поиск текста
    image = 'tmp.png'
    preprocess = "thresh"
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)

    # Вывод текста в лог
    print("\033[35mНа картинке найден текст: ")
    print("\033[0m" + text)
    print("\033[35mТекст после обработки: ")
    print("\033[0m", end="")
    for i in text:
        for j in i:
            if (j == '|'):
                print("I", end="")
            elif (j == '\n'):
                print(" ", end="")
            elif (j == "’"):
                print('\'', end="")
            elif (j != '[' and j != '\\'):
                print(j, end="")
    print()
    # Печать текста
    time.sleep(1)
    print("\033[34mНажмите ctrl+alt, для печати текста или добавьте shift для отмены")
    while (not (keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt'))):
        time.sleep(0.001)
    if (not keyboard.is_pressed('shift')):
        time.sleep(1)
        for i in text:
            for j in i:
                if (keyboard.is_pressed('shift')):
                    break
                if (j == '|'):
                    keyboard.write("I")
                elif (j == '\n'):
                    keyboard.write(" ")
                elif (j == "’"):
                    keyboard.write('\'')
                elif (j != '[' and j != '\\'):
                    keyboard.write(j)
                x = random.randint(1, 100) / 450
                time.sleep(x)
            if (keyboard.is_pressed('shift')):
                break
        print("\033[32mТекст успешно напечатан!")
    else:
        print("\033[31mПечать отменена!")


while True:
    print("\033[34mНажмите ctrl+alt, для начала.")
    while (not (keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt'))):
        time.sleep(0.001)
    time.sleep(1)
    game()
    time.sleep(1)
    print("\033[34mНажмите ctrl+alt, для повторного запуска или добавьте shift для отмены")
    while (not (keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt'))):
        time.sleep(0.001)
    if keyboard.is_pressed('shift'):
        break
    print(20 * '\n')
    time.sleep(1)
print("\033[31mПрограмма завершена!")
