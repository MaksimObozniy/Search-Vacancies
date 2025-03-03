# Search-Vacancies
 
Проект позволяет получать вакансии программистов из API HeadHunter и SuperJob, рассчитывать среднюю зарплату по языкам программирования и выводить результат в виде удобной таблицы.

## Установка

```bash
  git clone https://github.com/MaksimObozniy/Search-Vacancies.git
```

## Установка зависимостей

```bash
  python -m venv .venv
  .venv\Scripts\activate
  pip install -r requirements.txt
```

Убедитесь, что перед установкой зависимостей у вас настроено виртуальное окружение!

## Настройка ключей доступа к API

Для корректной работы скрипта, необходимо получить ключ для получения информации о вакансиях (Ключ можно получить после регистрации приложения, на сайте [SuperJob](https://api.superjob.ru/))

Добавьте новый файл .env в папку с проектом и пропишите в нём переменную ключа:

```.env
  API_KEY=Ваш_ключ
```
Пример:
```example
API_KEY=W4pspq4jifspw4jf9wjya.q8rt993
```
API ключ от SuperJob отличается от примера!

## Запуск скрипта

После выполнения всех требований для запуска скрипта, откройте консольную команду и запустите скрипт:

```bash
python srch_vacancies.py
```

### Результаты скрипта

После завершения скрипта, вы увидете таблицу вакансий, сколько вакансий было найдено по определнному языку программирования, сколько обработано вакансий c hh.ru и SuperJob.ru:

```bash
  +HeadHunter Moscow------+------------------+---------------------+------------------+
  | Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
  +-----------------------+------------------+---------------------+------------------+
  | Python                | 2000             | 422                 | 224502           |
  | Java                  | 1420             | 237                 | 216080           |
  | JavaScript            | 1954             | 662                 | 199613           |
  +-----------------------+------------------+---------------------+------------------+
  +SuperJob Moscow--------+------------------+---------------------+------------------+
  | Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
  +-----------------------+------------------+---------------------+------------------+
  | Python                | 0                | 0                   | 0                |
  | Java                  | 3                | 1                   | 120000           |
  | JavaScript            | 6                | 3                   | 142000           |
  +-----------------------+------------------+---------------------+------------------+
```
