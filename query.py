from dicts import ml, nlp, webdev, networking, distributed, graphics
import math
import operator
from ppl import users

index = {}

dlist = {
	"ml":0,
	"nlp":0,
	"webdev":0,
	"networking":0,
	"distributed":0,
	"graphics":0
	}

def search():
	while 1:
		q = raw_input("Enter Query: ")
		if q=="exit":
			break
		else:
			#cnt = 0
			for item in dlist:
				dlist[item]=0
			qu=[]
			tlist = q.split()
			for item in tlist:
				if item in dlist:
					dlist[item]=1
				else:
					qu.append(item)
			score = {}
			for item in dlist:
				if dlist[item]==1:
					if item=="ml":
						tdict = ml
					elif item=="nlp":
						tdict = nlp
					elif item=="webdev":
						tdict = webdev
					elif item=="networking":
						tdict = networking
					elif item=="distributed":
						tdict = distributed
					else:
						tdict = graphics
					for item2 in tdict:
						if item2 in index:
							string = index[item2]
							strlist = string.split("$")
							df = int(strlist[0])
							flag = 0
							for iter1 in strlist:
								if flag==0:
									flag=1
									continue
								cnt = int(iter1.split(":")[0])
								tf = int(iter1.split(":")[1])
								tf = math.log10(1+tf)
								idf = math.log10(157.0/df)
								tf_idf = tf*idf*10.0
								score[cnt]=score.get(cnt, 0)
								score[cnt]+=tf_idf+users[str(cnt)]["deg"]
							second = tdict[item2]
							if second==0:
								continue
							if second in index:
								string = index[second]
								strlist = string.split("$")
								df = int(strlist[0])
								flag = 0
								for iter1 in strlist:
									if flag==0:
										flag=1
										continue
									cnt = int(iter1.split(":")[0])
									tf = int(iter1.split(":")[1])
									tf = math.log10(1+tf)
									idf = math.log10(157.0/df)
									tf_idf = tf*idf*5.0
									score[cnt]=score.get(cnt, 0)
									score[cnt]+=tf_idf+users[str(cnt)]["deg"]

			for item in qu:
				if item in index:
					string = index[item]
					strlist = string.split("$")
					df = int(strlist[0])
					flag = 0
					for iter1 in strlist:
						if flag==0:
							flag=1
							continue
						cnt = int(iter1.split(":")[0])
						tf = int(iter1.split(":")[1])
						tf = math.log10(1+tf)
						idf = math.log10(157.0/df)
						tf_idf = tf*idf*10.0
						score[cnt]=score.get(cnt, 0)
						score[cnt]+=tf_idf+users[str(cnt)]["deg"]
			sorted_score = sorted(score.items(), key=operator.itemgetter(1), reverse=True)
			i = 0
			for item in sorted_score:
				#print item
				if i<3:
					print "Name: ",users[str(item[0])]["name"]
					print "email: ",users[str(item[0])]["emailid"]
					print "Mobile: ",users[str(item[0])]["mobile"]
					print "Education: ",users[str(item[0])]["education"]
					print "Skills : "
					for it in users[str(item[0])]["skills"]:
						print "\t", it
					print "\n"
					i+=1
				else:
					break

			score.clear()








if __name__=="__main__":
	fname = open("output.txt", "r")
	text = fname.read()
	for line in text.splitlines():
		temp = line.split("@")
		if len(temp)!=1:
			index[temp[0]] = temp[1]
			#print temp[0], temp[1]
	search()