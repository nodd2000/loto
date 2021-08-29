Правила игры можно скачать тут:

https://drive.google.com/open?id=1bDMcmVfhYaTUw3CB-MV8WtIIXdYEutvX

Количество игроков: 2-8 (можно расширить, изменив `config.MAX_NUM_PLAYERS`)

Тип игроков: компьютер/человек

Тесты:

`python3 -m pytest`

Запуск через Docker (перед сборкой прогоняются тесты):

`docker image build -t loto:latest .`

`docker run -it loto`
