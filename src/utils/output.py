import eel

graphInterface = True

def output(*msg):
    if graphInterface:
        eel.output(msg)
    
    print(msg)
    

def checkBtn():
    if not graphInterface:
        return

    eel.enableButton()
        
