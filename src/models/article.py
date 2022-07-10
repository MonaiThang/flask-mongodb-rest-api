import mongoengine as me
from datetime import date


class Article(me.Document):
    meta = {'collection': 'articles'}
    id = me.SequenceField(primary_key=True, sequence_name="article_id")
    title = me.StringField(required=True)
    date = me.DateField(default=date.today())
    body = me.StringField()
    tags = me.ListField(me.StringField())

    def to_json(self):
        # convert this document to JSON
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "body": self.body,
            "tags": self.tags
        }
