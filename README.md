## Autonomous Car Simulator/ Simulátor autonomního auta (EN/CZ)


### Dependencies/Potřebný SW

(EN) Described in file SETUP.md

(CZ) Potřebné info najdete v souboru SETUP.md

### Use/Spuštění

#### Auto

(EN) Drive with your own algorithm which is implemented at `Brain.py`.

(CZ) Ovládání auta programem napsaným v souboru `Brain.py`.
```
python main.py --auto <simple|advanced>
```

#### Manual

(EN) Drive with Keyboard.

(CZ) Ovládání klávesnicí.

```
python main.py
```

#### Maps/Mapy

(EN) Choose one of the available maps.

(CZ) Vyberte si jednu z nabízených map.

```
python main.py --map <0-3>
```

#### Cmd line examples/ Spouštění aplikace z příkazové řádky

```
python main.py --auto simple --map 1
python main.py --auto advanced --map 1
python main.py --auto advanced --map 2
python main.py --auto advanced --map 3
```


__Example/Ukázka__:

![Team1](https://github.com/x2ever/Autonomous-Car-Simulator/blob/master/images/1팀.gif)


### LiDAR

(EN) Participants receive virtual LiDAR and GPS data.

(CZ) Účastníci mají k dispozici virtuální LiDAR a GPS souřadnice.

![LiDAR_preview.png](https://github.com/x2ever/Autonomous-Car-Simulator/blob/master/images/LiDAR_preview.png)

### Credit/Zásluhy
driving club ThinKingo (see the source of the fork)
