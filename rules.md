# DDMP6 Hackaton

## Intro
Hello future developers! Here you will confront yourselves with one of the biggest challenges of this century: Autonomous Driving!

Your goal is to let your car reach autonomously (i.e., without you driving it in real time) the end of one track, going through all the checkpoints.

Too easy? You'll have to do it in the least possible time and with the shortest path (now we talk!).

How? Let's discover it together.

# Description
The candidate has to provide an autonomous driving function, based on data coming from the car's sensors.
The car is equipped with a speed meter (-15 to 15), a direction meter (-180 to +180 degrees), and a LiDAR system,
which allows to detect obstacles in the range -90 to + 90 degrees.

## Requirements
The control function must be implemented in Python. The candidate shall provide only the autonomos driving function.

## Tasks
The tasks are divided into two categories, the first one is for candidates aged 11 to 14, the second one for candidates 14+.

### Pod racer competition (Candidates 11-14)
The candidate shall provide an autonomous driving function which is able to drive the car to the finish line, through all the checkpoints.

The candidate shall use ONLY the current speed and position of the car as input data.

The goal is to reach the end of the assigned map optimizing both time and distance.

A maximum of 30 points will be assigned to the candidate, as follows:
- up to 10 points for completing the race
    - 10 points for crossing the finish line
    - 6 points for crossing 5 checkpoints
    - 4 points for crossing 4 checkpoints
    - 3 points for crossing 3 checkpoints
    - 2 points for crossing 2 checkpoints
    - 1 points for crossing 1 checkpoint
    - 0 points for crossing 0 checkpoints
- up to 10 points for the (complete) race time
    - 10 points for the top 15% of times
    - 6 points in between 16% and 35%
    - 4 points in between 36% and 50%
    - 3 points in between 51% and 75%
    - 2 points in between 76% and 90%
    - 1 points in between 91% and 100%
- up to 5 points for the (complete) race distance
    - 5 points for the top 15% of distance
    - 4 points in between 16% and 35%
    - 3 points in between 36% and 50%
    - 2 points in between 51% and 75%
    - 1 points in between 76% and 90%
    - 0 points in between 91% and 100%
- up to 5 points for the algorithm performance

### Tie fighter competition (Candidates 14+)
The candidate shall provide ONE autonomous driving function which is able to drive the car to the finish line on four different maps.
Three maps will be publicly available to all the candidates to test their implementation, the fourth map is unknown and will be used by the evaluation team.

A score of up to 25 points will be assigned per each race, according to the following rules:
- up to 10 points for completing the race
    - 10 points for crossing the finish line
    - 6 points for crossing 5 checkpoints
    - 4 points for crossing 4 checkpoints
    - 3 points for crossing 3 checkpoints
    - 2 points for crossing 2 checkpoints
    - 1 points for crossing 1 checkpoint
    - 0 points for crossing 0 checkpoints
- up to 10 points for the (complete) race time
    - 10 points for the top 15% of times
    - 6 points in between 16% and 35%
    - 4 points in between 36% and 50%
    - 3 points in between 51% and 75%
    - 2 points in between 76% and 90%
    - 1 points in between 91% and 100%
- up to 5 points for the (complete) race distance
    - 5 points for the top 15% of distance
    - 4 points in between 16% and 35%
    - 3 points in between 36% and 50%
    - 2 points in between 51% and 75%
    - 1 points in between 76% and 90%
    - 0 points in between 91% and 100%

The total score (up to 100) will determine the final classification.
Up to 5 bonus points shall be assigned to the best three algorithms.

## Tracks
### Pod racer competition
#### 1. Mos Espa Grand Arena
```
PHOTO
```

### Tie fighter competition
#### 1. Yavin 4 Rebel Base
```
PHOTO
```

#### 2. Hoth Ice Cave
```
PHOTO
```

#### 3. Forest of Endor
```
PHOTO
```

#### 4. Mustafar Lava Canyon
```
?????
```

## Technical info
### Simulation
The simulation of the track race happens on a 2D map, delimited by linear walls.

The game framework, based on `pygame`, evaluates the position of the car on the map at each new time frame, according to the current speed and direction of the car.

Within each time frame, the autonomous driving function shall:
- get the data from the car sensors (speed, direction, LiDAR)
- evaluate and send one or more control actions (increse/decrease speed, change direction)

The control actions are handled by means of an event queue, and will be executed by the game engine within the next simulation frame (in the order they have been issued).

**WARNING:** if the driving function is too slow, it will not be able to send the control events in time for the next simulation cycle.

**The track time considered for the competition is only the simulation time, not the program execution time.**
Therefore the total running time of the simulations may not necessarily coincide with the running time of the program (to ensure that performance variability will not lead to different results).

### Car
The car can be moved forward and backward by an absolute variation of speed of maximum 5 units per control event, and can be rotated by a maximum angle of 8 degrees in a single control event.

### LiDAR
The LiDAR data is stored into an array of 180 integers, which encodes the distance from the obstacles in the corresponding direction.

## Environment setup
### Python


### Other languages

## Examples
```
code 1
```
```
code 2
```
