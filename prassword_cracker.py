from random import *
import os 
u_pwd = input("enter your passwoed: ")
pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

pw=""
while(pw!=u_pwd):
    pw=""
    for latter in range(len(u_pwd)):
        gauss_pwd = pwd[randint (0,35)]
        pw=str(gauss_pwd)+str(pw)
        print(pw)
        print("Cracking Password ..........Please")
        os.system("cls")
print("Your Password Is: ",pw)