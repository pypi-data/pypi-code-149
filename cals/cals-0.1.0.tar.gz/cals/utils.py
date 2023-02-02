def time2sec(time):
    h,m,s,ms = time
    return (h*3600) + (m*60) + s + (ms/1000000)


def time2day(time):
    return time2sec(time)/86400


def day2time(day):
    h = day * 24
    hour = int(h)
    m = (h - hour) * 60
    minute = int(m)
    s = (m - minute) * 60
    second = int(s)
    ms = (s - second) * 1000000
    microsecond = round(ms)
    return (hour, minute, second, microsecond)


def et2jd(et):
    J2000 = 2451545.0
    return J2000 + (et / 86400)
