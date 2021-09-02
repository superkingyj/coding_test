from typing import *
from model.truck import Truck
from api.api import API
from strategy.most_to_least_strategy import MostToLeastStrategy
from model.command import Command
from model.map import Map
from pprint import pprint

class Simulator:
    def __init__(self, problemId):
        self.problemId = problemId
        self.size = (5, 5) if problemId == 1 else (60, 60)
        truckCount = 5 if problemId == 1 else 10
        self.map = Map(size = self.size)
        self.trucks = [Truck(id = i) for i in range(truckCount)]
        self.api = API()
        self.authKey = self.api.start(problem = self.problemId)['auth_key']
        self.strategy = MostToLeastStrategy()
    
    def run(self):
        while True:
            locations = self.api.locations(self.authKey)
            for item in locations["locations"]:
                self.map.setBikeById(item["id"], item["located_bikes_count"])
            trucks = self.api.trucks(self.authKey)
            for item in trucks["trucks"]:
                self.trucks[item["id"]].coordinate = self.map.getIdToCoordinate(item["location_id"])
                self.trucks[item["id"]].bikes = item["loaded_bikes_count"]

            commands = []
            for i in range(len(self.trucks)):
                commands.append(Command(i, self.strategy.runFull(self.trucks[i], self.map)).get())
            sim_result = self.api.simulate(self.authKey, commands)
            if sim_result['status'] == "finished": break
            pprint(sim_result)

        print(self.api.score(self.authKey))

            