#
# WS2812B * 8ea Full Color LED 1-wire Control 
# Ver.0.0.1 code by Young Sik Kim 

import time
import spidev

class ws2812B():
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0,1)  # (device[0,1], Chip select[0,1])
        self.spi.mode = 0b01
        self.spi.max_speed_hz = 800000
        
    # time set : 최소: 4/1.05e-6 (Hz) => 653us
    def clear(self):
        bx=[]
        for i in range(96):
            bx.append(0x88)
        
        self.spi.xfer(bx, int(4/1.05e-6))
        time.sleep(0.001)
    
    def LinearOn(self,n, r_data,g_data,b_data):
        nLED = int(n)
        rx_data = [[g_data,r_data,b_data]*nLED]
        tx=[]
        for rgb in rx_data:
            for byte in rgb: 
                for ibit in range(3,-1,-1):
                    #print ibit, byte, ((byte>>(2*ibit+1))&1), ((byte>>(2*ibit+0))&1), [hex(v) for v in tx]
                    tx.append(((byte>>(2*ibit+1))&1)*0x60 +
                            ((byte>>(2*ibit+0))&1)*0x06 +
                            0x88)
        #print [hex(v) for v in tx]
        self.spi.xfer(tx, int(4/1.05e-6))
        time.sleep(0.002)
        
    def middle(self,s,n, r_data,g_data,b_data):
        sLED = int(s)
        rx_data = [[0,0,0]*sLED]
        nLED = int(n)
        for i in range(sLED,nLED):
            rx_data.append([g_data,r_data,b_data])
        for i in range(nLED,10):
            rx_data.append([0,0,0])
            
        tx=[]
        for rgb in rx_data:
            for byte in rgb: 
                for ibit in range(3,-1,-1):
                    #print ibit, byte, ((byte>>(2*ibit+1))&1), ((byte>>(2*ibit+0))&1), [hex(v) for v in tx]
                    tx.append(((byte>>(2*ibit+1))&1)*0x60 +
                            ((byte>>(2*ibit+0))&1)*0x06 +
                            0x88)
        self.spi.xfer(tx, int(4/1.05e-6))
        time.sleep(0.002)
