import calendar
import time
print ('plannig plant\n')
irspringer = 24*24
qlspringer = 14*8
total_seed = irspringer+qlspringer
grass = 30*100
cranb_main_g = irspringer*240
other_g = qlspringer*80
print ('main seed = ',irspringer)
print ('cranberry main G = ',cranb_main_g)
print ('secondary seed = ',qlspringer)
print ('other G = ',other_g)
print ('total seed = ',total_seed)
print ('grass = ',grass)
print ('\n')
print ('today is ',time.strftime("%Y-%m-%d"))
print (calendar.month(2016,5))
