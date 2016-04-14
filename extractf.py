# -*- coding: utf-8 -*-
#!/usr/bin/python
#IRE_MAJOR_PROJECT--Semantic Job Candidate Recommendation Engine

import sys
import re
import os
from os import listdir
from os.path import isfile, join
import json
from dicts import languages, frameworks, modules, domains



index = {}

main_index = {}
for item in languages:
    main_index[item] = ""

for item in frameworks:
    main_index[item] = ""

for item in modules:
    main_index[item] = ""

for item in domains:
    main_index[item] = ""

#languages = {}

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

if ( __name__ == "__main__"):

    #Read from languages

    '''langfile = open(sys.argv[1], 'r')
    for line in langfile.readlines():
        temp = line.lower()

        languages[temp.split('\n')[0]] = [0, 0]
    #print languages'''
    onlyfiles = [f for f in listdir("./resum/") if isfile(join("./resum/", f))]
    #print onlyfiles
    cnt = 0
    for fname in onlyfiles:

        text=""

        fname = "./resum/"+fname
        try:
            os.system("java -jar pdfbox-app-1.8.11.jar ExtractText "+fname)
        except:
            continue
        fname = fname[:len(fname)-3]+"txt"
        try:
            file1=open(fname,'r')
        except:
            continue
        #f2 = open("teee", "w")
        ##target = open("output", 'w')    
        text=file1.read();
        print cnt
        text= re.sub('\n+','\n',re.sub('[\t\r\f\v]+', ' ',text.decode('utf-8').strip()))#removing spaces
        text = strip_non_ascii(text)
        text=text.replace(u'\xa0', u' ')
        text=text.lower()#removing non breaking space
        name=""
        mobile=""
        emailid=""
        deg = 1
        file1.close()
        os.system("rm -f "+fname)
        #   print text
        #f2.write(text)
        #f2.close()
        teli= text.split('\n')
        try:
            name=text.split('\n', 1)[0]#name using first line in resume
            name = name.title()

            #target.write(name)
            #target.write("\n")
        except:
            name = "-"
            #target.write("-")
            #target.write("\n")
            pass
        flag = 0
        for item in teli:
            try:
                mobile = re.search("(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}|(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}|(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", item.strip()).group(0)
                #mobile=re.search('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',item).group(0)
                #target.write(mobile)
                #target.write("\n")
                flag=1
                break
            except:
                continue
        
        if flag==0:
            mobile="-"
        try:
            emailid=re.findall(r"[^@\s,]+@[^@\s,]+\.[^@\s,]+", text)#list of emails using regular expression in regex(removing whitespace,@, and comma)
            emailid=','.join(emailid)
        except:
            emailid="-"
            pass
        flag=0;
        edu = "-"
        for single_line in text.splitlines():

            try:
                phd=re.search("p.h.d",single_line).group(0);
                edu = single_line
                deg = 4
                #target.write(single_line)
                #target.write("\n")
                flag=1;
                break
            except:
                pass;
            if(flag==0):
                try:
                    ms=re.search("m\.s|^ms$| ms|master of science",single_line).group(0);
                    #print single_line,2,ms
                    edu = single_line
                    deg = 3
                    #target.write(single_line)
                    #target.write("\n")
                    flag=1;
                    break
                except:
                    pass#need better regex
            if(flag==0):
                try:
                    mtech=re.search("m.{0,3}tech|master of technology",single_line).group(0);
                    edu = single_line
                    deg = 2
                    #target.write(single_line)
                    #target.write("\n")
                    flag=1;
                    break
                except:
                    pass
            if(flag==0):
                try:
                    btech=re.search("b.{0,3}tech|bachelor.*",single_line).group(0);
                    edu = single_line
                    #target.write(single_line)
                    #target.write("\n")
                    deg = 1
                    flag=1;
                    break
                except:
                    pass
        if(flag==0):
            pass
            #target.write("-")
            #target.write("\n")
        flag=0
        exp = "-"
        #text2 = re.sub("\n"," ", text)
        #patterns = [r'\b%s\b' % re.escape(item.strip()) for item in domains]
        #there = re.compile('|'.join(patterns))
        for single_line in text.splitlines():
            for item in domains:
                if item in single_line:
                    domains[item]+=1
        for single_line in text.splitlines():
            if ((single_line=="") or (single_line=="\n") or (ord(single_line[0])<97 or ord(single_line[0])>122) ) and flag==1:
                continue
            if flag==1 :
                exp = single_line
                #target.write(single_line)
                #target.write("\n")
                break
            if "work experience"==single_line or "experience"==single_line or "jobs"==single_line or "job experience"==single_line or single_line=="past experience":
                flag=1
        if(flag==0):
            pass
            #target.write("-")
            #target.write("\n")
        index[cnt] = index.get(cnt, {})
        index[cnt]["name"] = name
        index[cnt]["emailid"] = emailid
        index[cnt]["mobile"] = mobile
        index[cnt]["education"] = edu
        index[cnt]["experience"] = exp
        index[cnt]["deg"] = deg
        
        for single_line in text.splitlines():
            words = re.split(r' |\n|\\|/', single_line)
            for word in words:
                if word in modules:
                    lang = modules[word][0]
                    if lang=="c++" or lang=="cpp":
                        languages["c++"][0]+=1
                        languages["cpp"][0]+=1
                    elif lang=="js" or lang=="javascript":
                        languages["js"][0]+=1
                        languages["javascript"][0]+=1
                    else:
                        languages[lang][0]+=1
                    modules[word][1]+=1
                    index[cnt]["skills"]=index[cnt].get("skills", {})
                    index[cnt]["skills"][word] = index[cnt]["skills"].get(word, 0) + 1
                if word in frameworks:
                    lang = frameworks[word][0]
                    if lang=="c++" or lang=="cpp":
                        languages["c++"][0]+=1
                        languages["cpp"][0]+=1
                    elif lang=="js" or lang=="javascript":
                        languages["js"][0]+=1
                        languages["javascript"][0]+=1
                    else:
                        languages[lang][0]+=1
                    #print word, frameworks[word]
                    #languages[lang][0]+=1
                    frameworks[word][1]+=1
                    index[cnt]["skills"]=index[cnt].get("skills", {})
                    index[cnt]["skills"][word] = index[cnt]["skills"].get(word, 0) + 1
                if word in languages:
                    #languages[word][0]+=1
                    lang = word
                    if lang=="c++" or lang=="cpp":
                        languages["c++"][0]+=1
                        languages["cpp"][0]+=1
                    elif lang=="js" or lang=="javascript":
                        languages["js"][0]+=1
                        languages["javascript"][0]+=1
                    else:
                        languages[lang][0]+=1
                    '''if languages[word][1]==0:
                        languages[word][0]+=1
                        languages[word][1] = 1'''
                    index[cnt]["skills"]=index[cnt].get("skills", {})
                    index[cnt]["skills"][word] = index[cnt]["skills"].get(word, 0) + 1
        for item in languages:
            if languages[item][0]!=0:
                main_index[item]+="$"+str(cnt)+":"+str(languages[item][0])
                languages[item][0] = 0
        for item in modules:
            if modules[item][1]!=0:
                main_index[item]+="$"+str(cnt)+":"+str(modules[item][1])
                modules[item][1] = 0
        for item in frameworks:
            if frameworks[item][1]!=0:
                main_index[item]+="$"+str(cnt)+":"+str(frameworks[item][1])
                frameworks[item][1] = 0
        for item in domains:
            if domains[item]!=0:
                main_index[item]+="$"+str(cnt)+":"+str(domains[item])
                domains[item]=0
        cnt+=1

    



    for item in main_index:
        temp = main_index[item]
        if temp!="":
            tlist = temp.split("$")
            cnt = len(tlist)-1
            rlist = []
            for i2 in tlist:
                if i2=="":
                    continue
                i3 = i2.split(":")
                rlist.append([int(i3[1]), int(i3[0])])
            rlist.sort(reverse=True)
            main_index[item]="@"+str(cnt)
            for i2 in rlist:
                main_index[item]+="$" + str(i2[1])+":"+str(i2[0])





    fin = open("output.txt", "w")

    for item in sorted(main_index.keys()):
        fin.write(item)
        fin.write(main_index[item])
        fin.write("\n")

    json.dump(index, open("output2.txt",'w'))
    #json.dump(main_index, open("output.txt",'w'))
    #json.dump(languages, open("o2", "w"))
    #os.system("python -m json.tool output.txt > pretty.txt")
    os.system("python -m json.tool output2.txt > p2")
