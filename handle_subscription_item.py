def handle_subscription_item(channel_detail, subscription_item):
    print('Subscription %s : %s (https://youtube.com/channel/%s)' % (
        subscription_item['id'],
        subscription_item['snippet']['title'],
        subscription_item['snippet']['resourceId']['channelId']
    ))
