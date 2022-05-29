import random, requests


class Twitch:
    def __init__(self):
        self._token_2 = None
        self.session = requests.session()

        self.getkey()

    def getkey(self):
        _header_v1 = {
            "user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G973N Build/PPR1.190810.011) tv.twitch.android.app/13.0.0/1300000",
        }

        _data_v1 = {
            "bda": "",
            "public_key": "E5554D43-23CC-1982-971D-6A2262A2CA24",
            "site": "https://www.twitch.tv",
            "userbrowser": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G973N Build/PPR1.190810.011) tv.twitch.android.app/13.0.0/1300000",
            "rnd": f'0.{"".join(random.choices("1234567890", k=17))}'
        }

        r = self.session.post('https://client-api.arkoselabs.com/fc/gt2/public_key/E5554D43-23CC-1982-971D-6A2262A2CA24', _data_v1, _header_v1)  # , data=data
        self._token = r.json()["token"] if 'token' in r.text else print(' [ x ] Error getting token'); self._token_2 = r.json()["token"].split('|')[0]

        self.validate()

    def validate(self):
        url = "https://twitch-api.arkoselabs.com/fc/a/"

        querystring = {
            "callback": "fcAnalytic",
            "category": "loaded",
            "action": "game loaded",
            "session_token": self._token_2,
            "r": "eu-west-1",
            "metabgclr": "transparent",
            "guitextcolor": "#000000",
            "lang": "en",
            "pk": "E5554D43-23CC-1982-971D-6A2262A2CA24",
            "at": "40",
            "sup": "1",
            "rid": "42",
            "ag": "101",
            "cdn_url": "https://twitch-api.arkoselabs.com/cdn/fc",
            "lurl": "https://audio-eu-west-1.arkoselabs.com",
            "surl": "https://twitch-api.arkoselabs.com",
            "smurl": "https://twitch-api.arkoselabs.com/cdn/fc/assets/style-manager",
            "data[public_key]": "E5554D43-23CC-1982-971D-6A2262A2CA24",
            "data[site]": "null"
        }

        headers = {
            "host": "twitch-api.arkoselabs.com",
            "connection": "keep-alive",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
            "accept": "*/*",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-dest": "script",
            "referer": "https://twitch-api.arkoselabs.com/v2/E5554D43-23CC-1982-971D-6A2262A2CA24/enforcement.ee270dbcee9ecf648707d27d63315a36.html",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            #"cookie": "timestamp=165373900109175"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.text)

        self.create()

    def create(self):
        import requests

        url = "https://passport.twitch.tv/register"

        passw    = "$}W-3L^_-P*%L)cY"
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=6))
        email    = f"{username}{random.randint(100, 999)}@gmail.com"

        json = {
            "arkose": {
                "token": self._token
            },
            "birthday": {
                "day": 27,
                "month": 4,
                "year": 2000
            },
            "client_id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
            "email": email,
            "include_verification_code": True,
            "password": passw,
            "username": username
        }

        headers = {
                "host": "passport.twitch.tv",
                "connection": "keep-alive",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
                "content-type": "text/plain;charset=UTF-8",
                "accept": "*/*",
                "origin": "https://www.twitch.tv",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.twitch.tv/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
             }

        response = requests.post(url, json=json, headers=headers)

        print(response.text)


Twitch()
