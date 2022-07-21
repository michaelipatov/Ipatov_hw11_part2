import json
from pathlib import Path

home = Path.home()
path = Path(home, 'PycharmProjects', 'Ipatov_hw11_part2', 'candidates.json')


def load_candidates_from_json(path):
    """Возвращает список всех кандидатов"""
    with open(path, encoding="utf-8") as file:
        candidates_list = json.load(file)
        return candidates_list


candidates_list = load_candidates_from_json(path)


def get_candidate(candidate_id):
    """Возвращает кандидата по его id"""
    url_image = None
    candidate_name = None
    candidate_position = None
    candidate_skills = None
    for candidates_dict in candidates_list:
        if candidates_dict['id'] == candidate_id:
            url_image = candidates_dict['picture']
            candidate_name = candidates_dict['name']
            candidate_position = candidates_dict['position']
            candidate_skills = candidates_dict['skills']
    return url_image, candidate_name, candidate_position, candidate_skills


def get_candidates_by_name(candidate_name):
    """Находит кандидатов по имени и добавляет в словарь name_dict"""
    name_dict = {}
    for candidates_dict in candidates_list:
        if candidate_name in candidates_dict['name']:
            name_dict[candidates_dict['id']] = candidates_dict['name']
    return name_dict


def get_candidates_by_skill(skill_name):
    """Находит кандидатов по навыкам и добавляет в словарь name_by_skill_dict"""
    name_by_skill_dict = {}
    for candidates_dict in candidates_list:
        candidates_skills = candidates_dict['skills'].lower().split(", ")
        if skill_name in candidates_skills:
            name_by_skill_dict[candidates_dict['id']] = candidates_dict['name']
    return name_by_skill_dict
