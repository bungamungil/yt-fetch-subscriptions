from datetime import datetime
from peewee import Model, CharField, DateTimeField
from database import db


class Subscription(Model):
    subscription_id = CharField(index=True)
    user_channel_id = CharField()
    subscription_channel_id = CharField()
    subscription_channel_name = CharField()
    subscription_since = DateTimeField()
    timestamp = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = "subscriptions"
