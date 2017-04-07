from datetime import datetime,timedelta

print datetime.now() + timedelta(15)

print datetime.now() + timedelta(
	days=4,
	seconds=1231,
	milliseconds=123,
	minutes=21,
	hours=4,
	weeks=1
	)