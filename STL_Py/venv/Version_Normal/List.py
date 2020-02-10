from vehicle_detection_main1 import camera1
from vehicle_detection_main2 import camera2
from vehicle_detection_main3 import camera3
from vehicle_detection_main4 import camera4






import threading
















   







def main():
    
     # creating thread
    t1 = threading.Thread(target=camera1)
    t2 = threading.Thread(target=camera2)
 
    # starting thread 1
    t1.start()
    print("t1 started")
    print(t1)
    # starting thread 2
    t2.start()
    print("t2 started")
    print(t2)
    
    # wait until thread 1 is completely executed
    t1.join()
    print(t1)
    # wait until thread 2 is completely executed
    t2.join()
    print(t2)

    
    
    L=[]
   # a=camera1()
   # b=camera2()
   # c=camera3()
    #d=camera4()


    L=[10,15,20,5]
    

    return L

if __name__ == "__main__":
    main()
