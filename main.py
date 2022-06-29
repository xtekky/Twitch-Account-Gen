import requests, random, time, threading, json; from colorama import Fore, init

init(convert=True)

class Generator:
    def __init__(self, config_file, proxy_file, site_key, page_url):
        self.config           = json.load(open(config_file, 'r'))
        
        self.session          = requests.session()
        self.cap_service_key  = self.config["2captcha_key"]
        self.threads          = int(self.config["threads"])
        self.bio              = self.config["bio_text"]
        self.password         = self.config["password"]
        
        self.site_key         = site_key
        self.page_url         = page_url

        self.proxies          = open(proxy_file, 'r').read().splitlines()
        
        self.errors           = 0
        self.retries          = 0
        self.sucess           = 0
    
    def starter(self):
        while True:
            if threading.active_count() < self.threads:
                threading.Thread(target=self.get_captcha).start()
                
    def title(self):
        pass

    def get_captcha(self):
        
        _start = time.time()
        get_task = requests.get(
                url = f"https://2captcha.com/in.php",
                params = {
                    "key": self.cap_service_key,
                    "method": "funcaptcha",
                    "publickey": self.site_key,
                    "pageurl": self.page_url
                }
            )
        task_id = get_task.text.split("|")[1]
        print(f' New captcha task [{task_id}]')
        
        time.sleep(2.8)
        
        twocap_response = requests.get(
            url = f"https://2captcha.com/res.php",
            params = {
                    "key": self.cap_service_key,
                    "action": "get",
                    "id": task_id,
                }
            )

        while "CAPCHA_NOT_READY" in twocap_response.text:
            time.sleep(1.6)
            twocap_response = requests.get(
            url = f"https://2captcha.com/res.php",
            params = {
                    "key": self.cap_service_key,
                    "action": "get",
                    "id": task_id,
                }
            )
        captcha_response = twocap_response.text[3:]
        print(f' Captcha solved: [{task_id}] token: [{captcha_response.split("|")[0]}] time: {round(time.time() - _start)}s')
        self.gen_account(captcha_response)

    def gen_account(self, captcha_token):
        try:

            random_day   = random.randint(1,30)
            random_month = random.randint(1,12)
            email        = "".join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8)) + "@gmail.com"
            username     = f"{random.choices('abcdefghijklmnopqrstuvwxyz', k=4)}_onlp"

            prox = random.choice(self.proxies)

            r = requests.post(
                url = "https://passport.twitch.tv/register", 
                json = {
                    "username": username,
                    "password": self.password,
                    "email": email,
                    "birthday":
                        {
                            "day":random_day,
                            "month":random_month,
                            "year":2000
                            },
                    "client_id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
                    "arkose":
                        {
                            "token":captcha_token
                            }
                }, 
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
                }, 
                proxies = {
                    'http': f'http://{prox}',
                    'https':f'http://{prox}'
                }
            )
            

            if "You are trying to sign up for accounts too fast." in r.text:
                print(Fore.LIGHTRED_EX + 'You Are Being Rate Limited')

            elif "Please complete the CAPTCHA correctly." in r.text:
                print(Fore.LIGHTRED_EX + 'Captcha Solved Incorrectly')

            elif "access_token" in r.text:
                token = r.json()["access_token"]
                user_id = r.json()["userID"]

                bio_req = requests.post(
                        url = "https://gql.twitch.tv/gql", 
                        headers = {
                            "Connection": "keep-alive",
                            "Pragma": "no-cache",
                            "Cache-Control": "no-cache",
                            "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                            "Accept-Language": "pl-PL",
                            "sec-ch-ua-mobile": "?0",
                            "Client-Version": "e8881750-cfb7-4ff7-aaae-132abb1e8259",
                            "Authorization": f"OAuth {token}",
                            "Content-Type": "text/plain;charset=UTF-8",
                            "User-agent": f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
                            "Client-Session-Id": "671362f9f83b6729",
                            "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
                            "X-Device-Id": "O1MrFLwPyZ2byJzoLFT0K5XNlORNRQ9F",
                            "sec-ch-ua-platform": '"Windows"',
                            "Accept": "*/*","Origin": "https://dashboard.twitch.tv",
                            "Sec-Fetch-Site": "same-site",
                            "Sec-Fetch-Mode": "cors",
                            "Sec-Fetch-Dest": "empty",
                            "Referer": "https://dashboard.twitch.tv/",
                        }, 
                        json = [
                            {
                                "operationName": "UpdateUserProfile",
                                "variables": {
                                    "input": 
                                        {
                                            "displayName": username, 
                                            "description":self.bio,
                                            "userID": user_id
                                            }
                                        },
                                "extensions": 
                                    {
                                        "persistedQuery": 
                                            {
                                                "version": 1,
                                                "sha256Hash": "991718a69ef28e681c33f7e1b26cf4a33a2a100d0c7cf26fbff4e2c0a26d15f2"
                                                }
                                            }
                                    }
                        ],
                        proxies = {
                            'http': f'http://{prox}',
                            'https':f'http://{prox}'
                        }
                    )
                
                with open('./output/raw_tucans.txt','a+') as _:
                    _.write(f"{token}\n")

                with open('./output/tucans.txt','a+') as _:
                    _.write(f"{username}:{self.password}:{token}\n")
                
                print(Fore.GREEN + f"Generated | {Fore.RESET}{token}\n")
        except Exception as e:
            print(f'An error occured [{e}]')


if __name__ == '__main__':
    gen = Generator(
            config_file = './input/config.json',
            proxy_file  = './input/proxies.txt',
            site_key = "E5554D43-23CC-1982-971D-6A2262A2CA24",
            page_url = "https://www.twitch.tv/"
        )
    
    gen.starter()
