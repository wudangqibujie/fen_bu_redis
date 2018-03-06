from master import Clawer
import slav1_spiders
import slav2_spiders
import time

t1 = time.time()
Clawer()
slav2_spiders.slave_2()
slav1_spiders.slave_1()
t2 = time.time()
print("爬取用时:%f"%(t2-t1))
# slav2_spiders.slave_2()

