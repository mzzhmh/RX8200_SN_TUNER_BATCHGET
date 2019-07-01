#!/usr/bin/python3.6
# importing the requests library 
import requests 
import time
import numpy as np
import pandas as pd

#the result csv file
target = open('/opt/serialNumber/SAT_RX8200_VAST_SN.csv', 'w')
target.write("Site ID,IP Address,Serial Number,Audio 1 L,Audio 1 L Service,Audio 1 R,Audio 1 R Service,Audio 2,Audio 2 Service,Audio 3,Audio 3 Service,Audio 4 L,Audio 4 L Service,Audio 4 R,Audio 4 R Service,Site Name,District,State\n")
target.flush()

#the site district state dataframe
siteStateDF = pd.read_csv("/opt/RX8200SNGET/Site_District_State.csv",header=None,index_col=0)

#read the rx8200 list
with open("/opt/RX8200SNGET/RX8200_VAST_CUTDOWN_LIST.csv") as f:
	for line in f:
		time.sleep(1)
		print("==================Serial Number===================")
		print(line.strip())
		name = line.strip().split(";")[0].strip('"')
		IP = line.strip().split(";")[1].strip('"')
		print("Name:"+name)
		print("IP:"+IP)
		# construct api-endpoint 
		URL = "http://"+IP+"/tcf?cgi=show&$path=/Customization"
		#get the raw data
		try:
			r = requests.get(url = URL,timeout=10)
			htmlStr = r.text
		except Exception as e:
			htmlStr = str(e)
		print("------------------------------------------")
		print(htmlStr)
		print("------------------------------------------")		
		#get the sn
		SN = "None"
		pos = htmlStr.find("Serial Number")
		if pos != -1:
			theLine = htmlStr[pos:pos+100]
			print(theLine)
			print("------------------------------------------")
			SN = theLine.split(",")[2].strip("'")
		siteID = name.split(" ")[-1]
		print(siteID+","+name+","+IP+","+SN)
		#target.write("%s,%s,%s,%s\n" % (siteID,name,IP,SN))
		#target.flush()
		print("==================Serial Number End===============\n")


	
		time.sleep(1)
		#get the Audio Code
		print("==================Audio Code===================")
		# construct api-endpoint
		URL2 = "http://"+IP+"/tcf?cgi=show&$path=/Decode"
		#get the raw data
		try:
			r2 = requests.get(url = URL2,timeout=10)
			htmlStr2 = r2.text
		except Exception as e:
			htmlStr2 = str(e)
		print("------------------------------------------")
		print(htmlStr2)
		print("------------------------------------------")
		#get the Audio 1 L, Audio 1 R, Audio 2, Audio 3, Audio 4 L Audio 4 R
		Au1L = 'NA'
		Au1LSv = 'NA'
		Au1R = 'NA'
		Au1RSv = 'NA'
		Au2 = 'NA'
		Au2Sv = 'NA'
		Au3 = 'NA'
		Au3Sv = 'NA'
		Au4L = 'NA'
		Au4LSv = 'NA'
		Au4R = 'NA'
		Au4RSv = 'NA'
		#get Audio 1 L
		pos2 = htmlStr2.find("\'Audio 1 L\'")
		if pos2 != -1:
			theLine = htmlStr2[pos2:pos2+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)

			pos3 = theLine2.find("\'Service\'")
			if pos3 != -1:
				theLine3 = theLine2[pos3:pos3+80]
				print(theLine3)
				try:
					Au1L = theLine3.split(',')[1].strip("'").split("-")[0].strip()
					Au1LSv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
				except Exception as e:
					print(str(e))
					
		print("<Audio 1 L>:"+Au1L+"|"+Au1LSv)
		print("------------------------------------------")
		#get Audio 1 R
		pos2 = htmlStr2.find("\'Audio 1 R\'")
		if pos2 != -1:
			theLine = htmlStr2[pos2:pos2+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)

			pos3 = theLine2.find("\'Service\'")
			if pos3 != -1:
				theLine3 = theLine2[pos3:pos3+80]
				print(theLine3)
				try:
					Au1R = theLine3.split(',')[1].strip("'").split("-")[0].strip()
					Au1RSv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
				except Exception as e:
                                        print(str(e))
		print("<Audio 1 R>:"+Au1R+"|"+Au1RSv)
		print("------------------------------------------")
		#get Audio 2
		pos2 = htmlStr2.find("\'Audio 2\'")
		if pos2 != -1:
			theLine = htmlStr2[pos2:pos2+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)

			pos3 = theLine2.find("\'Service\'")
			if pos3 != -1:
				theLine3 = theLine2[pos3:pos3+80]
				print(theLine3)
				try:
					Au2 = theLine3.split(',')[1].strip("'").split("-")[0].strip()
					Au2Sv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
				except Exception as e:
                                        print(str(e))
		print("<Audio 2>:"+Au2+"|"+Au2Sv)
		print("------------------------------------------")
		#get Audio 3
		pos2 = htmlStr2.find("\'Audio 3\'")
		if pos2 != -1:
			theLine = htmlStr2[pos2:pos2+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)

			pos3 = theLine2.find("\'Service\'")
			if pos3 != -1:
				theLine3 = theLine2[pos3:pos3+80]
				print(theLine3)
				try:
					Au3 = theLine3.split(',')[1].strip("'").split("-")[0].strip()
					Au3Sv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
				except Exception as e:
                                        print(str(e))
		print("<Audio 3>:"+Au3+"|"+Au3Sv)
		print("------------------------------------------")
		#get Audio 4 L
		pos2 = htmlStr2.find("\'Audio 4 L\'")
		if pos2 != -1:
			theLine = htmlStr2[pos2:pos2+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)

			pos3 = theLine2.find("\'Service\'")
			if pos3 != -1:
				theLine3 = theLine2[pos3:pos3+80]
				print(theLine3)
				try:
					Au4L = theLine3.split(',')[1].strip("'").split("-")[0].strip()
					Au4LSv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
				except Exception as e:
                                        print(str(e))
		print("<Audio 4 L>:"+Au4L+"|"+Au4LSv)
		print("------------------------------------------")
		#get Audio 4 R
		pos2 = htmlStr2.find("\'Audio 4 R\'")
		if pos2 != -1:
			theLine = htmlStr2[pos2:pos2+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)

			pos3 = theLine2.find("\'Service\'")
			if pos3 != -1:
				theLine3 = theLine2[pos3:pos3+80]
				print(theLine3)
				try:
					Au4R = theLine3.split(',')[1].strip("'").split("-")[0].strip()
					Au4RSv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
				except Exception as e:
                                        print(str(e))
		print("<Audio 4 R>:"+Au4R+"|"+Au4RSv)
		print("------------------------------------------")
		print("==================Audio Code End===============\n")
		
		print("==================Summary Results===============")
		SiteName = "NA"
		District = "NA"
		State = "NA"
		#print(siteStateDF.head())
		try:
			SiteName = siteStateDF.loc[[int(siteID)],1].tolist()[0].strip()
			District = siteStateDF.loc[[int(siteID)],2].tolist()[0].strip()
			State = siteStateDF.loc[[int(siteID)],3].tolist()[0].strip()
		except Exception as e:
			print(str(e))
		print(siteID+","+IP+","+SN+","+Au1L+","+Au1LSv+","+Au1R+","+Au1RSv+","+Au2+
			","+Au2Sv+","+Au3+","+Au3Sv+","+Au4L+","+Au4LSv+","+Au4R+","+Au4RSv+","+SiteName+","+District+","+State)
		target.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (siteID,IP,SN,Au1L,Au1LSv,Au1R,Au1RSv,Au2,Au2Sv,Au3,Au3Sv,Au4L,Au4LSv,Au4R,Au4RSv,SiteName,District,State))
		target.flush()
		print("==================Summary Results End===========")
