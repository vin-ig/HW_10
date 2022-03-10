from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def page_index():
    result = '<pre>'
    for candidate in candidates:
        result += f"Имя кандидата: {candidate.get('name')}\nПозиция кандидата: {candidate.get('position')}\n" \
                  f"Навыки: {candidate.get('skills')}\n\n"
    result += '</pre>'
    return result


@app.route('/candidate/<name>')
def page_profile(name):
    result = '<pre>\n'
    for candidate in candidates:
        if candidate.get('name').lower() == name.lower():
            result += f"<img src='{candidate.get('picture')}'>\n\n" \
                      f"Имя кандидата: {candidate.get('name')}\nПозиция кандидата: {candidate.get('position')}\n" \
                      f"Навыки: {candidate.get('skills')}\n\n"
            break
    else:
        result += 'Кандидат не найден'
    result += '</pre>'
    return result


@app.route('/skill/<skill>')
def page_skill(skill):
    flag = False
    result = '<pre>\n'
    for candidate in candidates:
        skills = [elem.lower() for elem in candidate.get('skills').split(', ')]
        if skill.lower() in skills:
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
