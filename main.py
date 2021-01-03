from random import randrange
import time

maclauring_series_keys = ["ln(1+x)","e^x","sinx","cosx","arctanx","ln(1-x)","e^(-x)"]
maclauring_series_values = ["x - x^2/2 + x^3/3 ","1 + x + x^2/2 + x^3/6","x - x^3/6","1 - x^2/2","x - x^3/3","-x - x^2/2 - x^3/3","1 - x + x^2/2 - x^3/6"]
maclauring_series = {
    "ln(1+x)" : "x-x^2/2+x^3/3",
    "e^x" : "1+x+x^2/2+x^3/6",
    "sinx": "x-x^3/6",
    "cosx": "1-x^2/2",
    "arctanx": "x-x^3/3",
    "ln(1-x)": "-x-x^2/2-x^3/3",
    "e^(-x)":"1-x+x^2/2-x^3/6"
}



done = False
X = 0

while not done : 
    
    random = randrange(7)
    key = maclauring_series_keys[random]
    answers_left = 10 - X

    print(str(answers_left) +" right answers left")
    print(key)
    print("")
    answer = input("")
    print("")
    if answer.replace(" ","")==maclauring_series[key] :
        X=X+1

        print("you got it right")
        print("")
    else :
        print("wrong"+" the right answer is: ")
        print(maclauring_series_values[random])
        print("")
        X=X-1
    if X==10 :
        done=True
  
