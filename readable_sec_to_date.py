def format_duration(n):
    #assign variables
    s,m,h,d,y = 0,0,0,0,0
    date_range = ("Year", "Day", "Hour", "Minute", "Second")
    a = "and"
    
    #edge cases
    if n == 0:
        return "now"
    if n < 0:
        return None
    #calculation and dictionary writing
    dates = []
    if n > 0:
        m, s = divmod(n, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)
        
        if y == 0:
            None
        elif y == 1:
            dates.append(str(y))
            dates.append("Year")
        elif y > 1:
            dates.append(str(y))
            dates.append("Years")
        if d == 0:
            None
        elif d == 1:
            dates.append(str(d))
            dates.append("Day")
        elif d > 1:
            dates.append(str(d))
            dates.append("Days")
        if h == 0:
            None
        elif h == 1:
            dates.append(str(h))
            dates.append("Hour")
        elif h > 1:
            dates.append(str(h))
            dates.append("Hours")
        if m == 0:
            None
        elif m == 1: 
            dates.append(str(m))
            dates.append("Minute")
        elif m > 1:
            dates.append(str(m))
            dates.append("Minutes")
        if s == 0:
            None
        elif s == 1: 
            dates.append(str(s))
            dates.append("Second")
        elif s > 1:
            dates.append(str(s))
            dates.append("Seconds")
        
        if len(dates) > 2:
            dates_last = dates[-2:]
            dates_last = (" ".join(dates_last))
            del dates[-2:]  
            dates = (' '.join(l + ',' * (n % 2 == 1) for n, l in enumerate(dates)))
            dates = dates[:-1]
            dates = dates + " and"
            dates = dates + " " + dates_last
            print(dates)
            return dates
        else:
            print(" ".join(dates).strip())
            dates = (" ".join(dates).strip())
            return dates
        
format_duration(1030)