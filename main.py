import pywhatkit as pwk
#this
i = 5
while(i != 0):
    pwk.sendwhatmsg_instantly('+917230815261', 'Lets goooooo')
    #pwk.sendwhatmsg('+917230815261', 'Tatti Khaale',12,54)
    print("Successfully Sent!")
    i = -1
    
#below are the functions of pywhatkit
 
#import pywhatkit
#
## Send a WhatsApp Message to a Contact at 1:30 PM
#pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)
#
## Same as above but Closes the Tab in 2 Seconds after Sending the Message
#pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)
#
## Send an Image to a Group with the Caption as Hello
#pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")
#
## Send an Image to a Contact with the no Caption
#pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")
#
## Send a WhatsApp Message to a Group at 12:00 AM
#pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)
#
## Send a WhatsApp Message to a Group instantly
#pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")
#
## Play a Video on YouTube
#pywhatkit.playonyt("PyWhatKit")
