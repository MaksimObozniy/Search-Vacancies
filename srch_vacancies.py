import requests
import os
from dotenv import load_dotenv
from terminaltables import AsciiTable


MOSCOW_ID_HH = 1
MOSCOW_ID_SJ = 4
PER_PAGE_VACANCIES = 100


def calculate_salary(salary_from, salary_to):

    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    if salary_from:
        return salary_from * 1.2
    if salary_to:
        return salary_to * 0.8
    return None


def predict_rub_salary_hh(vacancy):
    salary = vacancy.get("salary")
    if not salary or salary.get("currency") != "RUR":
        return None

    salary_from = salary.get("from")
    salary_to = salary.get("to")

    return calculate_salary(salary_from, salary_to)


def get_hh_vacancies(language):
    url = "https://api.hh.ru/vacancies"
    page = 0
    all_vacancies = []

    while True:
        params = {
            "text": f"Программист {language}",
            "area": MOSCOW_ID_HH,
            "per_page": PER_PAGE_VACANCIES,
            "page": page
        }

        response = requests.get(url, params=params)
        if not response.ok:
            break

        vacancies_response = response.json()
        vacancies = vacancies_response.get("items", [])
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

    return calculate_salary(payment_from, payment_to)


def get_sj_vacancies(language, api_key):
    url = "https://api.superjob.ru/2.0/vacancies/"
    headers = {"X-Api-App-Id": api_key}
    page = 0
    all_vacancies = []

    while True:
        params = {
            "keyword": f"Программист {language}",
            "town": MOSCOW_ID_SJ,
            "count": PER_PAGE_VACANCIES,
            "page": page
        }

        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            break
        
        
        vacancies = response.json()["objects"]
        if not vacancies:
            break

        all_vacancies.extend(vacancies)
        page += 1

    return all_vacancies


def calculate_average_salary(vacancies, platform):
    salaries = []
    
    for vacancy in vacancies:
        if platform == 'hh':
            salary = predict_rub_salary_hh(vacancy)
        elif platform == 'sj':
            salary = predict_rub_salary_sj(vacancy)
        else:
            raise ValueError("Неизвестная платформа")
        
        if salary:
            salaries.append(salary)
        
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
    load_dotenv()
    api_key = os.getenv('SJ_API_KEY') 
    
    languages = ["Python", "Java", "JavaScript"]

    hh_salaries = {}
    for lang in languages:
        hh_vacancies = get_hh_vacancies(lang)
        hh_salaries[lang] = calculate_average_salary(hh_vacancies, "hh")

    sj_salaries = {}
    for lang in languages:
        sj_vacancies = get_sj_vacancies(lang, api_key)
        sj_salaries[lang] = calculate_average_salary(sj_vacancies, "sj")

    print_table("HeadHunter Moscow", hh_salaries)
    print_table("SuperJob Moscow", sj_salaries)
