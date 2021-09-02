import unittest
from model.map import Map

class Test_Map(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_getDistance(self):
        map = Map(size = (5,5))
        currentCoord = (0,0)
        targetCoord = (4,4)
        self.assertTrue(map.getDistance(currentCoord, targetCoord)==8)

        currentCoord = (4,4)
        targetCoord = (2,2)
        self.assertTrue(map.getDistance(currentCoord, targetCoord)==4)

        currentCoord = (4,4)
        targetCoord = (1,2)
        self.assertTrue(map.getDistance(currentCoord, targetCoord)==5)
    
    # test_getBike 는 test_truck 에서 다뤄짐