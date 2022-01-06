#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:58:06 2022

@author: aditisathe
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:18:08 2022

@author: aditisathe
"""





import pandas as pd
from datetime import datetime
from collections import Counter


name = []
status = []
timestamp = []
date = []
time = []
new_time = []
final_time = []

name_count = 0


duration = '00:00:00'
duration_datetime = datetime.strptime(duration, "%H:%M:%S")



# Opening the text file and storing its contents into 'content'
file = open('a_list.txt', encoding = "utf16", errors = 'ignore')
content = file.readlines()




# Taking the user's input - meeting start and end times
meet_start_time = str(input('Enter meeting start time (hh:mm:ss): '))
meet_start_time_datetime = datetime.strptime(meet_start_time, "%H:%M:%S")

meet_end_time = str(input('Enter meeting end time (hh:mm:ss): '))
meet_end_time_datetime = datetime.strptime(meet_end_time, "%H:%M:%S")



# Splitting each row into its component terms
for i in range(0, len(content)):
    split_list = content[i].split('\t')
    #print(split_list)
    name.append(split_list[0])
    status.append(split_list[1])
    timestamp.append(split_list[2])


# Removing the first entries of each list since they are column headings, and the headings have been modified later
name.remove(name[0])
status.remove(status[0])
timestamp.remove(timestamp[0])
    



# Splitting timestamp into date and time
for i in range(0, len(timestamp)):
    datetime_list = timestamp[i].split(',')
    date.append(datetime_list[0])
    time.append(datetime_list[1])


# Taking only time value in time list, removing "AM\n"
for i in range(0, len(time)):
    time_value = time[i][0 + 1 : time[i].find("AM'\n'") - 3]
    new_time.append(time_value)
    

# Converting 'string' type time values to 'datetime' type time values
for i in range(0, len(new_time)):
    date_time_obj = datetime.strptime(new_time[i], '%H:%M:%S')
    final_time.append(date_time_obj)




# Creating a dictionary and dataframe for the data
attendance_dict = {'Full Name' : name, 'Status' : status, 'Time' : final_time}
attendance_df = pd.DataFrame(attendance_dict)




# Counting total occurrences of each person's name
name_count = Counter(name)

n = list(name_count.keys())
c = list(name_count.values())



unique_names = list(set(name))
unique_names.sort()

attendance_df_sorted = attendance_df.sort_values(by = ['Full Name', 'Time'])


for element in unique_names:
    
    a_df = attendance_df_sorted.loc[attendance_df_sorted['Full Name'] == element]

    
    if len(a_df) == 1:
    # if the person has only joined and not left
    
        duration_datetime = meet_end_time_datetime - a_df['Time']
        print('Name: ', element)
        print('Record, total time present in meeting: ', duration_datetime)
        
    else:
    # if the person has joined and left multiple times
        
        a_df_len = len(a_df)
        #print(a_df_len)
        
        
        if a_df_len % 2 == 0:
        # If length of dataframe is even
            use_length = a_df_len
            final_diff = '00:00:00'
            
        else:
        # If length of dataframe is odd
            final_diff = '00:00:00'
            use_length = a_df_len - 1
            time3 = a_df.iloc[use_length]['Time']
            final_diff = meet_end_time_datetime - time3
            
        for i in range(0, use_length, 2):
                
            duration = '00:00:00'
            
                
            time1 = a_df.iloc[i]['Time']
            time2 = a_df.iloc[i + 1]['Time']
                
            time_diff = time2 - time1
            duration = duration + time_diff + final_diff
            
        print('Name: ', element)
        print('Total time present in meeting: ', duration)            
                
                
    print('\n\n')
        



  
    
    










