import eel
import os

from src.config import configVar

graphInterface = configVar['graphInferface']

def output(*msg):
    if graphInterface:
        eel.output(msg)
    
    print(msg)
    

def checkBtn():
    if not graphInterface:
        return

    eel.enableButton()
        

@eel.expose
def stop_search():
    if not graphInterface:
        return

    output("Habilitando botão...")
    # eel.enableButton()