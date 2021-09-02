from typing import *

class Map:
    def __init__(self, size: Tuple[int, int], value: int = 0, map: List[List[int]] = None):
        self.size = size
        if map:
            self.map = map
        else:
            self.map = [[value for i in range(0,size[1])] for j in range(0,size[0])]

    def __checkCoord(self, coord: Tuple[int, int]):
        if coord[0] >= 0 and coord[1] >= 0 and coord[0] < self.size[0] and coord[1] < self.size[1] : return
        raise RuntimeError(f"coord : {coord}, 좌표에러")

    def getMostCoord(self, blackList: List[Tuple[int, int]] = None):
        max_ = -1
        x_, y_ = -1, -1
        if not blackList:
            blackList = []
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if (x, y) in blackList:
                    continue
                if max_ < self.map[x][y]:
                    max_ = self.map[x][y]
                    x_, y_ = x, y
        return (x_, y_), max_

    def getLeastCoord(self, blackList: List[Tuple[int, int]] = None):
        min_ = 999999
        x_, y_ = -1, -1
        if not blackList:
            blackList = []
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if (x, y) in blackList:
                    continue
                if min_ > self.map[x][y]:
                    min_ = self.map[x][y]
                    x_, y_ = x, y
        return (x_, y_), min_
    
    def setBikeById(self, id: int, bike: int):
        self.map[int(id / self.size[0])][int(id % self.size[1])] = bike
    
    def getIdToCoordinate(self, id: int) -> Tuple[int, int]:
        return (int(id / self.size[0]), int(id % self.size[1]))

    def setBike(self, coord: Tuple[int, int], bike: int):
        self.__checkCoord(coord)
        self.map[coord[0]][coord[1]] = bike
    
    def getBike(self, coord: Tuple[int, int]):
        self.__checkCoord(coord)
        return self.map[coord[0]][coord[1]]
    
    def increase(self, coord: Tuple[int, int]):
        self.__checkCoord(coord)
        self.map[coord[0]][coord[1]] += 1

    def decrease(self, coord: Tuple[int, int]):
        self.__checkCoord(coord)
        self.map[coord[0]][coord[1]] -= 1

    def getDistance(self, src: Tuple[int, int], dst: Tuple[int, int]) -> int:
        self.__checkCoord(src)
        self.__checkCoord(dst)
        return abs(src[0]-dst[0])+abs(src[1]-dst[1])
    
    def print(self):
        for y in range(len(self.map[0]) - 1, -1, -1):
            for x in range(len(self.map)):
                print(self.map[x][y], end=' ')
            print()



