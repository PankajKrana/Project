import os

if __name__ == '__main__':
    print("Welcome to robospeaker 1,0 creatd by me ")
    while True:
        x= input("enter what you want to speak : ")
        if x=="q":
            os.system("say 'bye bye frand' ")
            break
        command=f"say {x}"
        os.system(command)