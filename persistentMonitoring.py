# -*- coding: utf-8 -*-
#Version: 2.0.0

import urllib
import psutil
import os
import time
import sys
from PyQt4 import QtGui  
from PyQt4.QtGui import QMessageBox  
aplicacion = QtGui.QApplication(sys.argv)


i = 0
while i == 0:
	cpu = psutil.cpu_percent()	
	time.sleep( 1 )
	if cpu > 30.0:
			
			cpu = psutil.cpu_percent()
			os.system('netstat > net.html')
			scan = "net.html"
			lines = urllib.urlopen(scan).read()
			ip = (['104.20.209.59','185.170.115.65','164.132.200.121','104.25.6.31','104.24.104.76','104.18.55.211','104.27.185.32','158.69.252.241','165.227.198.137','85.17.26.66','104.31.93.36',
			'104.31.92.36','52.57.80.78','5.255.86.116','45.77.196.10','45.63.109.36','207.246.116.117','45.77.192.104','188.166.33.242','178.62.227.52','104.18.46.158','104.27.152.155','104.18.54.211',
			'185.183.156.241','104.20.208.59','217.182.164.14','37.187.167.70','37.187.165.17','37.187.165.41','37.187.165.207','37.187.165.210','37.187.166.108','37.187.167.21','37.187.167.30',
			'37.187.167.36','37.187.167.47','37.187.167.69','37.187.167.70','37.187.167.72','37.187.167.83','104.28.16.102','145.239.252.74','54.37.87.37','185.80.53.183','188.42.240.146',
			'176.9.51.167','35.190.24.124','185.193.38.148','165.227.10.77','207.246.117.237','206.189.24.193','104.28.15.29','109.230.199.214','212.32.255.7','212.32.255.210','35.184.61.56','45.32.172.211',
			'144.202.45.243','207.246.77.212','104.20.66.187','104.27.162.69','212.32.255.10'])
			
			for busqueda in ip:
				search = lines.find(busqueda)	
				if search != -1:
					QMessageBox.information(None, 'Persistent Monitoring NotMINING.org', u'Miner Detected: %s' %busqueda,
					QMessageBox.Ok,
					QMessageBox.Ok)
					
					break
			os.system('rm -rf net.html')			
			time.sleep( 10 )
			
				
