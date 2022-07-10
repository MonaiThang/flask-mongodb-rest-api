from datetime import datetime

from flask import Blueprint, jsonify, make_response, request

from src.models.article import Article


bp_api_tags = Blueprint('api_tags', __name__, url_prefix='/tags')


@bp_api_tags.route('/<tag_name>/<article_date>', methods=['GET'])
def get_tag(tag_name, article_date):
    """
    Get the list of articles that have that tag name on the given date
    and some summary data about that tag for that day.
    :param tag_name: Tag to search.
    :param article_date: Date of the article in YYYY-MM-DD format.
    :return:
    {
        "tag" : "health",
        "count" : 2,
        "articles" : [
            1,
            7
        ],
        "related_tags" : [
            "science",
            "fitness"
        ]
    }
    """
    query_date = datetime.strptime(article_date, '%Y%m%d')

    # query using specified tag and date
    query_results = Article.objects(tags=tag_name, date=query_date).only('id', 'tags')
    list_article = []
    set_tags = set()
    for article in query_results:
        list_article.append(article.id)
        for tag in article.tags:
            if tag not in set_tags and tag != tag_name:
                set_tags.add(tag)

    # construct result object
    return make_response(
        jsonify({
            'tag': tag_name,
            'count': len(query_results),
            'articles': list_article,
            'related_tags': list(set_tags)
        }),
        200)
