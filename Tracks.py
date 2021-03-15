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
        WallSprite((500, 0), 1000, 4),
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 400), 4, 800),
        WallSprite((400, 400), 4, 800),
        WallSprite((600, 450), 4, 700),
        WallSprite((540, 650), 120, 4),
        WallSprite((540, 450), 120, 4),
        WallSprite((540, 300), 120, 4),
        WallSprite((540, 100), 120, 4),
        WallSprite((460, 200), 120, 4),
        WallSprite((460, 375), 120, 4),
        WallSprite((460, 550), 120, 4),
    ],
    [
    ],
    [
        FinishLineSprite((590, 50), 96, True)
    ],
    CarSprite('images/car.png', (500, 760)),
    (850, 700)
)

Map2 = (
    [
        WallSprite((500, 0), 1000, 4),
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 450), 4, 700),
        WallSprite((120, 450), 4, 700),
        WallSprite((360, 450), 4, 700),
        WallSprite((600, 450), 4, 700),
        WallSprite((840, 450), 4, 700),
        WallSprite((920, 100), 160, 4),
        WallSprite((240, 350), 4, 700),
        WallSprite((480, 350), 4, 700),
        WallSprite((720, 350), 4, 700),
    ],
    [
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
        WallSprite((160, 800), 320, 4),
        WallSprite((720, 800), 560, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 400), 4, 800),
        WallSprite((560, 600), 4, 400),
        WallSprite((560, 150), 4, 300),
        WallSprite((620, 350), 4, 100),
        WallSprite((590, 300), 60, 4),
        WallSprite((590, 400), 60, 4),
        WallSprite((440, 460), 4, 720),
        WallSprite((320, 100), 4, 200),
        WallSprite((320, 100), 4, 200),
        WallSprite((320, 680), 4, 240),
        WallSprite((320, 340), 4, 160),
        WallSprite((220, 230), 4, 60),
        WallSprite((270, 200), 100, 4),
        WallSprite((270, 260), 100, 4),
        WallSprite((220, 490), 4, 140),
        WallSprite((270, 420), 100, 4),
        WallSprite((270, 560), 100, 4),
    ],
    [
    ],
    [
        FinishLineSprite((380, 790), 120)
    ],
    CarSprite('images/car.png', (500, 760)),
    (850, 700)
)

Map4 = (
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
    ],
    [
        FinishLineSprite((500, 50), 96, True)
    ],
    CarSprite('images/car.png', (500, 760)),
    (850, 725)
)
