Содержание.

[Установка]#Установка

[Запуск]#Запуск

[Структура]#Cтруктура

[Примеры]#Примеры


#Установка
1. Необходим Python 3.10 или старше.
2. Клонировать репозиторий https://github.com/Bassist666/homework_twiter.git
3. Установить зависимости 'pip install -r requirements.txt'
4. Установить программу Postman.


#Запуск
1. Запуск проекта осуществляется командой 'python main.py'

#Структура

homework_twiter/
├── main.py
├── model/
│ ├── Twit.py
│ └── User.py
├── requirements.txt
└── README.md

#Примеры

Примеры выполнены в программе Postman.

1. Метод GET #Возвращает все созданные твиты

   Запрос http://127.0.0.1:5000/twits

   Ответ {"twits": []}

3. Метод POST #Создает новый твит

   Запрос http://127.0.0.1:5000/twits    

   Тело {"body": "text_twit", "author": "author_name"}

   Ответ {"status": "sucessfully created"}

5. Метод DELETE #Удаляет твит с номером <twit_num>

   Запрос http://127.0.0.1:5000/twits/<twit_num> #Вставить номер твита вместо <twit_num>

   Ответ {"status": "sucessfully deleted"}
