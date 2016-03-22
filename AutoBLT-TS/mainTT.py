import ThermalStream as TT
import os, sys, time, csv

os.chdir(os.path.dirname(sys.argv[0]))

myTT = TT.ThermalStream(gpib_port=18)

#myTT.WhoAmI()
myTT.SetRampRate(12)

print myTT.GetRampRate()

dwell = 3600

temp = [[25, 600],
        #[25, dwell],
        [35, dwell], 
        [45, dwell], 
        [55, dwell],
        [65, dwell],
        [75, dwell],
        [85, dwell],
        [90, dwell],
        [95, dwell],
        [100, 1800],
        [25, dwell],
        [15, dwell],
        [5, dwell],
        [0, dwell],
        [-5, dwell],
        [-10, dwell],
        [-15, dwell],
        [25, dwell],
        ]
        

myTT.Initialize()   

time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(time.time()))

with open('temp.csv', 'a') as log:     
    logger = csv.writer(log)
    logger.writerow(['---test begin---'])
    for t, d in temp:
        
        ts = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(time.time()))        
        row = [ts, 'Set point Begin', t]
        print row
        logger.writerow(row)        
        myTT.GoToTemp(t)
        
        ts = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(time.time()))
        row = [ts, 'Dwell Begin', t]
        print row        
        logger.writerow(row)        
        myTT.Dwell(d)
        
        ts = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(time.time()))
        row = [ts, 'Dwell Finish', t]
        print row
        logger.writerow(row)
        
        
            
