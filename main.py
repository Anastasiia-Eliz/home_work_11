from flask import Flask, render_template

import utils

app = Flask(__name__)

candidates_list = utils.get_candidates("candidates.json")


@app.route("/")
def index_page():
    """Выводит страницу со списком кандидатов и ссылками на их страницы"""
    return render_template('list.html', candidates=candidates_list)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    """Выводит страницу по ссылке на определенного кандидата """
    candidate = utils.get_candidate_id(candidate_id)
    return render_template('card.html', candidate=candidate)

@app.route("/search/<candidate_name>")
def get_names(candidate_name):
    """Выводит страницу с 1 или несколькими кандидатами по имени"""
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, candidates_len=len(candidates))


@app.route("/skills/<skill>")
def get_skills(skill):
    """ Выводит страницу с 1 или несколькими кандидатами по заданному навыку"""
    candidates = utils.get_candidate_skill(skill)
    return render_template('skill.html', candidates=candidates, candidates_len=len(candidates),
                           candidate_skill=skill)


app.run()
