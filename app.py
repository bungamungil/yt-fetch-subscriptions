import argparse

from googleapiclient.errors import HttpError

import fetch_user_credential as auth
from errors import ChannelDetailNotFound, LastBroadcastNotFound
from fetch_channel_detail import fetch_channel_detail
from iterate_subscriptions import iterate_subscriptions
from handle_subscription_item import handle_subscription_item

parser = argparse.ArgumentParser()
parser.add_argument('--credential', '-c', help='Use credential file')
args = parser.parse_args()


# Main function
if __name__ == '__main__':
    arg_credential = args.credential
    youtube_api = auth.fetch_user_credential(arg_credential)
    try:
        channel_details = fetch_channel_detail(youtube_api)
        if len(channel_details) > 0:
            channel_detail = channel_details[0]
            iterate_subscriptions(youtube_api, channel_detail, handle_subscription_item)
        else:
            raise ChannelDetailNotFound
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    except ChannelDetailNotFound:
        print("Channel detail not found")
    except LastBroadcastNotFound:
        print("Last broadcast not found")
