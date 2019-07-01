#!/usr/bin/python3.6
# importing the requests library 
import requests 
import time
import numpy as np
import pandas as pd

#the result csv file
#target = open('/opt/serialNumber/SAT_RX8200_VAST_SN.csv', 'w')

#the site district state dataframe
siteStateDF = pd.read_csv("/opt/RX8200SNGET/Site_District_State.csv",header=None,index_col=0)

#read the rx8200 list
with open("/opt/RX8200SNGET/RX8200_VAST_CUTDOWN_LIST.csv") as f:
	for line in f:
		time.sleep(1)
		print("==================================================")
		print(line.strip())
		name = line.strip().split(";")[0].strip('"')
		IP = line.strip().split(";")[1].strip('"')
		print("Name:"+name)
		print("IP:"+IP)

		# construct api-endpoint 
		URL = "http://"+IP+"/tcf?cgi=show&$path=/Decode"

		#get the raw data
		try:
			r = requests.get(url = URL,timeout=10)
			htmlStr = r.text
		except requests.exceptions.RequestException as e:
			htmlStr = str(e)
		print("------------------------------------------")
		print(htmlStr)
		print("------------------------------------------")		

		#get the Audio 1 L, Audio 1 R, Audio 2, Audio 3, Audio 4 L Audio 4 R
		Au1L = 0
		Au1LSv = 'NA'
		
		Au1R = 0
		Au1RSv = 'NA'
		
		Au2 = 0
		Au2Sv = 'NA'
		
		Au3 = 0
		Au3Sv = 'NA'
		
		Au4L = 0
		Au4LSv = 'NA'
		
		Au4R = 0		
		Au4RSv = 'NA'

		#get Audio 1 L
		pos = htmlStr.find("\'Audio 1 L\'")
		if pos != -1:
			theLine = htmlStr[pos:pos+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)
			
			pos2 = theLine2.find("\'Service\'")
			if pos2 != -1:
				theLine3 = theLine2[pos2:pos2+80]
				print(theLine3)
				Au1L = theLine3.split(',')[1].strip("'").split("-")[0].strip()
				Au1LSv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
		print("<Audio 1 L>:"+Au1L+"|"+Au1LSv)
		print("------------------------------------------")		

		#get Audio 1 R
		pos = htmlStr.find("\'Audio 1 R\'")
		if pos != -1:
			theLine = htmlStr[pos:pos+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)
			
			pos2 = theLine2.find("\'Service\'")
			if pos2 != -1:
				theLine3 = theLine2[pos2:pos2+80]
				print(theLine3)
				Au1R = theLine3.split(',')[1].strip("'").split("-")[0].strip()
				Au1RSv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
		print("<Audio 1 R>:"+Au1R+"|"+Au1RSv)
		print("------------------------------------------")		

		#get Audio 2
		pos = htmlStr.find("\'Audio 2\'")
		if pos != -1:
			theLine = htmlStr[pos:pos+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)
			
			pos2 = theLine2.find("\'Service\'")
			if pos2 != -1:
				theLine3 = theLine2[pos2:pos2+80]
				print(theLine3)
				Au2 = theLine3.split(',')[1].strip("'").split("-")[0].strip()
				Au2Sv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
		print("<Audio 2>:"+Au2+"|"+Au2Sv)
		print("------------------------------------------")		

		#get Audio 3
		pos = htmlStr.find("\'Audio 3\'")
		if pos != -1:
			theLine = htmlStr[pos:pos+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)
			
			pos2 = theLine2.find("\'Service\'")
			if pos2 != -1:
				theLine3 = theLine2[pos2:pos2+80]
				print(theLine3)
				Au3 = theLine3.split(',')[1].strip("'").split("-")[0].strip()
				Au3Sv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
		print("<Audio 3>:"+Au3+"|"+Au3Sv)
		print("------------------------------------------")		

		#get Audio 4L
		pos = htmlStr.find("\'Audio 4 L\'")
		if pos != -1:
			theLine = htmlStr[pos:pos+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)
			
			pos2 = theLine2.find("\'Service\'")
			if pos2 != -1:
				theLine3 = theLine2[pos2:pos2+80]
				print(theLine3)
				Au4L = theLine3.split(',')[1].strip("'").split("-")[0].strip()
				Au4LSv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
		print("<Audio 4L>:"+Au4L+"|"+Au4LSv)
		print("------------------------------------------")	

		#get Audio 4R
		pos = htmlStr.find("\'Audio 4 R\'")
		if pos != -1:
			theLine = htmlStr[pos:pos+280]
			#print(theLine)
			print("------------------------------------------")
			theLine2 = theLine.split("\n")[1]
			print(theLine2)
			
			pos2 = theLine2.find("\'Service\'")
			if pos2 != -1:
				theLine3 = theLine2[pos2:pos2+80]
				print(theLine3)
				Au4R = theLine3.split(',')[1].strip("'").split("-")[0].strip()
				Au4RSv = theLine3.split(',')[1].strip("'").split("-")[1].strip()
		print("<Audio 4R>:"+Au4R+"|"+Au4RSv)
		print("------------------------------------------")	

		print("==================================================\n")
	
			



