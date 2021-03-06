# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Окружение

Python должен быть установлен.

### Зависимости

. Используйте pip для установки зависимостей:

```bash
pip install -r requirements.txt
```

## Запуск

- Скачайте код: [https://github.com/evgeniya35/wine1.git](https://github.com/evgeniya35/wine1.git)
- Запустите сайт командой:
```bash
python main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Как работает

Программа `main.py` создает файл `index.html` из входных данных `wine.xlsx`. 
По умолчанию `main.py` загружает данные `wine.xlsx` из текущего каталога. Для указания другого источника данных, используйте:
```bash
python main.py --wine path/wine.xlsx
```

Пример входных данных:
Категория | Название | Сорт | Цена | Картинка | Акция
------------ | ------------- | ------------- | ------------- | ------------- | -------------
Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png | Выгодное предложение
Напитки | Коньяк классический |  | 350 | konyak_klassicheskyi.png | 
Белые вина | Ркацители | Ркацители | 499 | rkaciteli.png | 
Красные вина | Черный лекарь | Качич | 399 | chernyi_lekar.png | 
Красные вина | Хванчкара | Александраули | 550 | hvanchkara.png | 
Белые вина | Кокур | Кокур | 450 | kokur.png | 
Красные вина | Киндзмараули | Саперави | 550 | kindzmarauli.png | 
Напитки | Чача |  | 299 | chacha.png | Выгодное предложение
Напитки | Коньяк кизиловый |  | 350 | konyak_kizilovyi.png | 
