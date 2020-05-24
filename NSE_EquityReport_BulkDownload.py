import requests
from  zipfile import ZipFile
import pandas as pd
import shutil
import time
import os
import datetime



dir_path = os.path.dirname(os.path.realpath(__file__))

if os.path.isdir(dir_path + "/" +"NSE_EQ_zip_Download")==False:
	os.mkdir(dir_path + "/" +"NSE_EQ_zip_Download")


if os.path.isdir(dir_path + "/" +"NSE_EQ_zip_Extract")==False:
	os.mkdir(dir_path + "/" +"NSE_EQ_zip_Extract")



date_range = pd.date_range(start='1/1/2019', end='5/25/2020', freq='D').to_pydatetime()


for i in date_range:
	Day=i.strftime("%d")
	month=i.strftime("%b")
	year=i.strftime("%Y")
	completeDate=str(Day+month.upper()+year)


	filename="cm" + completeDate + "bhav.csv.zip"
	filename_EQ_data=filename

	zip_EQ=dir_path+"/"+"NSE_EQ_zip_Download"
	unzip_EQ=dir_path+"/"+"NSE_EQ_zip_Extract"

	EQ_url_path=dir_path

	try:
		EQ_url = "https://www1.nseindia.com/content/historical/EQUITIES/" + str(year) +"/" + month.upper() +"/"+ filename
		extract = requests.get(EQ_url, allow_redirects=True)
		
		open(zip_EQ + "\\" + filename_EQ_data + ".zip", 'wb').write(extract.content)


		zip_target_EQ=zip_EQ + '\\' + filename_EQ_data+".zip"
		with ZipFile(zip_target_EQ , 'r') as data_ziped_EQ:
			data_ziped_EQ.extractall(unzip_EQ)

		print("Report Downloaded"+" " +str(Day) +"-"+month+"-"+str(year))	
	except:
		print("Report Not Available"+" " +str(Day) +"-"+month+"-"+str(year))
		os.remove(zip_target_EQ)
	######################################################################################
