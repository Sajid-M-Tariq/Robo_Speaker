# imports
import os


# Main code
if __name__ == '__main__' :
    print('Welcome to RoboSpeaker 1.1 created by Sajid')
    while True:
        x = input("What you want to speak:")
        if x == "q" :
            command = f"say {'Powering off'}"
            os.system(command)
            break
        command = f"say {x}"
        os.system(command)









