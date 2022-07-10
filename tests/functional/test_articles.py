"""
Functional tests for the `bp_api_articles` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `bp_api_articles` blueprint.
"""
import json


def test_create_valid_article(test_client, init_database):
    """
    Given: A Flask application configured for testing.
    When: The '/articles' endpoint is requested using POST method.
    Then: Check the response is valid.
    """
    body = {
        'title': 'This is a test article',
        'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare nec urna a malesuada.',
        'tags': ['test', 'random']
    }
    response = test_client.post(
        '/api/articles',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(body)
    )
    assert response.status_code == 201


def test_create_invalid_article(test_client, init_database):
    """
    Given: A Flask application configured for testing.
    When: The '/articles' endpoint is requested using POST method.
    Then: Check the response is valid.
    """
    body = {
        'body': 'This should not pass.',
        'tags': ['test', 'random']
    }
    response = test_client.post(
        '/api/articles',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(body)
    )
    assert response.status_code == 400


def test_get_existed_article(test_client, init_database):
    """
    Given: A Flask application configured for testing.
    When: The '/articles/<article_id>' endpoint is requested using GET method.
    Then: Check the response is valid.
    """
    response = test_client.get('/api/articles/3')
    assert response.status_code == 200


def test_get_not_existed_article(test_client, init_database):
    """
    Given: A Flask application configured for testing.
    When: The '/articles/<article_id>' endpoint is requested using GET method.
    Then: Check the response is valid.
    """
    response = test_client.get('/api/articles/555')
    assert response.status_code == 404
