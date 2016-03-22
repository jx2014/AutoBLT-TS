import win32api, win32con
import time
import msvcrt


class BLTAuto():
    def __init__(self):
        self.startX = 0
        self.startY = 0
        self.clearX = 0
        self.clearY = 0
        self.nofTest = 3
        pass

    def Click(self):
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.2)
        
    def MoveTo(self,x2,y2, delay=0.001):
        timeout = 10 #10seconds for time out
        # get current location
        x, y = win32api.GetCursorPos()    
        
        t = time.time()
        n = 0
        while ((x != x2 or y != y2) and time.time() - t <= timeout):                
            n += 1
            if x < x2:
                x += 1
            elif x > x2:
                x -= 1
            
            if y < y2:
                y += 1
            elif y > y2:
                y -= 1
            
            if n % 3 == 0:
                time.sleep(delay)        
            win32api.SetCursorPos((x, y))
    
    def GoToStart(self):
        time.sleep(0.1)
        self.MoveTo(self.startX, self.startY)       
    
    def GoToClear(self):        
        time.sleep(0.1)
        self.MoveTo(self.clearX, self.clearY)
    
    def GetStartLoc(self):
        raw_input("Place mouse cursor at center of Start button and press Enter key to continue...")
        self.startX, self.startY = win32api.GetCursorPos()
        print 'Start button coordinates  (%d, %d)' % (self.startX, self.startY)
            
    def GetClearLoc(self):
        raw_input("Place mouse cursor at center of Clear button and press Enter key to continue...")
        self.clearX, self.clearY = win32api.GetCursorPos()
        print 'Clear button coordinates (%d, %d)' % (self.clearX, self.clearY)
    
    def DetectKey(self, timeout = 10):
        print 'Press q to stop at anytime\n'
        t = time.time()
        while (time.time() - t <= timeout):
            if msvcrt.kbhit():
                chr = msvcrt.getche()
                if chr == 'q':                    
                    exit()
            
    
    def __del__(self):
        print '\ngood bye!'
                
    
    # send control shift click
    def SendCSC(self):
        #d = int('0x44', 16)
        #d_scan = int('0x20', 16)
        
        #p = int('0x46', 16)
        #p_scan = int('0x19',16)
        
        #left control
        lcontrol = int('0xa2', 16)
        lcontrol_scan = int('0x1d', 16)
        
        #left shift
        lshift = int('0xa0', 16)
        lshift_scan = int('0x2a', 16)
        
        release = 2
        extend_scan_code=1
                
        time.sleep(0.2)
        win32api.keybd_event(lshift, lshift_scan)
        win32api.keybd_event(lcontrol, lcontrol_scan)
        time.sleep(0.2)
        #win32api.keybd_event(d, d_scan)
        self.Click()
        time.sleep(0.2)
        win32api.keybd_event(lshift, lshift_scan, release)
        win32api.keybd_event(lcontrol, lcontrol_scan, release)
        #win32api.keybd_event(d, d_scan)
        #win32api.keybd_event(p, p_scan)
    
    def NoOfTests(self):
        self.nofTest = raw_input("Enter the no of tests you wish to run (enter 999 to test forever until quit): ")
        self.nofTest = int(self.nofTest)
        
    
    def StartTest(self):
        self.NoOfTests()
        self.GetStartLoc()
        self.GetClearLoc()
        
        print 'Very good, now click on on BLT desktop to active it and sit back and relax'
        
        print 'number of tests: %d' % self.nofTest
        
        for i in range(10,0,-1):
            print 'test will begin in %d' % i
            time.sleep(1)
            
        i = 1        
        while self.nofTest > 0:            
            print 'test #%d' % i
            self.GoToStart()
            self.Click()
            self.DetectKey(timeout=60) 
            self.GoToClear()
            self.SendCSC()
            if self.nofTest <= 999:                             
                self.nofTest -= 1        
            i += 1
            
        
        
    
    
    
    
    