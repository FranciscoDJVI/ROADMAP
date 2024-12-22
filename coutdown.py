import threading
import datetime  
from time import sleep
import os

# Fecha inicial ingresado por el usuario.
final_date = input("\nIntroducce la fecha inicial dd/mm/aa hh:mm:ss ")

# Función para realizar la cuenta regresiva tomando la fecha ingresada por el usuario hasta la fecha acutal.
def countdown():
    final_date_format = datetime.datetime.strptime(final_date, "%d/%m/%Y %H:%M")
    fecha_now= final_date_format.now()
    total = final_date_format - fecha_now 
        
    print("Cuenta regresiva para el lanzamiento de Mouredev Pro...")
    print(f"Faltan {total.days} dias, {total.seconds // 3600} horas, {total.seconds // 60 % 60} minutos, {total.seconds % 60} segundos") 
        
    sleep(1)
        
    os.system("cls")

    if total.days == 00 and total.seconds == 00:
        print("Ha llegado el dia")
    else:
        countdown()


#07/11/2024 20:45:00

thread = threading.Thread(target=countdown)
thread = threading.Thread.start(thread)
thread = threading.Thread.join()
