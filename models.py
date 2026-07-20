from dataclasses import dataclass

@dataclass
class Video:
    id:str
    title:str
    channel:str
    duration:int
    views:int

