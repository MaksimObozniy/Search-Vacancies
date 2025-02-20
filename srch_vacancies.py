import requests
import os
from terminaltables import AsciiTable



API_KEY = os.getenv('API_KEY') 


def predict_rub_salary_hh(vacancy):
    salary = vacancy.get("salary")
    if not salary or salary.get("currency") != "RUR":
        return None

    salary_from = salary.get("from")
    salary_to = salary.get("to")

    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    if salary_from:
        return salary_from * 1.2
    if salary_to:
        return salary_to * 0.8

    return None


def get_hh_vacancies(language):
    url = "https://api.hh.ru/vacancies"
    page = 0
    all_vacancies = []

    while True:
        params = {
            "text": f"Программист {language}",
            "area": 1,
            "per_page": 100,
            "page": page
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            break

        vacancies = response.json().get("items", [])
        all_vacancies.extend(vacancies)

        if page >= response.json()["pages"] - 1:
            break

        page += 1

    return all_vacancies


def predict_rub_salary_sj(vacancy):
    payment_from = vacancy.get("payment_from")
    payment_to = vacancy.get("payment_to")
    currency = vacancy.get("currency")

    if currency != "rub":
        return None

    if payment_from and payment_to:
        return (payment_from + payment_to) / 2
    if payment_from:
        return payment_from * 1.2
    if payment_to:
        return payment_to * 0.8

    return None


def get_sj_vacancies(language):
    url = "https://api.superjob.ru/2.0/vacancies/"
    headers = {"X-Api-App-Id": API_KEY}
    page = 0
    all_vacancies = []

    while True:
        params = {
            "keyword": f"Программист {language}",
            "town": 4,
            "count": 100,
            "page": page
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            break

        vacancies = response.json()["objects"]
        if not vacancies:
            break

        all_vacancies.extend(vacancies)
        page += 1

    return all_vacancies


def calculate_average_salary(language, vacancies, salary_func):
    salaries = [salary_func(vacancy) for vacancy in vacancies if salary_func(vacancy)]
    average_salary = int(sum(salaries) / len(salaries)) if salaries else 0

    return {
        "vacancies_found": len(vacancies),
        "vacancies_processed": len(salaries),
        "average_salary": average_salary
    }


def print_table(title, results):
    table_data = [
        ["Язык программирования", "Вакансий найдено", "Вакансий обработано", "Средняя зарплата"]
    ]

    for language, stats in results.items():
        table_data.append([
            language,
            stats["vacancies_found"],
            stats["vacancies_processed"],
            stats["average_salary"]
        ])

    table = AsciiTable(table_data, title)
    print(table.table)


if __name__ == '__main__':
    languages = ["Python", "Java", "JavaScript"]

    hh_results = {lang: calculate_average_salary(lang, get_hh_vacancies(lang), predict_rub_salary_hh) for lang in languages}
    sj_results = {lang: calculate_average_salary(lang, get_sj_vacancies(lang), predict_rub_salary_sj) for lang in languages}

    print_table("HeadHunter Moscow", hh_results)
    print_table("SuperJob Moscow", sj_results)
