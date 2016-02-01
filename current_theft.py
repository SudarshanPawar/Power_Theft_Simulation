# Electricity Theft Simulation
# Automated inputs & based on those inputs the results are returned!

import random
import datetime
now=datetime.datetime.now()
records=[]
#sanctioned_connections=['A','B','C']

status_1="CONNECTION STABLE"
status_2="POWER THEFT OR EXTREME POWER CONSUMPTION. CHECK THE SITE!"
status_3="CONNECTION FAILURE,CHECK THE CONNECTIONS"
status_4="Low Power Consumption!"
while True:
    threshold_value= random.randrange(200,500)

    continue_checking=raw_input("Check Consumption Status? Y /N ")
    def detection():
  
        if threshold_value==300:
            print "CURRENT CONSUMED: '",threshold_value,"' Amp."
            print status_1
            records.append(threshold_value,status_1)
        elif threshold_value > 350:
            print "CURRENT CONSUMED: '",threshold_value,"' Amp."
            print status_2
        elif threshold_value<200:
            print "CURRENT CONSUMED: '",threshold_value,"' Amp."
            print status_3
        else:
            print "CURRENT CONSUMED: '",threshold_value,"' Amp."
            print status_4
    if continue_checking=='Y' or continue_checking=='y':
        detection()
    else:
        target = open("logs.txt", 'w')
        target.write("CURRENT MONITORING RESULTS")
        target.write("\n")
        target.write(str(now))
        records.append(threshold_value)
        target.write(threshold_value)
        target.close()
        #print "Incorrect input! Program Exited..."
        break

