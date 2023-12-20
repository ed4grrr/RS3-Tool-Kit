import urllib.request

import urllib.error

import UsefulLists


class Player_High_Score_API():

    def __init__(self):
        super()

    def get_player(self,username):
        api_request = urllib.request.Request('https://secure.runescape.com/m=hiscore/index_lite.ws?player=' + username)

        try:
            response = urllib.request.urlopen(api_request)
        except urllib.error.HTTPError as e:
            return f"Unfulfilled Request,\nCode: {e.code}\nReason: {e.reason}"

        except urllib.error.URLError as e:
            return f"Failed to reach Server, \nReason: {e.reason} "

        data = [[int(number) if number != '' else 0 for number in entry.split(",")] for entry in response.read().decode().split("\n")]

        if len(data) == 0:
            return("Invalid Player Name")

        return dict(zip(UsefulLists.USER_LITE_SCORE_API_RESPONSE_ORDER, data))

if __name__ == "__main__":
    api_test = Player_High_Score_API()

    response=api_test.get_player("Deathmunglar")

    print(response)