#!/usr/bin/env bash
# Скрипт для сборки проекта на Render

# Установка зависимостей
pip install -r requirements.txt

# Сбор статических файлов
python manage.py collectstatic --no-input

# Применение миграций
python manage.py migrate

# Пункт 5: Создание необходимых файлов для деплоя

1. **Создай файл `build.sh`** в корне проекта:
```bash
#!/usr/bin/env bash
# Скрипт для сборки проекта на Render

# Установка зависимостей
pip install -r requirements.txt

# Сбор статических файлов
python manage.py collectstatic --no-input

# Применение миграций
python manage.py migrate
```