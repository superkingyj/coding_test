import unittest
from model.truck import Truck
from model.truck_command import TruckCommand
from model.map import Map

class Test_Truck(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    '''
    def test_move(self):
        truck = Truck(coord = (0, 0))
        r = truck.move(coord = (1, 1)) # ["RIGHT", "UP"] or ["UP", "RIGHT"]
        self.assertTrue(len(r) == 2)
        self.assertTrue(r == [TruckCommand.RIGHT, TruckCommand.UP] or r == [TruckCommand.UP, TruckCommand.RIGHT])
    '''
    
    def test_pickup(self):
        map = Map(size = (1, 1))
        map.setBike((0, 0), 3)
        truck = Truck(coord = (0, 0))
        truck.pickup(map)
        self.assertTrue(truck.bikes == 1)
        self.assertTrue(map.getBike((0, 0)) == 2)

    def test_takeoff(self):
        map = Map(size = (1, 1))
        map.setBike((0, 0), 0)
        truck = Truck(coord = (0, 0), bikes = 3)
        truck.takeoff(map)
        self.assertTrue(truck.bikes == 2)
        self.assertTrue(map.getBike((0, 0)) == 1)