import eel
import os

graphInterface = os.environ.get('GRAPH_INTERFACE')

def output(*msg):
    if graphInterface:
        eel.output(msg)
    
    print(msg)
    

def checkBtn():
    if not graphInterface:
        return

    eel.enableButton()
        
