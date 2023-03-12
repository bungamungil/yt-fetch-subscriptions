import time


def iterate_subscriptions(youtube_api, channel_detail, callback):
    request = youtube_api.subscriptions().list(
        part='snippet,contentDetails',
        mine=True,
        maxResults=50
    )
    while request:
        response = request.execute()
        for item in response.get('items', []):
            callback(channel_detail, item)
        time.sleep(2)
        request = youtube_api.subscriptions().list_next(
            request, response
        )
