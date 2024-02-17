from drone import drone
 
drone=drone()
drone.connect()
#trim(Roll,Pitch,Throttle,Yaw)
drone.trim(0,0,0,0)
drone.get_mag_x()

#drone.disarm()
#drone.takeoff()
#print("Increasing throttle speed") 
#drone.throttle_speed(2,3) #(value, Duration)
#drone.land()
#drone.disarm()
