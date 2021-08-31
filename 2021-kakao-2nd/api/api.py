from typing import *
import requests

from model.command import Command

TOKEN = "c91b50bf594c7f704c0833af593f2e51"
URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

class API:
    def __check_status(self, status_code: int, url: str, json: dict):
        if status_code != 200:
            raise requests.exceptions.HTTPError(f"ERROR! url:{url}, status: {status_code}, json:{json}")

    def start(self, token: str = TOKEN, problem: int = 1) -> dict:
        '''
Response
Key

Key	Type	Description
auth_key	String	Start API 를 통해 발급받은 key, 이후 문제 풀이에 진행되는 모든 API에 이 key를 사용
problem	Integer	선택한 시나리오 번호
time	Integer	현재 카카오 T 바이크 서비스에서의 시각 (0부터 시작)

Example

{
  "auth_key": "1fd74321-d314-4885-b5ae-3e72126e75cc",
  "problem": 1,
  "time": 0
}
        '''
        # requests.post(f"{URL}/start", headers={"X-Auth-Token":token}, data={"problem":problem}) # Errer
        # requests.post(f"{URL}/start", headers={"X-Auth-Token":token, "Content-Type":"applications"}, data=json.dumps({"problem":problem}))
        url = f"{URL}/start"
        json = {"problem":problem}

        r = requests.post(url, headers = {"X-Auth-Token":token}, json = json)
        self.__check_status(r.status_code, url, json)

        return r.json()
        

    def locations(self, authorization: str) -> dict:
        url = f"{URL}/locations"
        r = requests.get(url, headers = {'Authorization': authorization, 'Content-Type': "application/json"})
        self.__check_status(r.status_code, url, None)
        
        return r.json()
        
    def trucks(self, authorization: str) -> dict:
        url = f"{URL}/trucks"
        r = requests.get(url, headers = {'Authorization': authorization, 'Content-Type': "application/json"})
        self.__check_status(r.status_code, url, None)
        
        return r.json()

    def simulate(self, authorization: str, commands: List[Command]) -> dict:
        url = f"{URL}/simulate"
        json = {"commands" : commands}
        print(json)
        r = requests.put(url, headers = {'Authorization': authorization, 'Content-Type': "application/json"}, json = json)
        self.__check_status(r.status_code, url, None)
        
        return r.json()

    def score(self,authorization: str) -> dict:
        url = f"{URL}/score"
        r = requests.get(url, headers = {'Authorization': authorization, 'Content-Type': "application/json"})
        self.__check_status(r.status_code, url, None)

        return r.json()
