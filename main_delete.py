import argparse
import time

import fetch_user_credential as auth
from subscription import Subscription
from delete_subscription import delete_subscription

parser = argparse.ArgumentParser()
parser.add_argument('--credential', '-c', help='Use credential file')
args = parser.parse_args()


# Main function
if __name__ == '__main__':
    arg_credential = args.credential
    youtube_api = auth.fetch_user_credential(arg_credential)
    subscriptions = [subscription for subscription in Subscription.select()]
    for subscription in subscriptions:
        delete_subscription(youtube_api, subscription.subscription_id)
        subscription.delete_instance()
        print("Delete subscription for %s" % subscription.subscription_channel_name)
        time.sleep(2)
