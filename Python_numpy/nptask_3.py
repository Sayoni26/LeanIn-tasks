#**Task 3**

#* Write a NumPy program to display all the dates for the month of March, 2017.
import numpy as np
print("all data for the month of march 2017:")
print(np.arange('2017-03','2017-04',dtype='M'))

#* Write a NumPy program to get the dates of yesterday, today and tomorrow.
yes=np.datetime64("today",'D')-np.timedelta64(1,'D')
print("yesterday's date:",yes)
tod=np.datetime64("today",'D')
print("today's date:",tod)
tom=np.datetime64("today",'D')+np.timedelta64(1,'D')
print("tomorrow's date:",tom)
date=np.array([yes,tod,tom])
print(date)

#* Write a NumPy program to find the number of weekdays in March 2017.
print("Number of weekdays in March 2017:")
print(np.busday_count('2017-03', '2017-04'))

