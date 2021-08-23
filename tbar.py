# Taskbar IP list
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from netifaces import interfaces, ifaddresses, AF_INET  
from requests import get
import os
  
def mebar():  
	app = QApplication([])
	app.setQuitOnLastWindowClosed(False)
	# Adding an icon
	icon = QIcon("icong.png")
	# Adding item on the menu bar
	tray = QSystemTrayIcon()
	tray.setIcon(icon)
	tray.setToolTip("IP List")
	tray.setVisible(True)
	#Find addresses and interfaces
	menu = QMenu()
	for ifaceName in interfaces():
		addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
	#    print('%s: %s' % (ifaceName, ', '.join(addresses)))
		menu.addAction(ifaceName.ljust(15,)+"\t"+ifaceName.join(addresses))
	# To quit the app
	extip=get('https://api.ipify.org').text
	wanip=QAction("wanip".ljust(15,)+"\t"+extip)
	menu.addAction(wanip)
	quit = QAction("Quit")
	quit.triggered.connect(app.quit)
	menu.addAction(quit)
	menu.addAction("") # makes a blank space for clarity
	  
	# Adding options to the System Tray
	tray.setContextMenu(menu)
	  
	app.exec_()
	
if __name__ == '__main__':
	mebar()
	
