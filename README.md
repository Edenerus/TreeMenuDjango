# AsyncAPI

    Это приложение характеризует древовидное меню

___

## Бэкенд-функционал:

- Админ-панель, в которой можно добавлять Меню и его Элементы
- Отображение Меню и возможность переходить по элементам

___

## Стэк:

![Python3.10](https://img.shields.io/badge/-Python3.10-blue)
![Django](https://img.shields.io/badge/-Django-blue)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-blue)
![Docker](https://img.shields.io/badge/-Docker-blue)

___

## Запуск:

1) Клонируйте репозиторий
`git clone https://github.com/Edenerus/TreeMenuDjango`.
2) Переименуйте файл `.env.example` в `.env` и заполните его значениями
3) Создайте и запустите докер-образ командой `docker-compose up --build -d`
4) После создания контейнеров, протестировать функционал вы сможете с помощью ссылок:
    - http://localhost:80/admin/ - для входа в админку и создания Меню со статикой. Используйте \
    Username: admin \
    Password: admin \
    чтобы войти в админку (она создается автоматически).
    - http://localhost:8000/menu/ - для просмотра списка Меню. После вам развернется это меню и вы сможете просмотреть элементы внутри меню

___

## Авторы

- Ключников Кирилл. https://github.com/Edenerus
