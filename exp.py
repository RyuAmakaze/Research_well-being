import cv2
import time
import random
from record import MakeWavFile
from png import show,show_str
import csv
import datetime


#n is difficulty level.
def exp1(name,n,i):
    list = []
    show_str("start")
    time.sleep(3)
    cv2.destroyAllWindows()

    #record code record time is 3*n[s]
    #MakeWavFile("record/"+name+"_MemoTime_%d"%n+"_%d"%j+".wav",3*n)
    #subprocess.check_call(["python",MakeWavFile("record/"+name+"_MemoTime_%d"%n+"_%d"%j+".wav",3*n)])

    for k in range(n):
        if k==0:
            number = random.randrange(9)

        else:
            pre = number
            while pre == number:
                number = random.randrange(9)
        print(number)
        show(number)
        list.append(number)
        time.sleep(3)
        cv2.destroyAllWindows()


    show_str("end")
    time.sleep(2)
    cv2.destroyAllWindows()

    show_str("answer")
    now = datetime.datetime.now()
    answer_time = str(datetime.date.today()) + "-" + str(now.hour) + str(now.minute) + str(now.second)
    print("world time in answer : " + answer_time)
    MakeWavFile("record/"+name+"_Answer_%d"%n+"_%d"%i+".wav",n)
    cv2.destroyAllWindows()

    f = open("answer/"+name+"_TrueAns_%d"%n+"_%d"%i+".csv", 'w')
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(list)

    print("TureAns is " + str(list))
    print("difficulty level is %d"%n + "  how times is %d"%i)
    print("")

#難易度nの試行をj回行う
def exp2(name,n,j):
    for i in range (j):
        exp1(name,n,i)

    show_str("break")
    now = datetime.datetime.now()
    break_time = str(datetime.date.today()) + "-" + str(now.hour) + str(now.minute) + str(now.second)
    print("world time in break : " + break_time)
    time.sleep(20)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    name = "test"
    start_level = 4
    max_level = 11 #max_level-1 is max.
    times_exp = 10 #in the leble,times to play.

    t0 = time.time()
    now = datetime.datetime.now()
    start_time = str(datetime.date.today()) + "-" + str(now.hour) + str(now.minute) + str(now.second)
    print("start time is " + start_time)
    print("")


    show_str("freedom")
    time.sleep(10)
    cv2.destroyAllWindows()
    for x in range(max_level-start_level):
        exp2(name+"_1",x+start_level,times_exp)

    show_str("speech")
    time.sleep(30)
    cv2.destroyAllWindows()
    for level in range(max_level-start_level):
        exp2(name+"_2",x+start_level,times_exp)

    show_str("nospeech")
    time.sleep(30)
    cv2.destroyAllWindows()
    for x in range(max_level-start_level):
        exp2(name+"_3",x+start_level,times_exp)

    t1 = time.time()
    print(str(t1-t0))
    print("experiment finish.")
