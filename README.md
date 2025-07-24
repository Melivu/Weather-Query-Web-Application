Это веб-приложение на Django для получения текущей погоды с использованием API OpenWeatherMap и БД PosgreSQL. Приложение позволяет запрашивать погоду по названию города и просматривать историю пользовательских запросов.

Установка:
1) Клонируйте репозиторий: git clone https://github.com/Melivu/Weather-Query-Web-Application.git
2) Установите зависимости: pip install -r requirements.txt
3) Настройте PostgreSQL:
   - Создайте базу данных PostgreSQL.
   - Настройте переменные окружения в файле .env:
      SECRET_KEY=ваш_секретный_ключ
      WEATHER_API_KEY=ваш_ключ_api_openweathermap
      DB_NAME=имя_базы_данных
      DB_USER=пользователь_базы_данных
      DB_PASSWORD=пароль_базы_данных
      DB_HOST=localhost
      DB_PORT=5432
      DEBUG=True
4) Примените миграции: python manage.py migrate
5) Запустите сервер: python manage.py runserver

Использование:
Перейдите на главную страницу (/) для ввода города и получения текущей погоды.
История пользовательских запросов доступна по адресу /history/.
Админ-панель (/admin/) позволяет добавлять города вручную.

