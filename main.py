import requests, json, random

session = requests.Session()



header_v1 = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-us",
        #"client-id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
        "connection": "Keep-Alive",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "host": "client-api.arkoselabs.com",
        "origin": None,
        "user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G973N Build/PPR1.190810.011) tv.twitch.android.app/13.0.0/1300000",
        "x-requested-with": "tv.twitch.android.app"
    }

#data = 'bda=eyJjdCI6Iis1V0lZTzVTcGZCRUF1QmFnMTZjZFNYUlRBOTIrdjBxTkgyZjFJNkh2UU9OS0FjTFh3YktlbkJ3Mk43ZGk4a1dNd3Z3ZUxsQldORG0rSjNoVE42SitmOXg0MkNDTndTdUU0MGFQejF1VERiTzI1bW5TSW5HMWNSYmNjTG10SnNKUXlxQjB3Y0huQWRzTEM3L3lPeGRtMERmMk1tL2V0RmRscnJQRGRRaVdubkFPV3E2T0ovWWlJMFlUaWF0Mkh3aGtHTC9kV2FvOU1rc2N2STNnV0xRZXNmOWk4TE1wVXlSSFZVTDNqWXJ5WkxMQ1NiRmkybjkxWDBhUFhMTjBXaTJrRHN0L3hMRWVNVnkxdlFyYXdtQVNYVXVmQnJnWVJLclRXNVBUL0NOZStlSDRObi95SE9TbDhZa3lrNjRYdnBJa1M4bjlYMlFqL1ZMSEFvYXdMdDBNNHZiLzY2d1hXVHpWV3BwblJUak56NDNEaFlkblF4c1lBaDhUamo4QlJKZFhNZW1xRk9FQ2lZNm5rczd1ei9Cck5sSFlEOEJyT3ozT0FDazdGNXZEalE1YVYyOUQzKzY2c051dE9WRE9pWlJSNVFjYkdIQzA1a2hzejJETzFDNWtzREo0VnVlSXUyMmI5NUNKbXRwamJzU2pwb09Jb1cxL2oyajJkeFpPK09nc2xXNjBmVXpsMlRMMG5wNkRIcEN0TGRMZnhza1plYW9EVHhUNHkrRWtEY1Q5T0Y3THU5WmJqejRnd2J6MEtRRG1kdUpWckc0TTZRVEp2T21PTGtqVEUzVEV3WTRWczFwL3J4djE3bHhxL2VoZ2YxaVB1eEpoQTkwWXFKcXhqN1ByZ0pxc0FRL1RYYkpYR3lGRnBvTWtQRWUvMnBwN1RadGVrWFQwN09vSlR0U2hGMUg2SWZHS3Ywek9KdUhrRW95S09BT1ZnY2pXejBmQ3p1RjBkdmJ0Y1daWDhRQkVueE9GdTNqcFlKRlpMTGo0Z2VuRW0vRjF0YXZUc0c0TitUZ0FvLzBCY1l5VHNpcTUzSStOdW9wRG5sV1A5UjNKMDlib2xlcjFDdGJha0srZURzcjhXelpwbVhQVXNjRVZHN2djeUZRTkNDaStaNEtmWERyUHdlT29CRnlkNmlZRUY3ejBxekNLdGM4SmJQVTZkTkZvb0l5TmVZM1BJRUZhYU9oSDZpdHN4UXk3NmlBWUVOVHVETDlkSlRKMlVrL0pRRm1ZaXp6U2cwcmRXcHptMUs3ZXFEbisyYUhVRlhPYVNSZEFwSS9tV3lmblF4NUJGajBTYmZrNnRqR00vOG1TbkU3enpzV2tTVXNqMWdScmJUUU5TZGMrVDlWK1FBVk5hZjdJTnNDY3BHR1VVWU1QZ3hBUFVLakxRYkh2NWNWVUxnck1ON3FpbDQzQXRHcTR0bVNxR0orWFZNNk1xSTBld1JWU2I4U3BmN3ZMS3ZmYzlaQ2d1aUNSTFlTK2dreStXdy9td01nMFlpdWp5QmlhK0lpdkR0RGJqeUw3MkI2Q21wZGQ5SExLV3ZVQlpEYlpaZG9mSnlualNoak4rcFlRRGo4UUs4Y3c5Ukx0eTlJYWxiK3pPQnVTa05tMy9RYjUrK2hCWmtJVnFhc1Y4SUFPZVlHUnFEeHp0N0hiZlVTZXBXOVFyZzhjTjJDekFtbTZrbE5iSnRIaFkxWWRQZkRTTGUxU1RKb1hKWFRWZ3pLVTZkTGd1U2p3WndoaDVTc01aeTJBMnhtTmpKaktaU29ZRHhqV2lTcFV4eG5zVC9oNTRyNmNSQjhDNHFUbyt3ODh3a3hSQXVVNklDYWVReVVhdnZ2ZzJ1WUU3bTZBQWNEek01M2VoYkw4M2pUS0F0UDAvNkpjdm9HOFI3TVhuYUhZUUYxRW1xOFVTR3A5eGNma0laTzhmWDRZMXhZYUkxaVQ2cnYvNDZ4VEhid2RoWjBMVUZHN3dKRlVNZEdDZWQxVERUSDJvN2xKR1ZhMUVRNWV3WkRaNW41Q3JpVjFDK1FkUmJVSUJuR3QyZjJObFRxR1Z4VC9OVGJvSUlITkNXQjFzOGJWS3lRSzViNnVMZ2NlRWJDcy9HOTk1NW1tSjJUZitxK3ZyeFRxbkk3bnYwdjh5NmQzZnBsU0NNZnU5NFZrZDNWai9LemVoM1lyV3BWSnZnR1JSQS9CQ3krOEo1bHk5K2ZaQ0VIZjM3RUVxUEsrOXYvNUQxSkxWb2M2TWdPYkdZSUM0Z1JPcVA3TTdUdzRtdkkrZUlCM245a0Q1MGZwSE92azdMZHdRTVNHSmhZZnk0c1FkRU5WTUk1VXhLeGNnMXlPbE1SUDFWVnUzQWZ2YndtTTRUR0Q4NkFKVUJmNGFVeVRHQlZGMGJQTGlYajBtTGtOeEJJVDlQRjRSangwbDM3M1pOcnFxdlJ2Skhrd2lNOW0wTVpXZ2VxZTJWMG1uVmtqeHMzWG5sMVdMaWRhSkJKV0E0cUtBTCtKTldrcU93SU53OGFzeVlJU2lBREQva1QycisyL1FRbEYwY3E2RzF0eHYxSlZWb1kxcWNwUWVESXB2c2x4amsvcjJsdTdqelIzREtRalBPcVg4cjg4dUsrR0FzdG5zdTJqV3F4UVVWSlIzMTA2YUVxWVRaRytBUEMxODFkcXZqRmFwaGIxYzRybHp3Vy9hSEQxSDk1dXBpUzg4OWlhbEJCbmdUWkVOT0k3ZzE5empzMGQ3Tks4Z3h3Rkdma1ROeElwMzRzRU5od09vbUxpMy8zbUZZRW1BaEFRc0NUa1VXaGFPZ0dBKzhwcHlZRUg1c3BlcFNBSm5IVnBnejNycmZ6WU5URm5XZkVYdUZySGNVVEVKSFdnK3NkTittOW1zbzdiV084Y01Zb3UvUXE3U3JMUkc4S24xYVIreERKMFdNQjlkek9nMjJDbXhBZjNRSHlpZmdwRGVwK2hHbFo5Vi85R3ZqUkQyVUVZTlpNdld0UDViM0RiK3BqMm8wUzJDTnEzNXVnOGNFZTdOVDl4T1RtazZOL0xaWjlTTWY0a2ZxdzZvY3ZRSXF0M29rR1RBT1pCdEdQTmdKV0F5TjV3VmFwTUxVZUpXWDcxRlo3dTJoRnZ3K2ZRQmx4QWFETW9xTzRDTWdFcDMvUFRmdVF6RFo5OFVyelNIT0JzVmRLbFpuZkJQRjJ0UTJFb3dlK3RyclF2akFOeHhIcy9aaGRLcENrMHZvMXVadnhGYmxGOHZwYUxxNVcvNmhkOUV5dit6Y3BCUHI1VEpKc29VbkFSYm5LVEdwZ3dQa0lRTWZKOUNuUDJQb0JOZFZGUjdBSDY3QU1taXVldURGS2sxVU1aS2JiVlkxSlBKSTlqaHJ6dkZSTVlSb05TdjUvU016NzJSNkVxNmN0OGZXbWFzWlcvYk43SUM0Ky9hWGVCQWtEV280czI4Mnd0bEY4c1Nqa0d1TzRKUDJEZGc0RTJhOW5DV3plTWtnUjNLV2FIbWJYa25Eb1FUbys0enlPYlVHajl3Tm1PSklHd3ZkSkJzZVZZYTB1YWdRM29LR1FnT0pNYXBOSjUyQkdkRllJYW4yUytNZC8zc2RldkpyY2dOVHZMQUI2L01CUmZkNnJPSG9kc2gzQklLRnR3S2FqTHIyUlFXbC9tT29YbmhvblJ3Tk5PendOaW9ZaGdVUWl4UWV5UDBVVXpaTis2VXpBKzJSKzVwZWxPVjVVQytMR0Y1NHJxUUlwd09lSXB3bkVTYlZVbG1FeWpkT1hIcHppN21ITkoxOU1WRGZZTlpnRzY1cW04TFhRRFRRTVZGbUlCUXJCVThjb1lXNCt2ZmN2MWdvcmlrdlRZUWoxTllua0dQQVExaXA3cDN6K25OWloySnFHVitXdXhZNWxxYnZzd0FmMkdRc1pCR2lzcEowZVVweUxxWGlyL3o4YWhFYk5OV0RnREpWZHdLTG02R3I5WFl4SkFpMFFrN3A2WncraHF2NlhpOWJzZmJDeTdUQmZJVkh6YUNMY2w2WktneEQ3Ri9KVFZkajVmb0NXR0JuVTIvYzhLOUxrb0dWT2FxeEQwaUJLWVcyd21FelFyRlZ0bWNHd0NiUTYvRStBUUp1TzcvbmIrR1czclIxeDNpY2c3VlNUSk84NFduMWpRZ3RhMXMvZXBwM3JuakNDaDBuamxJLytKMkgyZVVuWDM3YS9TOTRNUHkwdU4yNG5Ob2JxL0N5TWtWWGhpdTJzaXZaRXZLRW5MRVllR1Z2UThtVGsxYXo1NHJ4SG5tUjhXNGJqSzlLSThYdWdUL21mRnBWVTBnSU9DUFVqeFRIQm5IZUhUTTQzU3R4SGFtcy9tSzVYNkhnYVY1RktjTkNGTmcvdkNOM2MwTkp4UFVSc1dFcnZCYnR5eHhTZUNjdHlzZjE3cmJnQi9vRWtGbXdJQ1dOSWRsYm5FdnZhRDFmZ2dmUlZuYXpTaldoamUwcXByYUFBdU5ETmRxVDdic1U2ZGduYldvVFc4cEdIZWxsZXR5VldhcXBVL3hlSmFMdU9NZTMwQ3dVZndidmJyTlhLN2ZPRmYyZGEwcTg4eE5IemkzZXpmZURneXExZjh3NnBGMC9HYXlQdlBxMk5FUko0dFhPYXhsWlZxOFFFdkJLY2ZIM0Q1d0Q5bU1YY1k3STZnV3lZb0g4elhBK1dlTmU2eXBGU0RnSmQyNm1BUXV1QUs1Wjk0blk5SzRPbHdPMC9Pcmd1bnhyYmlhU055N1A2RmcvK3ZmZGttRytkbmF2YU5iOUxjaDhGSlN0MUltRTdSYlRZT1hJcFRZUURTMDgrNldtSERyeW56RDhJdmlPQVFyNmswNThzUnFWYXQ3VzVsUU5qTnkzMldVNHZGbzVIL2hXaE9FZFFDM2xBTnpUbVFYNndKeW9aMTJhU2J0c2FVN2NoNUpCOXk2WFNlQkdRYmNFLzR3c3JJU2l1Q0VjdVFodThRV2FCZzJ2UWVtNzhaRmFhSTJDRnpzamJTNTg1cDdsYjBpQXd5SjB6ck90SGtFeFdPYlBJOER0NTgwdEQwZy9yd0pLd1FjTlRuZzVVL21sT0ZSK2lEYm1DM0h5c3ZoN09iVTQ2Zzh5a1FsSFJTWmhKRElTZGxCWEVpLzR0aElLNWVtNTZrdnhmVVNFM2FtV1VRVXlaOTZDZ1orOHE1TXBPbjNiMjNoa2ZUOEhSd2NRWVdhUXQvVzcwSG1kSEhmeVJibGJ3ZFAyTHppUzlhNVd4MzFvOWFBNjRVSVRrUnZBenRDRkFNRWw5akNZVnU3STVkbExOanA0ekFFK0dCNHBFZUwwTU1NOWhZanpQT0hLU0EyUmR1VjI5blhUTVRLelRya0RDdWU0ZWhvUjRSL2p1ckozMGlUbUxxaVBBU0tvdXQxd1VLVDkwRUIvcWdNTmJoL25TMjdlRERQamFnMVN4cG5lNER5T0RPeFh6ZkVsdUNEdm5IZ1FaeG50R0M5OEIzcTJad3ZRc3lXV3NUWWpwVXhZUWYybkEzQVBSdjdBMTNnOERnOXlOcnJ5STdRMklQZGw1V0crV0NUbUtKSzFXU1AxMnUwVlZaVHRVYmM0L3J6VmJJVTVBWENxVnlWdHFRUGsvZVd5RFdabzd1VERsUzB6U2hybENZTE9WK1VYaGg5eWV3a0NjSWRONXFuaCtEaWlqUkdzeTc0UEl0QnZhdm15WFNnOThKUmgvbzhPZ3NrTFdvNXZLSmJrQWltalNIanhHbS93Ykd5SUUrQ05WM2dReG0rd3VPY1J3N3dRZ0Y0WjhFeGEvd2poUHlUMURMd2pWSExXZkxlY01ya1pkQlU2eUt5M3RNYjJwMU4wMndBZmlSM2NpRjNVK1RsSjdHbU5TN3B2R25xUzZWT0tUNU5VYjRTeWxGT3kwNmFGRGh0YkdKTk9hMlkycHBPK3VxUHhNRm5yVjlySSt4a1ZPQ3FmdFhQUTdFNk5SeXlhMG90aFZTVWttRmVtSk9mYUUzNVpPaC9TSklSMlNYK2FBbnB1QXQ3eGk0ME1FaEFIaTljK25YcnY0VWF1Nmp6c3B2cVQwYVNOUk1IWEMyZSs1OEJYakhMMGlrczNFSDY3UnZUUktURG1ORnVqNVJPekd6MWNmdm5lTUVIdnFmb1VZVlMwZlhLdDVxcVhvaTZEOXZQV2l2RzE4cXRRN2VtekxXV0lseE9SMU9sMUwxMnNSelQyV2s1eFVmZGJyVTYwOUJidmtGbmxLQncxZWVpWUgzR3BzbEl1RmNWVk82eEhtNEpMd2tla2tHa2hvNGxveTFaRlAvTVV0MnplQ3hJbTU3S3lSdEJzZ081REJFYTc2NXF3bmRhK1VtT0FmcTF3dkxMSGNmb2JnbkV1YlRyWTZSNDlubGtMaU9nVitPeXdncWVJaEpPak43RE0yMTd0V2RWNmk0VFdSNk1OWXJmTUoyTXlpeGpNenA1T01CZU4yZkZBdHM5TGJnRWRxSEdCU1lXeWczd3ZZQ2FjTnFtbmVJRDZub0lhbVduV0plMGpIQ2tKRk0rUVVjN2JGMW1xdW5WWlBOSlZLc3E3MG9qQ2Z5OWpvdkYwaStDWEFVdGh1IiwiaXYiOiI4OGZiYzc1NzA5OTRmOGY2YjRjMjVkNmM3YjU0ZjQ3YiIsInMiOiJhMzYyMjJiYjUxNWFlNmEyIn0%3D&public_key=E5554D43-23CC-1982-971D-6A2262A2CA24&site=file%3A%2F%2F&userbrowser=Mozilla%2F5.0%20(Linux%3B%20Android%207.1.2%3B%20SM-G973N%20Build%2FPPR1.190810.011%3B%20wv)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Version%2F4.0%20Chrome%2F92.0.4515.131%20Mobile%20Safari%2F537.36&rnd=0.9144498999004613'

