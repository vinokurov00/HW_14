from flask import Flask, jsonify
from utils import get_picture_by_title, get_picture_by_years, get_picture_by_rating, get_picture_by_genre


app = Flask(__name__)
app.config['app.json.ensure_ascii'] = False


@app.route("/movie/<title>/")
def picture_page(title):
    result = get_picture_by_title(title)
    return jsonify(result)


@app.route("/movie/<int:year1>/to/<int:year2>/")
def pictures_by_years_page(year1, year2):
    result = get_picture_by_years(year1, year2)
    return jsonify(result)


@app.route("/rating/<rating>/")
def pictures_by_rating_page(rating):
    result = get_picture_by_rating(rating)
    return jsonify(result)


@app.route("/genre/<genre>/")
def pictures_by_genre_page(genre):
    result = get_picture_by_genre(genre)
    return jsonify(result)


if __name__ == "__main__":
    app.run()