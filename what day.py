from datetime import datetime, timedelta

now = datetime.now() 

print()
print('The current date is:',str(now.day),"/",str(now.month),"/",str(now.year) )
print()
print('(To exit, enter "q".)')
print()

while True:
    d_inp = input("How many days in the future? >")
    if d_inp == 'q':
        raise SystemExit
    else:
        d_inp = int(d_inp)
        # Using current time
        curr_time = datetime.now()
  
        # Calculating future date
        future_date = curr_time + timedelta(days = d_inp)
  
    # printing calculated future_dates
    print()
    print('Date will be:', str(future_date.day),"/",(future_date.month),"/", (future_date.year))
    print()