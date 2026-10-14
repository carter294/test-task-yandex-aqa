# Пример проекта автотестов REST API [Яндекс.Диска](https://yandex.ru/dev/disk/rest/)
## Что нужно для запуска

1. Установить зависимости

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Получить OAuth-токен [тут](https://yandex.ru/dev/disk/poligon/)
3. Создать файл .env и вписать в него строку "YANDEX_DISK_TOKEN={токен}"

## Запуск

```bash
pytest -v
```

## Структура

```
├── conftest.py # фикстуры
├── tests/
│   └── test_disk_api.py # тесты
├── requirements.txt
└── README.md
```

