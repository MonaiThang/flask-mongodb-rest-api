from datetime import date

from src.models.article import Article


def test_article():
    """
    Given: An article model.
    When: A new article is created.
    Then: Check all fields are defined correctly, including counters.
    """
    article = Article(
        title='This is a test article',
        body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare nec urna a malesuada.',
        tags=['test', 'random']
    )
    assert isinstance(article.id, int) is True
    assert article.title == 'This is a test article'
    assert article.body == 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare nec urna a malesuada.'
    assert article.date == date.today()
    assert len(article.tags) == 2
    assert article.tags == ['test', 'random']
