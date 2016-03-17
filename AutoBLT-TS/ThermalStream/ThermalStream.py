import visa
import binascii
import winsound
import time
import datetime


rm = visa.ResourceManager()

class ThermalStream():
    def __init__(self,gpib_port, dwell=3600, ):
        gpib = 'GPIB0::' + str(gpib_port) + '::INSTR'
        print '{0:30}: {1}'.format('GPIB port', gpib)
        self.TT = rm.open_resource(gpib)
        
        self.soundFile = r'C:\Users\RMA\My Documents\LiClipse Workspace\ThermalStream\sound.wav'
                
        self.PrintInfo()
    
    def PrintInfo(self):   
        
        print '{0:30}: {1}'.format('DeviceName', self.WhoAmI())
        print '{0:30}: {1}c'.format('Air to Dut', self.GetAirToDut())
        print '{0:30}: {1}'.format('Auxiliary', self.GetAuxiliary())
        print '{0:30}: {1}'.format('Compressor', self.GetCompressor())
        print '{0:30}: {1}'.format('DUT Sensor type:', self.GetDutSensor())
        print '{0:30}: {1}'.format('Device Thermal constant', self.GetDutConstant())
        print '{0:30}: {1}'.format('DUT Mode:', self.GetDutMode())
        print '{0:30}: {1}'.format('Error Code', self.GetError())
        print '{0:30}: {1}'.format('Main air flow', self.GetFlow())
        print '{0:30}: {1} scfm or {2} l/s'.format('Current air flow:', self.GetFlowRateSCFM(), self.GetFlowRateLS())
        print '{0:30}: {1}'.format('Thermal head', self.GetThermalHead())
        print '{0:30}: {1}c'.format('Lower limit', self.GetLowLimit())
        print '{0:30}: {1}c'.format('Upper limic', self.GetUpperLimit())
        print '{0:30}: {1}'.format('SetPoint Mode', self.GetMode())
        print '{0:30}: {1}'.format('Current Temperature Event', self.GetTempEvent())
        print '{0:30}: {1}'.format('Ramp rate', self.GetRampRate())
        print '{0:30}: {1}'.format('SetPoint Instant', self.GetSetpointD())
        print '{0:30}: {1}'.format('TargetSet point', self.GetTargetTempSetPoint())        
        #print '{0:30}: {1}'.format('Temp', self.GetTemp())
        print '{0:30}: {1}'.format('Air temperature', self.GetAirTemp())
        print '{0:30}: {1}'.format('Dut tempreature', self.GetDutTemp())
        print '{0:30}: {1}'.format('Soak', self.GetSoak())
        print '{0:30}: {1}'.format('Setpoint Window', self.GetSetpointWindow())
        print '{0:30}: {1}'.format('What is it doing', self.GetWhat())        
    
    def CurrentInfo(self):
        print '{0:30}: {1}'.format('Thermal head', self.GetThermalHead())
        print '{0:30}: {1}'.format('Main air flow', self.GetFlow())
        print '{0:30}: {1}'.format('Ramp rate', self.GetRampRate())
        print '{0:30}: {1} scfm or {2} l/s'.format('Current air flow:', self.GetFlowRateSCFM(), self.GetFlowRateLS())
        print '{0:30}: {1}'.format('Ramp rate', self.GetRampRate())        
        print '{0:30}: {1}'.format('SetPoint Mode', self.GetMode())        
        print '{0:30}: {1}'.format('TargetSet point', self.GetTargetTempSetPoint())
        print '{0:30}: {1}'.format('Current Temperature Event', self.GetTempEvent())
        print '{0:30}: {1}'.format('Air temperature', self.GetAirTemp())
        print '{0:30}: {1}'.format('Dut tempreature', self.GetDutTemp())
    
    def CurrentInfoShort(self):
        print 'Setpoint: {0}, Dut: {1}, Air: {2}, Flow: {3}scfm'.format(self.GetTargetTempSetPoint(), 
                                                                    self.GetDutTemp(), 
                                                                    self.GetAirTemp(),
                                                                    self.GetFlowRateSCFM())
                
    
    def Ask(self, command):
        return self.TT.query(command).rstrip().encode('ascii', 'ignore')
    
    def Write(self, command):
        self.TT.write(command)
        
    def WhoAmI(self):
        #result = self.Ask('*IDN?').rstrip()
        return self.Ask('*IDN?')
        #return result
    
    def GetAirToDut(self):
        #result = self.Ask('ADMD?').rstrip()
        return self.Ask('ADMD?')        
        #return result
    
    def GetAuxiliary(self):
        #result = self.Ask('AUXC?').rstrip()
        result = self.TT.query('AUXC?')
        #return bin(int(result))
        return int(result)
        #return result
    
    def GetCompressor(self):
        result = self.Ask('COOL?')        
        if result == '1':
            return 'On'
        elif result == '0':
            return 'Off'
        else:
            return 'Unknown'
    
    def GetDutSensor(self):
        result = self.Ask('DSNS?')
        if result == '0':
            return 'No Sensor'
        elif result == '1':
            return 'type T thermocouple'
        elif result == '2':
            return 'type K thermocouple'
        else:
            return 'unknown type'
    
    def GetDutConstant(self):
        return self.Ask('DUTC?')

    def GetDutMode(self):
        result = self.Ask('DUTM?')
        if result == '0':
            return 'Air controlled'
        elif result == '1':
            return 'Ext. Sensor controlled'
        else:
            return 'Unknown mode'
    
    def GetError(self):
        result = self.Ask('EROR?')
        return result
    
    def GetFlow(self):
        result = self.Ask('FLOW?')        
        if result == '0':
            return 'Off'
        elif result == '1':
            return 'On'
        else:
            return 'unknown'
    
    def GetFlowRateSCFM(self):
        result = self.Ask('FLWR?')        
        return result
    
    def GetFlowRateLS(self):
        result = self.Ask('FLRL?')        
        return result
    
    def GetThermalHead(self):
        result = self.Ask('HEAD?')
        if result == '0':
            return 'Head is up'
        elif result == '1':
            return 'Head is down'
        else:
            return 'Unknown'
    
    def SetThermalhead(self, position):        
        if position == 'up':            
            self.Write('STND 0')
        elif position == 'down':
            self.Write('STND 1')
        else:
            print 'invalid input, use \'up\' or \'down\''
    
    def GetLowLimit(self):
        self.lowerlimit = int(self.Ask('LLIM?'))
        return self.lowerlimit
    
    def GetUpperLimit(self):
        self.upperlimit = int(self.Ask('ULIM?'))
        return self.upperlimit
    
    def SetLowerLimit(self, lower):
        if lower > -99 and lower < 25:
            print 'old lower limit ', self.GetLowLimit()
            command = 'LLIM %d' % lower
            self.Write(command)
            print 'new lower limit ', self.GetLowLimit()
        else:
            print 'lower limit must be with in -99 to +25C'
            
    def SetUpperLimit(self, upper):
        if upper < 225 and upper > 25:
            print 'old upper limit ', self.GetUpperLimit()
            command = 'ULIM %d' % upper
            self.Write(command)
            print 'new upper limit ', self.GetUpperLimit()
        else:
            print 'upper limit must be with in +25 to +225C'
        
    
    def GetRampRate(self):
        result = self.Ask('Ramp?')
        result = float(result) * 10
        return int(result) 
    
    def GetSetpointD(self):
        return self.Ask('SETD?')
    
    def GetMode(self):
        result = self.Ask('SETN?')
        if result == '0':
            return 'Hot'
        elif result == '1':
            return 'Ambient'
        elif result == '2':
            return 'Cold'
        else:
            return 'unknown setpoint %s' % result
    
    def GetTempEvent(self):
        result = int(self.Ask('TECR?'))
        if result == 1:
            return 'at temperature'
        elif result == 2:
            return 'not at temperature'
        else:
            return 'unknown event: %d' % result
               
    
    def SetMode(self, setpoint):
        if setpoint not in ['hot', 'cold', 'ambient']:
            print 'invalid set point, must be hot, ambient or cold' 
        else:
            #self.Write('RSTO')            
            if setpoint == 'hot':
                self.Write('SETN 0')
            elif setpoint == 'ambient':
                self.Write('SETN 1')
            elif setpoint == 'cold':
                self.Write('SETN 2')      
         
            
    
    def GetTargetTempSetPoint(self):
        return self.Ask('SETP?')
    
    def SetTargetTempSetpoint(self, setpoint):
        if setpoint < self.upperlimit or setpoint >= self.lowerlimmit:
            self.Write('SETP %d' % setpoint)
        else:
            print 'target tempeature must be within %d, %d' % (self.lowerlimit, self.upperlimit)
    
    def GetSoak(self):
        return self.Ask('SOAK?')
    
    def GetTemp(self):
        return self.Ask('TEMP?')

    def GetAirTemp(self):
        return self.Ask('TMPA?')
    
    def GetDutTemp(self):
        return self.Ask('TMPD?')

    def GetSetpointWindow(self):
        return self.Ask('WNDW?')
    
    def SetSetpointWindow(self, window):
        if window < 10 or window > 0:
            self.Write('WNDW %d' % window)
        else:
            print 'Invalid window setpoint, must between 0.1 to 9.9'
    
    def GetWhat(self):
        result = self.Ask('WHAT?')
        if result == '5':
            return 'Operator Screen'
        elif result == '6':
            return 'Cycle screen'
        else:
            return 'Unknown %s' % result     
    
    def SetRampRate(self, rate):
        command = 'RAMP %d' % (rate)
        self.Write(command)
    
    def SetFlowOn(self):
        self.Write('Flow 1')
    
    def SetFlowOff(self):
        self.Write('Flow 0')
    
    def Initialize(self):
        self.Write('RSTO')
        self.SetMode('ambient')
        self.SetFlowOn()
        self.SetThermalhead('down')
        self.CurrentInfo()
        
    def GetTimeStamp(self):        
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d, %H:%M:%S')
        return timestamp
    
    def PlaySound(self):
        winsound.PlaySound(self.soundFile, winsound.SND_ASYNC | winsound.SND_LOOP)
    
    def StopSound(self):
        winsound.PlaySound(None, winsound.SND_ASYNC)
    
        
    
    def GoToTemp(self, temp):
        mode = None
        if temp > 25:
            mode = 'hot'
        elif temp < 25:
            mode = 'cold'
        elif temp == 25:
            mode = 'ambient'
        else:
            print 'Unknown mode'            
        
        print self.GetTimeStamp()
        ts = time.time()
        self.SetMode(mode)
        self.SetRampRate(9)
        self.SetTargetTempSetpoint(temp)        
        self.SetFlowOn()
        self.SetThermalhead('down')
        self.CurrentInfo()
        
        status = self.GetTempEvent()
        while self.GetTempEvent() == 'not at temperature':
            self.CurrentInfoShort()            
            print '{0} {1}'.format(self.GetTempEvent(), '...wait 10 secs...\n')
            time.sleep(10)
        
        if self.GetTempEvent() == 'at temperature':            
            self.CurrentInfoShort()
            print 'at temperature'
            self.CurrentInfo()
            print self.GetTimeStamp()
            print 'took %s secs to reach setpoint' % (time.time() - ts)
            self.PlaySound()            
            raw_input("Press Enter to continue...")
            self.StopSound() 
        else:
            print self.GetTempEvent()
    
    def Dwell(self, duration): #with half time warning
        ts = time.time()
        halftime = duration/2
        while (time.time() - ts) < (halftime):
            self.CurrentInfoShort()
            print 'Dwell for %s secs... %s secs left till halftime..\n' % (duration, halftime - int(time.time() - ts))            
            time.sleep(10)
        
            if time.time() - ts > halftime:
                self.PlaySound()
                print 'halftime has reached'
                time.sleep(3)
                raw_input("Press Enter to continue...")
                self.StopSound()
        
        while (time.time() - ts) < duration:
            self.CurrentInfoShort()
            print 'Dwell for %s secs... %s secs left..\n' % (duration, duration - int(time.time() - ts))            
            time.sleep(10)
        
            if time.time() - ts > duration:
                self.PlaySound()
                print 'Dwell for {0}seconds has reached'.format(duration)
                time.sleep(3)
                raw_input("Press Enter to continue...")
                self.StopSound()
        
        
            
        
            
            
        
        
        
        
        
            
        
        
    
    