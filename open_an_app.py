#D1
#This python code will open the application & break every 2 hours for 3 times.
import webbrowser
import time
total_breaks=3
break_count=0
while(break_count<total_breaks):
#During the sleep period (5sec), the program does nothing except for waiting. 
#The sleep command doesn't "close" the application or make the program stop.
#The program remains active in the background, but it doesn't execute any further actions 
#until the sleep time is over    
    time.sleep(5)
    webbrowser.open_new("https://www.youtube.com/")
    break_count+=1;