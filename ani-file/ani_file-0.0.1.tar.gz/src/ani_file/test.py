from chunk import Chunk
import builtins
import struct
import ani_file
import wave
# my_ani = ani_file.open(".\\test_res\\aero_busy.ani")
# # my_ani.getframestofile()
my_ani = ani_file.open(".\\my_aero_busy.ani","wb")
my_ani.setframespath([".\\0.ico",".\\3.ico",".\\6.ico",".\\9.ico",".\\12.ico",".\\15.ico"])
my_ani.setauthor("EEVEE")
my_ani.setseq([0,1,0,2,0,3,0,4,0,5])
my_ani.setrate([2,4,6,8,10,12,14,16,18,20])
my_ani.close()

my_ani = ani_file.open(".\\my_aero_busy.ani","r")
print(my_ani.getseq())

# my_ani = Chunk(open(".\\my_aero_busy.ani","rb"),bigendian = 0)
# print(my_ani.getname)
# frame1 = my_ani.getframedata()[0]
# print(frame1)
# file = builtins.open(".\\test_output\\frame1.txt", "wb")
# file.write(frame1)
# file.close()
# print(type(my_ani))
# print(my_ani._seq)

# my_icon = open(".\\test_output\\lamy0.ico", "rb")
# my_ani = open(".\\test_output\\lamy0.ico", "w")
# my_ani = open(".\\test_res\\lamy_wait.ani","wb")
# my_ani.write(b"RIFF")

# my_ani.write(struct.pack("<4sI4s4s10I",b"RIFF",48,b"ACON",b"anih",36,36,8,45,0,0,0,0,8,3))
# my_ani.close()
# my_ani = open(".\\test_res\\lamy_wait.ani","rb")
# data = memoryview(my_ani).cast("B")
# print(len(my_ani.read()))
# my_ani = ani_file.open(".\\test_res\\lamy_wait.ani")
# my_ani.close()
# myString = 0
# print(myString.encode("utf-8"))
# print(my_ani.read())

# my_ani=ani_file.open(".\\test_res\\aero_busy.ani")
# print("nFrames is: ",my_ani.getnframes())
# print("nSteps is: ", my_ani._nSteps)
# print("seq is: ",my_ani.getseq())
# print("iname is: ",my_ani.getname())
# print("seq is: ",my_ani._seq)
# print("rate is: ", my_ani.getrate())

# import wave, struct, math, random
# sampleRate = 44100.0 # hertz
# duration = 1.0 # seconds
# frequency = 440.0 # hertz
# obj = wave.open('.\\test_res\\sound.wav','w')
# obj.setnchannels(1) # mono
# obj.setsampwidth(2)
# obj.setframerate(sampleRate)
# for i in range(99999):
#    value = random.randint(-32767, 32767)
#    data = struct.pack('<h', value)
#    obj.writeframesraw( data )
# obj.close()


#my_ani._iart
# print(my_ani.getframedata())
# my_ani.getframestofile(".\\test_output", "lamy")
# print(my_ani._bfAttributes)

#myframes = my_ani.getframesdata()

#print(type(myframes))
#print(len(myframes))
#new_file = open("test4.ico", "wb")
#new_file.write(myframes[0])
"""
print("-----------------------------------------")
list_chunk = my_ani._list_chunk
print(list_chunk.read())
print(list_chunk.getname())
print(list_chunk.getsize())

#ani_file.open(".\\test_res\\aero_busy.ani")



my_ani = builtins.open(".\\test_res\\lamy_wait.ani", 'rb')


#print(my_ani.read())
whole_chunk = Chunk(my_ani, bigendian = 0)
#print(whole_chunk.getname())
#print(whole_chunk.getsize())
whole_chunk.read(4)

#anih chunk
chunk = Chunk(whole_chunk, bigendian = 0)
#print(chunk.getname())
#print(chunk.getsize())
#print(chunk.tell())
cbSize, nFrames, nSteps, iWidth, iHeight, iBitCount, nPlanes, iDispRate, bfAttributes = struct.unpack_from("<9I", chunk.read(36))
#print(cbSize, nFrames, nSteps, iWidth, iHeight, iBitCount, nPlanes, iDispRate, bfAttributes)
#print(chunk.tell())
chunk.skip()

#LIST chunk
chunk = Chunk(whole_chunk, bigendian = 0)
print(chunk.getname())
print(chunk.getsize())
print(chunk.read(4))
#icon number 1
icon_chunk = Chunk(chunk, bigendian = 0)
print(icon_chunk.getname())
print(icon_chunk.getsize())
icon_data = icon_chunk.read(icon_chunk.getsize())
new_file = open("test.ico", "wb")
new_file.write(icon_data)
icon_chunk.skip()
#icon number 2
icon_chunk = Chunk(chunk, bigendian = 0)
print(icon_chunk.getname())
print(icon_chunk.getsize())
icon_data = icon_chunk.read(icon_chunk.getsize())
new_file = open("test2.ico", "wb")
new_file.write(icon_data)
icon_chunk.skip()
#icon number 3. Last one
icon_chunk = Chunk(chunk, bigendian = 0)
print(icon_chunk.getname())
print(icon_chunk.getsize())
icon_data = icon_chunk.read(icon_chunk.getsize())
new_file = open("test3.ico", "wb")
new_file.write(icon_data)
icon_chunk.skip()


#seq chunk
chunk.skip()
chunk = Chunk(whole_chunk, bigendian = 0)
print(chunk.getname())
print(chunk.getsize())
"""