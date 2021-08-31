from typing import *
from strategy.strategy import Strategy
from model.truck import Truck
from model.truck_command import TruckCommand
from model.map import Map

blackList = []

class MostToLeastStrategy(Strategy):
    def run(self, truck: Truck, map: Map):
        dstAct = TruckCommand.PICK_UP
        rblackList = [coord for id, coord in blackList if id != truck.id]
        if truck.bikes <= 3:
            dst, count = map.getMostCoord(blackList=rblackList)
            if count <=2:
                return TruckCommand.DO_NOTHING
        else: 
            dst, count = map.getLeastCoord(blackList=rblackList)
            if count > 2:
                return TruckCommand.DO_NOTHING
            dstAct = TruckCommand.TAKE_OFF
        if (truck.id, (dst)) not in blackList:
            blackList.append((truck.id, (dst)))

        ## (0,0) --> (2,1)
        print(f"truck.coord: {truck.coordinate}, dst: {dst}, truck.bikes: {truck.bikes}, dstAct: {dstAct}", end='')
        if (truck.coordinate != dst):
            if truck.coordinate[0] < dst[0]: command = TruckCommand.RIGHT
            elif truck.coordinate[0] > dst[0]: command = TruckCommand.LEFT
            elif truck.coordinate[1] < dst[1]: command = TruckCommand.UP
            else: command = TruckCommand.DOWN
        else: 
            command = dstAct
        print(f", command: {command}")
        map.print()
            
        truck.act(command, map)
        return command
        
    def runFull(self, truck: Truck, map: Map):
        blackList = []
        return [self.run(truck, map) for _ in range(10)]
