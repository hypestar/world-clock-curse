from time import sleep
from datetime import datetime
from pytz import timezone
class WorldClock:

    def __init__(self):
        self.initMap()


    def initMap(self):
        self.worldmap = []
        self.worldmap.append('                OOOOO  OOOOOOOOOO      O  O             OO')
        self.worldmap.append('          OOOO O OO O    OOOOOOO                    O  OOOOOOOOOOO  O')
        self.worldmap.append('OOOOOOOOOOOOOOOOOOO OO    OO    OO      OO OO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
        self.worldmap.append('  OOO  OOOOOOOOOO   OOO                 O OOOOOOOOOOOOOOOOOOOOOOOOOO    O')
        self.worldmap.append('         OOOOOOOOOOOOOOOO           OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
        self.worldmap.append('          OOOOOOOOOOOO             OOOOO OO   OOOOOOOOOOOOOOOOOOOOO O')
        self.worldmap.append('          OOOOOOOOOO                 OO      OOOOOOOOOOOOOOOOOOO O O')
        self.worldmap.append('            OOOO                   OOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
        self.worldmap.append('               OO                 OOOOOOOOOOOO OOOO  OOOO OOOOO')
        self.worldmap.append('                 OO              OOOOOOOOOOOOO O      O    OO')
        self.worldmap.append('                    OOOO           OOOOOOOOOOOOO                O')
        self.worldmap.append('                   OOOOOOO             OOOOO O              O OOO')
        self.worldmap.append('                    OOOOOOOOO           OOOOOO               O      OO')
        self.worldmap.append('                    OOOOOOOO            OOOOOO                    O O')
        self.worldmap.append('                      OOOOOO            OOOOO  O              OOOOOOOO')
        self.worldmap.append('                     OOOO                OOO                  OOOOOOOOO')
        self.worldmap.append('                     OOOO                                           OO     O')
        self.worldmap.append('                     OO                                                   O')
        self.worldmap.append('                     O')

   
    def getCopenhagenTime(self):
        return datetime.now(tz=timezone('Europe/Copenhagen')).strftime('%a, %H:%M')

    def getTokyoTime(self):
        return datetime.now(tz=timezone('Asia/Tokyo')).strftime('%a, %H:%M')        

    def getNewYorkTime(self):
        return datetime.now(tz=timezone('US/Eastern')).strftime('%a, %H:%M')

    def getRarotongaTime(self):
        return datetime.now(tz=timezone('Pacific/Rarotonga')).strftime('%a, %H:%M')

    def getHongKongTime(self):
        return datetime.now(tz=timezone('Asia/Hong_Kong')).strftime('%a, %H:%M')        

    def getNairobeTime(self):
        return datetime.now(tz=timezone('Africa/Nairobi')).strftime('%a, %H:%M')        

    
if __name__ == '__main__':
    wc = WorldClock()
    for line in wc.worldmap:
        print(line)


