import numpy as np

from src.Wall import WallSprite
from src.Checkpoint import CheckpointSprite
from src.Car import CarSprite
from src.Trophy import TrophySprite
from src.FinishLine import FinishLineSprite


### Format: a map is a tuple composed of the following fields
### - a list of WallSprites which delimit the track
### - a list of CheckpointSprites which set optional checkpoints
### - a list of FinishLineSprites which identify the end of the track (should be only one)
### - the CarSprite with its initial position
### - the HUD (text timing info) position, as a tuple (x,y)

Map0 = (
    [
        WallSprite((500, 100), 100, 4), # H top
        WallSprite((500, 700), 100, 4), # H bottom
        WallSprite((450, 400), 4, 600), # V left
        WallSprite((550, 400), 4, 600), # V right
    ],
    [
        CheckpointSprite("Checkpoint 1", (500, 500), 100, 1),
        CheckpointSprite("Checkpoint 2", (500, 300), 100, 1)
    ],
    [
        FinishLineSprite((500, 150), 100)
    ],
    CarSprite('images/car.png', (500, 650)),
    (850, 700)
)

Map1 = (
    [
        WallSprite((500, 100), 800, 4), # H top
        WallSprite((500, 500), 800, 4), # H bottom
        WallSprite((100, 300), 4, 400), # V left
        WallSprite((900, 300), 4, 400), # V right

        WallSprite((500, 250), 500, 4), # H top
        WallSprite((500, 350), 500, 4), # H bottom
        WallSprite((250, 300), 4, 100), # V left
        WallSprite((750, 300), 4, 100), # V right

    ],
    [
        CheckpointSprite("Checkpoint 1", (175, 300), 150, 1),
        CheckpointSprite("Checkpoint 2", (450, 175), 150, 1, True),
        CheckpointSprite("Checkpoint 3", (825, 300), 150, 1)
    ],
    [
        FinishLineSprite((550, 425), 150, True)
    ],
    CarSprite('images/car.png', (500, 425), 90),
    (850, 700)
)

Map2 = (
    [
        WallSprite((500, 0), 1000, 4),
        WallSprite((500, 800), 1000, 4),
        WallSprite((920, 100), 160, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((120, 450), 4, 700),
        WallSprite((240, 350), 4, 700),
        WallSprite((360, 450), 4, 700),
        WallSprite((480, 350), 4, 700),        
        WallSprite((600, 450), 4, 700),
        WallSprite((720, 350), 4, 700),
        WallSprite((840, 450), 4, 700),
        WallSprite((1000, 450), 4, 700),
    ],
    [
        CheckpointSprite("Checkpoint 1", (180, 300), 120, 1),
        CheckpointSprite("Checkpoint 2", (420, 300), 120, 1),
        CheckpointSprite("Checkpoint 3", (660, 300), 120, 1)
    ],
    [
        FinishLineSprite((990, 50), 96, True)
    ],
    CarSprite('images/car.png', (60, 750)),
    (910, 700)
)

Map3 = (
    [
        WallSprite((500, 0), 1000, 4),
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 400), 4, 800),
        WallSprite((560, 750), 4, 100),
        WallSprite((440, 750), 4, 100),
        WallSprite((500, 600), 800, 4),
        WallSprite((220, 700), 440, 4),
        WallSprite((780, 700), 440, 4),
        WallSprite((100, 350), 4, 500),
        WallSprite((200, 250), 4, 500),
        WallSprite((300, 350), 4, 500),
        WallSprite((900, 350), 4, 500),
        WallSprite((800, 250), 4, 500),
        WallSprite((700, 350), 4, 500),
        WallSprite((500, 100), 400, 4),
        WallSprite((500, 540), 60, 4),
        WallSprite((530, 570), 4, 60),
        WallSprite((470, 570), 4, 60),
    ],
    [
        CheckpointSprite("Checkpoint 1", (150, 300), 100, 1),
        CheckpointSprite("Checkpoint 2", (850, 300), 100, 1),
        CheckpointSprite("Checkpoint 3", (600, 650), 100, 1, True),
        CheckpointSprite("Checkpoint 4", (400, 650), 100, 1, True),
    ],
    [
        FinishLineSprite((500, 50), 96, True)
    ],
    CarSprite('images/car.png', (500, 760)),
    (850, 725)
)
