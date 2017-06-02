from datetime import timedelta, datetime


def Skolko_dney():

	now = datetime.today()

	Next_year = int(now.strftime("%Y"))+1
	NG = datetime(Next_year,01,01)
	p = NG - now
	v = int((NG - now).total_seconds())

	d = v//(60*60*24)
	h = (v - d*(24*60*60))//(60*60)
	m = (v - d*(24*60*60) - h*(60*60))//60
	s = v - d*(24*60*60) - h*(60*60) - m*(60)
	return "Do konca goda ostalos:\n" + str(d) + " dney\n" + str(h) + " chasov\n" + str(m) + " minut\n" + str(s) + " sekund\n" + "Proverka: " + str(p)
	
print(Skolko_dney())
