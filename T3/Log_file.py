#u are given a log file that lists logon and logoff time for users of a system
#each has has 3 entries: username, logon time, logoff time
#times are in 24hr format and for a single work day
#wap that reads the file and prints all the users who were online for more than 1hr with display of the duration in hrs and mins
with open("D:\A1_MeetS\Python\T3\logfile.txt") as f:
    i=f.readlines()
    for j in i:
        k=j.split()
        logon=k[-2].split(":")
        logoff=k[-1].split(":")
        logon=int(logon[0])*60+int(logon[1])
        logoff=int(logoff[0])*60+int(logoff[1])
        if logoff-logon>60:
            print(k[0]+" was online for "+str((logoff-logon)//60)+":"+str((logoff-logon)%60))