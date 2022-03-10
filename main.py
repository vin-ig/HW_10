from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def page_index():
    """Главная страница"""
    result = '<pre>'
    for candidate in candidates:  # Выводим общий список кандидатов
        result += f"Имя кандидата: {candidate.get('name')}\nПозиция кандидата: {candidate.get('position')}\n" \
                  f"Навыки: {candidate.get('skills')}\n\n"
    result += '</pre>'

    return result


@app.route('/candidate/<name>')
def page_profile(name):
    """Страница с данными кандидата"""
    flag = False
    result = '<pre>\n'
    for candidate in candidates:
        if name.lower() in candidate.get('name').lower():  # Ищем совпадение по имени
            result += f"<img src='{candidate.get('picture')}'>\n\n" \
                      f"Имя кандидата: {candidate.get('name')}\nПозиция кандидата: {candidate.get('position')}\n" \
                      f"Навыки: {candidate.get('skills')}\n\n"
            flag = True
    if not flag:
        result += 'Кандидат не найден'
    result += '</pre>'

    return result


@app.route('/skill/<skill>')
def page_skill(skill):
    """Поиск кандидата по навыкам"""
    flag = False
    result = '<pre>\n'
    for candidate in candidates:
        if skill.lower() in candidate.get('skills').lower():  # Ищем совпадение по навыкам
            result += f"Имя кандидата: {candidate.get('name')}\nПозиция кандидата: {candidate.get('position')}\n" \
                      f"Навыки: {candidate.get('skills')}\n\n"
            flag = True
    if not flag:
        result += 'Кандидата с такими навыками не найдено'
    result += '</pre>'

    return result


with open('candidates.json', encoding='utf-8') as file:
    candidates = json.load(file)

app.run()
