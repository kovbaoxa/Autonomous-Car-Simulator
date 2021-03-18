import time
import pygame
import math

class Brain:
    def __init__(self, database):
        self.database = database

    def run(self, cv=None, bcv=None):
    
        ######################################################################
        # ZAČÁTEK BLOKU
        # V tomto bloku můžete inicializovat proměnné mimo cyklus
        ######################################################################
        
        # my_amazing_var = 0
        # my_regular_var = 0

        ######################################################################
        # KONEC BLOKU
        ######################################################################
    
        while self.isRunning():
            with cv:
                cv.wait()

            '''
            1. Jak ovládat auto?

                Funkce pro zrychlení auta s volitelným parametrem "num".
                Num musí být v rozsahu 0-5. Pokud není "num" specifikován, 
                použije se výchozí hodnota 5.
                
                self.faster(num)

                Funkce pro zpomalení auta s volitelným parametrem "num".
                Num musí být v rozsahu 0-5. Pokud není "num" specifikován, 
                použije se výchozí hodnota 5.

                self.slower(num)

                Funkce pro zatočení doprava s volitelným parametrem "num".
                Num musí být v rozsahu 0-10. Pokud není "num" specifikován, 
                použije se výchozí hodnota 10°.

                self.right(num)

                Funkce pro zatočení doleva s volitelným parametrem "num".
                Num musí být v rozsahu 0-10. Pokud není "num" specifikován, 
                použije se výchozí hodnota 10°.

                self.left(num)


            2. Jak přistupovat k informacím o autě?

                Rychlost auta v rozsahu [0-15]:
                self.getCarSpeed()
                
                Data z lidaru na autě uložená v poli délky 180 prvků v rozsahu [0-300]:
                self.getLidarData()

                Natočení auta v rozsahu [0-360°]:
                self.getCarDirection()
                
                Souřadnice auta uložené ve struktuře tuple:
                self.getCarPosition()

            '''
            ####################################################################
            # ZAČÁTEK BLOKU
            # Zde implementujte váš algoritmus
            ####################################################################

            # Nahradit vaším programem
            self.faster(2)

            ####################################################################
            # KONEC BLOKU
            ####################################################################

            with bcv:
                bcv.notifyAll()

    ####################################################################
    # CAR CONTROL
    ####################################################################

    def faster(self, val: int = 5):
        self.database.control.faster(val)

    def slower(self, val: int = 5):
        self.database.control.slower(val)

    def right(self, val: int = 10):
        self.database.control.right(val)

    def left(self, val: int = 10):
        self.database.control.left(val)

    ####################################################################
    # CAR SENSORS
    ####################################################################
    def getCarPosition(self):
        return self.database.car.position

    def getCarSpeed(self):
        return self.database.car.speed

    def getCarDirection(self):
        return self.database.car.direction

    def getLidarData(self):
        return self.database.lidar.data

    ####################################################################
    # SIMULATION INFO
    ####################################################################
    def isRunning(self):
        return not self.database.stop

    def getTimestamp(self):
        return self.database.timestamp

    def getRunTime(self):
        return self.database.run_time

    def getRunDistance(self):
        return self.database.run_dist
