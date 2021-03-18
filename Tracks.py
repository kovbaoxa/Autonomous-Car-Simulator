from Wall import WallSprite
from Car import CarSprite
from Trophy import TrophySprite
from FinishLine import FinishLineSprite

import numpy as np

### Format: a map is a tuple composed of the following fields
### - a list of WallSprites which delimit the track
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
        FinishLineSprite((500, 150), 100)
    ],
    CarSprite('images/car.png', (500, 650)),
    (850, 700)
)
