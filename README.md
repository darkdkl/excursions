###  Проект: Куда пойти —  в Москве

Демо вариант : 
http://darkdmake.pythonanywhere.com/

##### Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей: 

```
pip3 install -r requirements.txt
```
##### Настройка
Создайте .env в каталоге с приложением со следующим содержимым.
```
SECRET_KEY = 'ваш secret key'
DEBUG = False (для продакшена и true для разработки)
```
Для создания директории /static/ в корне проекта выполните:
```
python3 manage.py collectstatic
```
В директорию json_data_to_load поместите файлы *.json
для заполнения базы данными.
Json файлы можно получить перейдя по ссылке : https://github.com/devmanorg/where-to-go-places/tree/master/places

Пример структуры json файлов:
```
{
    "title": "Останкинская телебашня",
    "imgs": [
        "https://domain.com/image.jpg",
    ],
    "description_short": "краткое описание",
    "description_long": "полное описание с html тегами разметки",
    "coordinates": {
        "lng": "долгота",
        "lat": "широта"
    }
}
```
Заполните базу данными выполнив команду
```
python3 manage.py load_place
```
####Запуск
для запуска на локальном компьютере выполните
```
python3 manage.py runserver
```
Тестовые данные взяты с сайта [KudaGo](https://kudago.com).



######Dark Dmake, 2020