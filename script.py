import pyautogui
import time 

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter") 
pyautogui.write("https://teste.com")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=655, y=474)
pyautogui.write("brunno@teste.com.br")
pyautogui.click(x=693, y=548) 
pyautogui.write("****")
pyautogui.click(x=694, y=613)
time.sleep(3)

