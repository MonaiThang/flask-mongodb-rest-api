from datetime import date

import pytest

from src import create_app, db
from src.models.article import Article


@pytest.fixture(scope='module')
def new_article():
    article = Article(
        title='This is a test article',
        body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare nec urna a malesuada.',
        tags=['test', 'random']
    )
    return article


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.py')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Insert user data
    article1 = Article(
        title='latest science shows that potato chips are better for you than sugar',
        date=date(year=2016, month=9, day=22),
        body='some text, potentially containing simple markup about how potato chips are great',
        tags=['health', 'fitness', 'science']
    )
    article2 = Article(
        title='Sri Lanka protesters set fire to PM Wickremesinghe\'s official residence hours after thousands storm '
              'presidential residence',
        date=date(year=2022, month=7, day=10),
        body='Thousands of protesters, angered by Sri Lanka\'s worst economic crisis in 70 years, have stormed the '
             'president\'s house, office. Many blame the country\'s decline on Mr Rajapaksa, and are demanding his '
             'resignation. At least 39 people, including two police officers have been injured and hospitalised in '
             'the protests',
        tags=["Sri Lanka", "world", "protests"]
    )
    article3 = Article(
        title="Elon Musk says he's terminating $63 billion Twitter buyout deal",
        date=date(year=2022, month=7, day=10),
        body="Mr Musk said Twitter had \"not complied with its contractual obligations\" surrounding the deal. Shares "
             "of Twitter fell 5 per cent on Friday. In April, Mr Musk became the company's largest shareholder after "
             "acquiring a 9 per cent stake.",
        tags=["Elon Musk", "world", "twitter", "money", "social media", "business", "finance"]
    )
    article4 = Article(
        title="Australians aged over 30 now eligible for a fourth COVID-19 vaccine dose",
        date=date(year=2022, month=7, day=10),
        body="Australians aged 30 and over are now eligible to receive a fourth COVID-19 vaccine dose from next week "
             "following advice from the Australian Technical Advisory Group on Immunisation (ATAGI). From July 11 "
             "ATAGI has recommended that people aged 50 to 64 years old should receive a fourth dose, while people "
             "aged 30 to 49 years old may choose to have a fourth dose.",
        tags=["COVID 19", "coronavirus", "Australia", "disease", "health", "vaccine"]
    )
    article5 = Article(
        title="COVID-19 antiviral treatments to become available to more Australians",
        date=date(year=2022, month=7, day=10),
        body="Known as Lagevrio and Paxlovid, the drugs cost $6.80 for a concession card holder and around $40 for "
             "others. The health minister says anyone interested in the treatment should speak to their GP. Treatment "
             "needs to begin as soon as possible after symptoms appear",
        tags=["COVID 19", "coronavirus", "Australia", "health", "drugs", "health services", "national"]
    )
    article6 = Article(
        title="Is North Korea hiding a bigger problem behind its COVID-19 outbreak?",
        date=date(year=2022, month=7, day=10),
        body="Choi Jung-hun smiled as I read out the latest official COVID-19 figures from North Korean state media: "
             "fewer than 5 million cases of \"fever\" and just 73 fatalities - a fraction of the death toll of every "
             "other country in the world. \"North Koreans call them rubber band statistics,\" he said, "
             "in a nod toward Pyongyang's flexibility with the truth. \"It's hard even for North Korea to know its "
             "own numbers.\"",
        tags=["COVID 19", "coronavirus", "North Korea", "health", "Kim Jong Un", "world", "politics", "national"]
    )
    article1.save()
    article2.save()
    article3.save()
    article4.save()
    article5.save()
    article6.save()
    yield  # this is where the testing happens!

    # cleanup test database
    db.connection.drop_database('test')
