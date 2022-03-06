# -*- coding: utf-8 -*-

gua8 = dict()
gua8['坤'] = 0b000
gua8['艮'] = 0b100
gua8['坎'] = 0b010
gua8['巽'] = 0b110
gua8['震'] = 0b001
gua8['离'] = 0b101
gua8['兑'] = 0b011
gua8['乾'] = 0b111

w = dict()
w['坤'] = 8000 
w['艮'] = 9000 
w['坎'] = 10000 
w['巽'] = 11000 
w['震'] = 12000 
w['离'] = 13000 
w['兑'] = 14000 
w['乾'] = 15000 


#src, cmd是八卦字符
def get_chksum(src, cmd):
    if gua8.has_key(src) and gua8.has_key(cmd):
        tmp = (gua8[src] ^ gua8[cmd]) + 11	
 	chksum = (w[src] + tmp)%8
	print(gua8[src],gua8[cmd],w[src], tmp, chksum)
	for k,v in gua8.items():
	    if v == chksum:
		return k
    return ''
    
up 		= ['兑','离','离','乾','震','艮','艮','兑','乾','坤','兑','巽','坎','坎','艮','震','坤','坤','离','乾','乾','乾','乾']
down_left 	= ['离','巽','巽','兑','坤','艮','巽','离','震','艮','兑','巽','震','兑','巽','兑','坎','震','兑','兑','兑','兑','坤']
weight = 93.75

down = []
down2 = []
for si in range(0,len(up)):
    chk = get_chksum(up[si], down_left[si])
    down.append(down_left[si]+chk) 
for s in down:
    print s.decode('utf-8')

#获取救援指令chksum
s = get_chksum('乾','坎')
print(s.decode('utf-8'))
