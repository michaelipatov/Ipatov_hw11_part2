from flask import Flask, render_template
from utils import load_candidates_from_json, path, get_candidate, get_candidates_by_name, \
    get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def head_page():
    candidates_list = load_candidates_from_json(path)
    return render_template('list.html', candidates_list=candidates_list)


@app.route('/candidates/<int:candidate_id>')
def candidates_page(candidate_id):
    url_image, candidate_name, candidate_position, candidate_skills = get_candidate(candidate_id)
    return render_template('card.html', url_image=url_image, candidate_name=candidate_name,
                           candidate_position=candidate_position, candidate_skills=candidate_skills)


@app.route('/search/<candidate_name>')
def search_page(candidate_name):
    name_dict = get_candidates_by_name(candidate_name)
    return render_template('search.html', name_dict=name_dict)


@app.route('/skill/<skill_name>')
def skill_page(skill_name):
    name_by_skill_dict = get_candidates_by_skill(skill_name)
    return render_template('skill.html', name_by_skill_dict=name_by_skill_dict)


app.run()
