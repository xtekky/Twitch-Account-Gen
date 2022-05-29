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
        # print(_token, '\n', _token_2)

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


        #payload = '{\"username\":\"cziecbieeub333\",\"password\":\"azer321!33!!\",\"email\":\"birxxkusultu@vusra.com\",\"birthday\":{\"day\":4,\"month\":7,\"year\":2000},\"client_id\":\"kimne78kx3ncx6brgo4mv6wki5h1ko\",\"arkose\":{\"token\":\"736292100d403d39.0839892905|r=eu-west-1|metabgclr=transparent|guitextcolor=%23000000|lang=en|pk=E5554D43-23CC-1982-971D-6A2262A2CA24|at=40|sup=1|rid=42|ag=101|cdn_url=https%3A%2F%2Ftwitch-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-eu-west-1.arkoselabs.com|surl=https%3A%2F%2Ftwitch-api.arkoselabs.com|smurl=https%3A%2F%2Ftwitch-api.arkoselabs.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager\"}}'

        passw = "$}W-3L^_-P*%L)cY"
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=6))
        email = f"{username}{random.randint(100, 999)}@gmail.com"

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
            #"cookie": "unique_id=oIRxcb1tupIdbenSa6sPChHxyWIL1tgF; unique_id_durable=oIRxcb1tupIdbenSa6sPChHxyWIL1tgF; twitch.lohp.countryCode=FR; experiment_overrides={%22experiments%22:{}%2C%22disabled%22:[]}; spare_key=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3Bhc3Nwb3J0LnR3aXRjaC50diIsInN1YiI6IltcIjc5NzgxNDI0M1wiXSIsImF1ZCI6ImJydXRlLWZvcmNlLXByb3RlY3Rpb24iLCJleHAiOjE2NjkyOTExMTksImlhdCI6MTY1MzczOTExOSwibm9uY2UiOiJoM1YxbXUtNHdOQW5qRzlULWcxR2Z5UnBGSElnR2Q0d3dMd19fVnA0cXVnPSJ9.HVPagFYyuuAfLViVAObhlILT9hW9oWrKknYuBRrV7rHtIIGl_8JGGX553IaqR2mim7_7pN0uoJ0OXPf7B6Bqvg%3D%3D; last_login=2022-05-28T11:58:39Z; server_session_id=8f70abfb5bd14a56a3ee069d404ef155; api_token=twilight.2cb22833a262d2117487be586841109d"
        }

        response = requests.post(url, json=json, headers=headers)

        print(response.text)


Twitch()
