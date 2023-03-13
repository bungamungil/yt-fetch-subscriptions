def delete_subscription(youtube_api, subscription_id):
    return youtube_api.subscriptions().delete(
        id=subscription_id
    ).execute()
