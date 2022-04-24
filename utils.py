import json

candidates = []


def get_candidates(path):
    """Получает список кандидатов из json-файла"""
    global candidates
    with open(path, "r", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def get_candidate_id(candidate_id):
    """Выводит кандидата с определенным id"""
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return {
                "name": candidate["name"],
                "position": candidate["position"],
                "picture": candidate["picture"],
                "skills": candidate["skills"]
            }


def get_candidate_skill(candidate_skill):
    """Выводит кандидатов с определенными навыками"""
    result = []

    for candidate in candidates:
        candidate_skills = candidate["skills"].lower().split(", ")

        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)

    return result


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    result = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            result.append(candidate)

    return result


