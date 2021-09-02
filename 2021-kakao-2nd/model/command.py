from typing import *

class Command:
    def __init__(self, truck_id, command):
        # { "truck_id": 0, "command": [2, 5, 4, 1, 6] }
        
        self.dict_ = {"truck_id": truck_id, "command": [item.value for item in command]}
    
    def get(self) -> dict:
        return self.dict_