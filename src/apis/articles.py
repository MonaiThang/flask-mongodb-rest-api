from flask import Blueprint, jsonify, make_response, request

from src.models.article import Article


bp_api_articles = Blueprint('api_articles', __name__, url_prefix='/articles')


@bp_api_articles.route('', methods=['POST'])
def create_article():
    """
    Insert an article into the database. Its ID will be generated automatically as sequence.
    Example request body:
    {
        "title": "Sri Lanka protesters set fire to PM Wickremesinghe's official residence hours after thousands storm presidential residence",
        "date" : "2022-07-10'
        "body" : "Thousands of protesters, angered by Sri Lanka's worst economic crisis in 70 years, have stormed the president's house, office. Many blame the country's decline on Mr Rajapaksa, and are demanding his resignation. At least 39 people, including two police officers have been injured and hospitalised in the protests",
        "tags" : ["Sri Lanka", "world", "protests"]
    }
    If date is not specified, the current datetime will be used.
    :return: Results with HTTP response code
    """
    content = request.json
    if 'title' not in content.keys():
        return make_response(jsonify(message="title is required"), 400)
    article = Article(
        title=content['title'],
        date=content['date'] if 'date' in content.keys() else None,
        body=content['body'] if 'body' in content.keys() else None,
        tags=content['tags'] if 'tags' in content.keys() else None
    )
    article.save()
    return make_response(jsonify(message='Article created'), 201)


@bp_api_articles.route('/<article_id>', methods=['GET'])
def get_article(article_id):
    """
    Get the article details by its ID.
    :param article_id: Article ID in integer format. This should match the id field in collection.
    :return: the JSON representation of the article.
    """
    article_obj = Article.objects(id=int(article_id)).first()
    if article_obj:
        return make_response(jsonify(article_obj.to_json()), 200)
    else:
        return make_response(jsonify(message='Article ID not exist'), 404)