rnd = "0." + ("").join(random.choices("1234567890", k = 17))
data = {
    "bda": "",
    "rnd": rnd,
    "site": "https://www.twitch.tv",
    "userbrowser": "Mozilla/5.0 (Linux; Android 7.1.2; SM-G973N Build/PPR1.190810.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36"
    }

r = session.post('https://client-api.arkoselabs.com/fc/gt2/public_key/E5554D43-23CC-1982-971D-6A2262A2CA24' , data=data, headers=header_v1) #, data=data
#print(json.dumps(r.json(), indent=4))

token_v1 = r.json()['token']
print(token_v1)

headers_v2 = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G973N Build/PPR1.190810.011) tv.twitch.android.app/13.0.0/1300000"
        }

session_token = token_v1.split('|')[0]
#print(session_token)
captcha = session.post(f'https://client-api.arkoselabs.com/fc/get_audio/?session_token={session_token}&analytics_tier=40&r=us-west-2&language=en', headers=headers_v2)

with open(f'./captchas/{random.randint(1,100000)}.wav', 'wb') as ff:
    ff.write(captcha.content)
"""
There was a glitch where they wouldn't look for captcha completion + the downloaded audio file is corrupted or idk, don't have time
will fix it in the vacations
"""

passw = "$}W-3L^_-P*%L)cY"
username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=6))
email = f"{username}{random.randint(100, 999)}@gmail.com"

