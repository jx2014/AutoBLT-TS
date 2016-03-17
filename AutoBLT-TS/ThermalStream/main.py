import ThermalStream as TT
import os, sys

os.chdir(os.path.dirname(sys.argv[0]))

myTT = TT.ThermalStream(gpib_port=18)

#myTT.WhoAmI()
myTT.SetRampRate(12)

print myTT.GetRampRate()

dwell = 3600

hightemp = [35, 45,55,65,75,85,90,95,100]
lowtemp = [20,15,10, 5]

'''
with open('temp.csv', 'wb') as log:
    
    for temp in hightemp:
        myTT.SetMode('hot')
        myTT.SetTargetTempSetpoint(temp)
        
        while myTT.GetTempEvent() == 'not at temperature':
            
'''