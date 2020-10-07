# lib_lesson
Проек для обучения django
## Подготовка к запуску
1. Необходимо в корень проекта добавить файд `.secret.env` 
1. Добавить в файл `.secret.env` строку: `SECKRET_KEY=<seckret key>`, где вместо `<seckret key>` вставить любой свой ключь (или сгенерировать его через онлайн сервисы)
## Запуск в локальном окружении
1. `docker-compose build`
1. `docker-compose up`
## Запуск в прод окружении
1. В settings.py установить DEBUG=False
1. `docker-compose -f docker-compose.stage.yml build`
1. `docker-compose -f docker-compose.stage.yml up`
