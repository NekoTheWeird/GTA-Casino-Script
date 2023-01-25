from cProfile import label
from time import sleep
import keyboard
import mouse
from win32 import win32gui
import win32con, win32com.client
import threading
import os

print("-/--/-//Made by IamNekoGirl and AidyTheWeird//-/--/\n-/--/--/-//This script is free of charge//-/--/--/-\n-/--/--/--/-//Only from UnknownCheats//-/--/--/--/-\n")
print("Consider supporting my work on Ko-Fi!")
print("ko-fi.com/iamnekogirl\n")
sleep(2)
print("------------------------------------------\n|\Please enter the window name of GTAHaX/|\n------------------------------------------")
#Print print print omg so much print




gtaWindow = win32gui.FindWindow("grcWindow", "Grand Theft Auto V") 
gtahax = win32gui.FindWindow(None, input()) #fuck this shit, i guess it works
shell = win32com.client.Dispatch("WScript.Shell")
ScriptActive = True


# Makes the script into a function cuz idk
def MainFunction():
	shell.SendKeys('%')
	win32gui.SetForegroundWindow(gtaWindow)
	sleep(0.2)
	keyboard.press_and_release('enter')
	win32gui.SetForegroundWindow(gtahax)
	win32gui.SetWindowPos(gtahax, None, 0, 0, 0, 0, win32con.SWP_NOSIZE)
	sleep(0.25)
	mouse.move(100, 525, absolute=True)
	mouse.click()
	mouse.click()
	sleep(1)
	return
	print("FUCK ME")
	sleep(5)
	print("5 SECONDS NO FUCK BROOOOOO")
	return



#keyboard.wait("b")			#Depricated



# GTA and HAX open check

if gtaWindow == 0:
	print("GTA V window not found. Are you sure you started the game? (Or i fucked up somehow...)")
	sleep(3)
	exit()	
elif gtahax == 0:
	print("GtaHax Window not found. Is it open? Or did i fuck up somewhere...")
	sleep(3)
	exit()
else:
	print("Game Window: ", gtaWindow)
	print("GTAHaX Window: ", gtahax)
	print("Script is ready to start.\nPress F1 when ready.")
	keyboard.wait("f1")
	print ("----------------------\nStarting in 5 seconds... :)\n----------------------")
	print("You can press F2 to pause and F1 to resume again.\nAlso F3 exits the script completely.")
	sleep(5)


# Makes a thread that checks if F1/F2/F3 has been pressed. If yes the script should die.. eventually.
def thread1():
	while True:
		global ScriptActive
		lock = threading.Lock()
		if keyboard.is_pressed('f2'):
			with lock:
				ScriptActive = False
				sleep(0.1)
				print("Pausing! Please wait and pray. Press F1 to resume again or F3 to exit.")
		elif keyboard.is_pressed('f1'):
			with lock:
				ScriptActive = True
				sleep(0.1)
				print("Letsgoooo runnin again.")
		elif keyboard.is_pressed('f3'):
			with lock:
				print("Okay bye :)")
				sleep(2)
				os._exit(1)



threading.Thread(target = thread1).start()

# Runs the script forever. Or until universe ends.... or until F2/F3 is pressed. Whichever comes first.
def ScriptusMechanicus():
	while ScriptActive:
		MainFunction()

while True:
	ScriptusMechanicus()


	
