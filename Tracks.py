from Wall import WallSprite
from Checkpoint import CheckpointSprite
from Car import CarSprite
from Trophy import TrophySprite
from FinishLine import FinishLineSprite

import numpy as np

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
        CheckpointSprite((500, 500), 100, 1, "Checkpoint 1"),
        CheckpointSprite((500, 300), 100, 1, "Checkpoint 2")
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
        CheckpointSprite((175, 300), 150, 1, "Checkpoint 1"),
        CheckpointSprite((450, 175), 1, 150, "Checkpoint 2"),
        CheckpointSprite((825, 300), 150, 1, "Checkpoint 3")
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
        CheckpointSprite((180, 300), 120, 1, "Checkpoint 1"),
        CheckpointSprite((420, 300), 120, 1, "Checkpoint 2"),
        CheckpointSprite((660, 300), 120, 1, "Checkpoint 3")
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
        CheckpointSprite((150, 300), 100, 1, "Checkpoint 1"),
        CheckpointSprite((850, 300), 100, 1, "Checkpoint 2"),
        CheckpointSprite((600, 650), 1, 100, "Checkpoint 3"),
        CheckpointSprite((400, 650), 1, 100, "Checkpoint 4"),
    ],
    [
        FinishLineSprite((500, 50), 96, True)
    ],
    CarSprite('images/car.png', (500, 760)),
    (850, 725)
)
