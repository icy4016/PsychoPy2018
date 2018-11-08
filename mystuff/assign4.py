from sys import argv
import datetime
from datetime import date 
import calendar

script, certain_year, certain_month, certain_date = argv
print 'hi, you input the year %s, month %s, and date %s' %(certain_year, certain_month, certain_date)
ans = datetime.date(int(certain_year), int(certain_month), int(certain_date))
print 'and that day is %s!' % calendar.day_name[ans.weekday()]

#def query_day_of_any_ymd
#	print "Please input the year, month, and date:"
