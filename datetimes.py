import datetime

# Best way to deal with datetimes in Python 3
# and to produce timestamps

# Use Timezones and make sure Datetimes are Timezone-Aware (TZ-Aware)
# We can do this using datetime.now with a timezone

# With a built in timezone
unow = datetime.datetime.now(datetime.timezone.utc) # This gives us a TZ-Aware Datetime in UTC
print(unow)
# datetime.datetime(2021, 4, 22, 3, 41, 16, 308781, tzinfo=datetime.timezone.utc)

# We can now get the POSIX timestamp for the current time from our UTC Datetime
uts = unow.timestamp()
print(uts)
# 1619062876.308781

# We can get the datetime back from the timestamp using fromtimestamp with a timezone as well
unow = datetime.datetime.fromtimestamp(uts, datetime.timezone.utc)  # This will give us the same TZ-Aware Datetime in UTC
print(unow)
# datetime.datetime(2021, 4, 22, 3, 41, 16, 308781, tzinfo=datetime.timezone.utc)

# Or with PyTZ
try: 
    import pytz
except ImportError:
    print("Missing pytz")
else:
    unow = datetime.datetime.now(pytz.UTC)
    # datetime.datetime(2021, 4, 22, 3, 42, 12, 839002, tzinfo=<UTC>)

    uts = unow.timestamp()
    # 1619062932.839002

    unow = datetime.datetime.fromtimestamp(uts, pytz.UTC)
    # datetime.datetime(2021, 4, 22, 3, 42, 12, 839002, tzinfo=<UTC>)

# You can get a similar result to .now() + timezone by using utcnow and tzinfo replace
datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

# Problems and Confusion that can arise if you don't follow this pattern
# Problems can arise when working with naive datetimes
now = datetime.datetime.now()   # You get a naive DateTime (non TZ-aware) based system timezone

# Even though now is a naive datetime, it's based on the current system time
# so this will adjust the time by the timezone offset to produce the timestamp
nts = now.timestamp()           # This is an accurate POSIX timestamp

unow = datetime.datetime.utcnow()   # A Local DateTime based on UTC

# It's important to remember that unow represents the current UTC time, 
# but it's still a naive datetime, so it will be treated just like now
uts = unow.timestamp()              # Now we run into trouble

# This timestamp does not represent our current time, 
# but is effectivel in the future since it is not timezone aware
