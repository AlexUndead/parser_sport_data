Конфигурация
------------

1. python = 3.7
2. mysql = 14.14
3. rabbitmq-server 3.6.15


Зависимости
-----------
1. mysqlclient==1.4.6
2. pika==1.1.0
3. SQLAlchemy==1.3.17


Инструкция для запуска приложения
---------------------------------
1. установить все компоненты и зависимости
2. настроить фаил конфигурации config.py
3. добавить файлы которые нужно парсить согласно настроенным путям в файле конфигурации
4. запустить скрипт парсинга, сохранения и добавления в очередь данные о спорте (фаил app_sport.py)
5. запустить скрипт добавления коэффициентов к матчу (фаил app_match.py)

