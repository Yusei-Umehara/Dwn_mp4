import pytube
import pyautogui as robot
import time

navegador= input("Cual es tu navegador")
tu_video = input("Que video deseas descargar?")
yutuBar = 700, 130
posVideo = 461, 319

#Funcion para abrir
def abrir (pos, click = 1):
    robot.moveTo(pos)
    robot.click(clicks=click)

#Abrir youtube
robot.hotkey("Win","s")
time.sleep(1)
robot.typewrite(navegador)
time.sleep(1)
robot.hotkey("enter")
time.sleep(2)
robot.hotkey("ctrl","l")
time.sleep(0.5)
robot.typewrite("youtube.com")
time.sleep(1)
robot.hotkey("enter")
time.sleep(4)

abrir(yutuBar, click=2)
time.sleep(1)
robot.typewrite(tu_video)
time.sleep(2)
robot.hotkey("enter")
time.sleep(4)
abrir(posVideo, click=2)
time.sleep(2)
robot.hotkey("ctrl","l")
robot.hotkey("ctrl","x")

#debes regresar manualmente a insertar la url + enter para completar el proceso

url = input("Inserte la url del video:")
youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download()


