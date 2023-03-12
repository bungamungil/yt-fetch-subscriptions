from subscription import Subscription


def handle_subscription_item(channel_detail, subscription_item):
    subscription = Subscription()
    subscription.subscription_id = subscription_item['id']
    subscription.user_channel_id = subscription_item['snippet']['channelId']
    subscription.subscription_channel_id = subscription_item['snippet']['resourceId']['channelId']
    subscription.subscription_channel_name = subscription_item['snippet']['title']
    subscription.subscription_since = subscription_item['snippet']['publishedAt']
    subscription.save()
