from typing import *
from abc import ABC, abstractmethod, abstractclassmethod
from model.truck import Truck
from model.map import Map

class Strategy(ABC):
    @abstractmethod
    def run(self, truck: Truck, map: Map):
        pass
    @abstractmethod
    def runFull(self, truck: Truck, map: Map):
        pass