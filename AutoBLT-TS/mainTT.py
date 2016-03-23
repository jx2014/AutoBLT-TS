import ThermalStream as TT
import os, sys, time, csv

os.chdir(os.path.dirname(sys.argv[0]))

myTT = TT.ThermalStream(gpib_port=18)

#myTT.WhoAmI()
myTT.SetRampRate(12)

print myTT.GetRampRate()

dwell = 3600

test_temp =[[30,60],
            [27,60]
            ]

temp_qual = [[25, 600],
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
        

#temp = test_temp
temp = temp_qual

myTT.Initialize()   

time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(time.time()))


for t, d in temp:
    
    with open('temp.csv', 'ab') as log:
        logger = csv.writer(log)
        logger.writerow(['---test begin---'])
        
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
        
        
            
