import requests as rq
ip=""
while ip!="q":
	ip=input("Enter IP Address (enter q to exit):")
	if ip!="q":
		req= rq.get(url="http://ip-api.com/json/{0}".format(ip))
		print(req.json())