json = {
    "arkose":{
        "token": "20562920e60401e57.4970684105|r=eu-west-1|metabgclr=transparent|guitextcolor=%23000000|lang=en|pk=E5554D43-23CC-1982-971D-6A2262A2CA24|at=40|rid=64|ag=101|cdn_url=https%3A%2F%2Ftwitch-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-eu-west-1.arkoselabs.com|surl=https%3A%2F%2Ftwitch-api.arkoselabs.com|smurl=https%3A%2F%2Ftwitch-api.arkoselabs.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager"     
        },
    "birthday":{
        "day":27,
        "month":4,
        "year":2000
        },
    "client_id":"kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
    "email": email,
    "include_verification_code":True,
    "password": passw,
    "username": username
    }

header = {
        "accept": "application/vnd.twitchtv.v3+json",
        "accept-encoding": "gzip",
        "accept-language": "en-us",
        "client-id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
        "connection": "Keep-Alive",
        "content-type": "application/json; charset=UTF-8",
        "host": "passport.twitch.tv",
        "user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G973N Build/PPR1.190810.011) tv.twitch.android.app/13.0.0/1300000",
        "x-device-id": "7549bd7d0bf549159a556926aebf0c43"
    }

r = session.post("https://passport.twitch.tv/register", json=json, headers=header)

print(r.text)
