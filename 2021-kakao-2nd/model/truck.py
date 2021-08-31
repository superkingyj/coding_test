from typing import *
from model.truck_command import TruckCommand
from model.map import Map

class Truck:
    def __init__(self, coord: Tuple[int, int] = (0, 0), bikes: int = 0, id: int = 0):
        self.coordinate = coord
        self.bikes = bikes
        self.id = id

    def move(self, command: TruckCommand):
        if command == TruckCommand.RIGHT:
            self.coordinate = (self.coordinate[0]+1, self.coordinate[1])
        elif command == TruckCommand.LEFT:
            self.coordinate = (self.coordinate[0]-1, self.coordinate[1])
        elif command == TruckCommand.UP:
            self.coordinate = (self.coordinate[0], self.coordinate[1]+1)
        elif command == TruckCommand.DOWN:
            self.coordinate = (self.coordinate[0], self.coordinate[1]-1)

    def takeoff(self, map: Map):
        if self.bikes <= 0: 
            raise RuntimeError("바이크를 내릴 수 없습니다.")
        self.bikes -= 1
        map.increase(self.coordinate)

    def pickup(self, map: Map):
        if map.getBike(self.coordinate) <= 0 and self.bikes >= 20:
            raise RuntimeError("바이크를 실을 수 없습니다.")
        self.bikes += 1
        map.decrease(self.coordinate)
    
    def act(self, command: TruckCommand, map: Map):
        if command in [TruckCommand.RIGHT, TruckCommand.LEFT, TruckCommand.UP, TruckCommand.DOWN]:
            self.move(command)
        elif command == TruckCommand.TAKE_OFF:
            self.takeoff(map)
        elif command == TruckCommand.PICK_UP:
            self.pickup(map)
