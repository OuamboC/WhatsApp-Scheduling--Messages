import pywhatkit as kit 
import pyautogui
import time
import pygetwindow as gw

# Using Exception Handling to avoid 
# uncprecented errors
try:
    phone_no = str(input("Enter phone number: ")) # The recipient's phone number, including the country code.
    message = str(input("Enter message: ")) # The message you want to send.
    time_hour = int(input("Enter hour 0-24: ")) # The hour (24-hour format) at which you want to send the message.
    time_min = int(input("Enter minutes 00-59: ")) # The minutes at which you want to send the message
    wait_time = 20 # The time in seconds before sending the message once the browser is opened (default is 20 seconds).
    tab_close_time = 20 # The time in seconds before closing the browser tab after the message is sent (default is 20 seconds).
    # Sending message to receiver 
    # using pywhatkit
    kit.sendwhatmsg(phone_no, message, time_hour, time_min, wait_time, tab_close_time)

    # Adding a delay to allow WhatsApp Web to load the messge
    time.sleep(5)

    # Bring the browser window to the front 
    browser_window = gw.getWindowsWithTitle('WhatsApp')[0]
    browser_window.activate()
    
    #Pressing 'Enter' to send the message
    pyautogui.press('enter')

    print ("Successfully Sent!")
    


except Exception as e:
    # Handling Exception and printing error messgae
    print(f"An Unexpected Error: {e}")
    

    