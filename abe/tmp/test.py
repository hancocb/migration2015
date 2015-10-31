request.POST._mutable = True
request.POST['now'] = 100
request.POST['now2'] = u'10000' #unicode?
context = { "req" : request }
import pdb; pdb.set_trace() #for debug