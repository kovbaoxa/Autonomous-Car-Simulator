from Wall import WallSprite
from Car import CarSprite
from Trophy import TrophySprite
from Parking import Parking
from Crosswalk import Crosswalk

Map1 = (
    [
        WallSprite((500, 0), 1000, 4),
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 400), 4, 800),
        WallSprite((400, 400), 4, 800),
        WallSprite((600, 400), 4, 800),
        WallSprite((540, 650), 120, 4),
        WallSprite((540, 450), 120, 4),
        WallSprite((540, 300), 120, 4),
        WallSprite((540, 100), 120, 4),
        WallSprite((460, 200), 120, 4),
        WallSprite((460, 375), 120, 4),
        WallSprite((460, 550), 120, 4),
    ],
    [
        TrophySprite((500, 40))
    ],
    [

    ],
    [

    ],
    CarSprite('images/car.png', (500, 760)),
)

Map2 = (
    [
        WallSprite((500, 0), 1000, 4),
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 400), 4, 800),
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
        TrophySprite((950, 40))
    ],
    [

    ],
    [
        Crosswalk((60, 400), 120, 4, interval=40, phase=0),
        Crosswalk((180, 300), 120, 4, interval=30, phase=5),
        Crosswalk((180, 500), 120, 4, interval=30, phase=15),
        Crosswalk((300, 200), 120, 4, interval=20, phase=30),
        Crosswalk((300, 600), 120, 4, interval=20, phase=40),
        Crosswalk((420, 400), 120, 4, interval=40, phase=55),
        Crosswalk((540, 600), 120, 4, interval=20, phase=65),
        Crosswalk((540, 200), 120, 4, interval=20, phase=80),
        Crosswalk((660, 300), 120, 4, interval=30, phase=70),
        Crosswalk((660, 500), 120, 4, interval=30, phase=85),
        Crosswalk((780, 400), 120, 4, interval=40, phase=95),
    ],
    CarSprite('images/car.png', (60, 750)),
)

Map3 = (
    [
        WallSprite((512, 2.5), 1024, 5),
        WallSprite((512, 765.5), 1024, 5),
        WallSprite((2.5, 384), 5, 768),
        WallSprite((0 + 20, 0), 30, 1000),
        WallSprite((0 + 20, 768), 30, 0 + 100),
        WallSprite((0 + 50, 0), 30, 900),
        WallSprite((0 + 50, 768), 30, 100 + 100),
        WallSprite((0 + 80, 0), 30, 805),
        WallSprite((0 + 80, 768), 30, 195 + 100),
        WallSprite((0 + 110, 0), 30, 715),
        WallSprite((0 + 110, 768), 30, 285 + 100),
        WallSprite((0 + 140, 0), 30, 630),
        WallSprite((0 + 140, 768), 30, 370 + 100),
        WallSprite((0 + 170, 0), 30, 560),
        WallSprite((0 + 170, 768), 30, 440 + 100),
        WallSprite((0 + 200, 0), 30, 495),
        WallSprite((0 + 200, 768), 30, 505 + 100),
        WallSprite((0 + 230, 0), 30, 435),
        WallSprite((0 + 230, 768), 30, 565 + 100),
        WallSprite((0 + 260, 0), 30, 380),
        WallSprite((0 + 260, 768), 30, 620 + 100),
        WallSprite((0 + 290, 0), 30, 330),
        WallSprite((0 + 290, 768), 30, 670 + 100),
        WallSprite((0 + 320, 0), 30, 285),
        WallSprite((0 + 320, 768), 30, 715 + 110),
        WallSprite((0 + 350, 0), 30, 245),
        WallSprite((0 + 350, 768), 30, 755 + 120),
        WallSprite((0 + 380, 0), 30, 210),
        WallSprite((0 + 380, 768), 30, 790 + 130),
        WallSprite((0 + 410, 0), 30, 180),
        WallSprite((0 + 410, 768), 30, 820 + 140),
        WallSprite((0 + 440, 0), 30, 155),
        WallSprite((0 + 440, 768), 30, 845 + 150),
        WallSprite((0 + 470, 0), 30, 135),
        WallSprite((0 + 470, 768), 30, 865 + 160),
        WallSprite((0 + 500, 0), 30, 120),
        WallSprite((0 + 500, 768), 30, 880 + 170),
        WallSprite((0 + 530, 0), 30, 110),
        WallSprite((0 + 530, 768), 30, 890 + 180),
        WallSprite((0 + 560, 0), 30, 105),
        WallSprite((0 + 560, 768), 30, 895 + 190),
        WallSprite((0 + 590, 0), 30, 105),
        WallSprite((0 + 590, 768), 30, 895 + 190),
        WallSprite((0 + 620, 0), 30, 110),
        WallSprite((0 + 620, 768), 30, 890 + 180),
        WallSprite((0 + 650, 0), 30, 120),
        WallSprite((0 + 650, 768), 30, 880 + 170),
        WallSprite((0 + 680, 0), 30, 135),
        WallSprite((0 + 680, 768), 30, 865 + 160),
        WallSprite((0 + 710, 0), 30, 155),
        WallSprite((0 + 710, 768), 30, 845 + 150),
        WallSprite((0 + 740, 0), 30, 180),
        WallSprite((0 + 740, 768), 30, 825 + 140),
        WallSprite((0 + 770, 0), 30, 210),
        WallSprite((0 + 770, 768), 30, 790 + 130),
        WallSprite((0 + 800, 0), 30, 245),
        WallSprite((0 + 800, 768), 30, 755 + 120),
        WallSprite((0 + 830, 0), 30, 285),
        WallSprite((0 + 830, 768), 30, 715 + 110),
        WallSprite((0 + 860, 0), 30, 330),
        WallSprite((0 + 860, 768), 30, 670 + 100),
        WallSprite((0 + 890, 0), 30, 380),
        WallSprite((0 + 890, 768), 30, 620 + 100),
        WallSprite((0 + 920, 0), 30, 435),
        WallSprite((0 + 920, 768), 30, 565 + 100),
        WallSprite((0 + 950, 0), 30, 495),
        WallSprite((0 + 950, 768), 30, 505 + 100),
        WallSprite((0 + 980, 0), 30, 560),
        WallSprite((0 + 980, 768), 30, 440 + 100),
        WallSprite((0 + 1010, 0), 30, 630),
        WallSprite((0 + 1010, 768), 30, 370 + 100),
        WallSprite((0 + 1040, 0), 30, 710),
        WallSprite((0 + 1040, 768), 30, 290 + 100),
    ],
    [
        TrophySprite((980, 400))
    ],
    CarSprite('images/car.png', (30, 570), -20)
)
