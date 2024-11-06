<p align="center">
<img src="https://img.shields.io/badge/made%20by-Dafter-orange.svg">
<img src="https://img.shields.io/github/license/DafterT/Typeracer">
<img src="https://img.shields.io/badge/3.11-_?label=python">
<img src="https://img.shields.io/badge/2021-_?label=Year&color=pink">
</p>

# Typeracer
Данная программа создана для автоматического решения задач на скорость с сайта [play.typeracer.com](play.typeracer.com) путем парсинга данных со скриншота и последующей имитацией ввода с клавиатуры.
# Библиотеки
Для работы необходима библиотека `Pillow` и `OpenCV`, для работы с картинками, а также `pytesseract`, который позволяет считать с картинки английские буквы и преобразовать их в строку `Python`. Также для печати используется модуль `keyboard`.

Для работы pytesseract необходимо указать путь к Tesseract-OCR. Это необходимо сделать в коде, в строке:
```python
pytesseract.pytesseract.tesseract_cmd = "Path_to_tesseract/Tesseract-OCR/tesseract.exe"
```
Прямая ссылка на инсталлятор tesseract на windows: [Установка](https://kumisystems.dl.sourceforge.net/project/tesseract-ocr-alt/tesseract-ocr-setup-3.02.02.exe?viasf=1)