import unittest
from model.truck import Truck
from model.truck_command import TruckCommand
from model.map import Map
from strategy.strategy import Strategy
from strategy.most_to_least_strategy import MostToLeastStrategy

class Test_Strategy(unittest.TestCase):
    def setUp(self) -> None:
        self.truck = Truck((0,0), 0)
        self.map = Map((5,5), 1)

        self.map.setBike((2,1),5)
        self.map.setBike((4,3),0)

    def test_mostToLeastStrategy(self):
        strategy = MostToLeastStrategy()
        for i in range(3): 
            strategy.run(self.truck, self.map)
        self.assertTrue(self.truck.coordinate == (2,1) and self.truck.bikes == 0)
        for i in range(3): 
            strategy.run(self.truck, self.map)
            print(self.truck.bikes)
            print(self.truck.coordinate)
        self.assertTrue(self.truck.coordinate == (2,1) and self.truck.bikes == 3)
        for i in range(4): 
            strategy.run(self.truck, self.map)
        self.assertTrue(self.truck.coordinate == (4,3) and self.truck.bikes == 3)
        
        strategy.run(self.truck, self.map)
        self.assertTrue(self.truck.coordinate == (4,3) and self.truck.bikes == 2)


