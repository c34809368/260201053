month=input("please enter the month:")
day=int(input("please enter the day the day: "))

if (month=='january') or (month=='february') or (month=='march'):
	season='winter'
elif (month=='april') or (month=='may') or (month=='june'):
	season='spring'
elif (month=='july') or (month=='august') or (month=='september'):
	season='summer'
else:
	season='autumn'

if (month=='march') and (day>=20):
	season='spring'
elif (month=='june') and (day>=21):
	season='summer'
elif (month=='september') and (day>=22):
	season='autumn'
elif (month=='december') and (day>=21):
	season='winter'

print("the date is:",day,month,"and the season is:",season)