"""
Functional tests for the `bp_api_tags` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `bp_api_tags` blueprint.
"""


def test_get_tags_info(test_client, init_database):
    """
    Given: A Flask application configured for testing.
    When: The '/tags/<tag_name>/<article_date>' endpoint is requested using GET method.
    Then: Check the response is valid.
    """
    response = test_client.get('/api/tags/health/20220710',)
    json_response = response.json
    assert response.status_code == 200
    assert json_response['tag'] == 'health'
    assert json_response['count'] == 3
    assert json_response['articles'] == [4, 5, 6]
    assert json_response['related_tags'].sort() == [
        "Australia",
        "health services",
        "national",
        "Kim Jong Un",
        "North Korea",
        "world",
        "politics",
        "coronavirus",
        "disease",
        "vaccine",
        "COVID 19",
        "drugs"
    ].sort()


def test_get_tags_not_exist(test_client, init_database):
    """
    Given: A Flask application configured for testing.
    When: The '/tags/<tag_name>/<article_date>' endpoint is requested using GET method.
    Then: Check the response is valid. Expected result:
    {
        "articles": [],
        "count": 0,
        "related_tags": [],
        "tag": "abc"
    }
    """
    response = test_client.get('/api/tags/abc/20220710',)
    json_response = response.json
    assert response.status_code == 200
    assert json_response['tag'] == 'abc'
    assert json_response['count'] == 0
    assert json_response['articles'] == []
    assert json_response['related_tags'] == []


def test_get_tags_no_article(test_client, init_database):
    """
    Given: A Flask application configured for testing.
    When: The '/tags/<tag_name>/<article_date>' endpoint is requested using GET method.
    Then: Check the response is valid. Expected result:
    {
        "articles": [],
        "count": 0,
        "related_tags": [],
        "tag": "health"
    }
    """
    response = test_client.get('/api/tags/health/20000710',)
    json_response = response.json
    assert response.status_code == 200
    assert json_response['tag'] == 'health'
    assert json_response['count'] == 0
    assert json_response['articles'] == []
    assert json_response['related_tags'] == []