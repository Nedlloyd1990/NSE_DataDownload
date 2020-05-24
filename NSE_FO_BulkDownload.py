import requests
from  zipfile import ZipFile
import pandas as pd
import shutil
import time
import os
import datetime



dir_path = os.path.dirname(os.path.realpath(__file__))

if os.path.isdir(dir_path + "/" +"NSE_FO_zip_Download")==False:
	os.mkdir(dir_path + "/" +"NSE_FO_zip_Download")


if os.path.isdir(dir_path + "/" +"NSE_FO_zip_Extract")==False:
	os.mkdir(dir_path + "/" +"NSE_FO_zip_Extract")



date_range = pd.date_range(start='1/1/2019', end='5/25/2020', freq='D').to_pydatetime()


for i in date_range:
	Day=i.strftime("%d")
	month=i.strftime("%b")
	year=i.strftime("%Y")
	completeDate=str(Day+month.upper()+year)


	filename="fo" + completeDate + "bhav.csv.zip"
	filename_FO_data=filename

	zip_FO=dir_path+"/"+"NSE_FO_zip_Download"
	unzip_FO=dir_path+"/"+"NSE_FO_zip_Extract"

	FO_url_path=dir_path

	try:
		FO_url = "https://www1.nseindia.com/content/historical/DERIVATIVES/" + str(year) +"/" + month.upper() +"/"+ filename
		extract = requests.get(FO_url, allow_redirects=True)
		
		open(zip_FO + "\\" + filename_FO_data + ".zip", 'wb').write(extract.content)


		zip_target_FO=zip_FO + '\\' + filename_FO_data+".zip"
		with ZipFile(zip_target_FO , 'r') as data_ziped_FO:
			data_ziped_FO.extractall(unzip_FO)

		print("Report Downloaded"+" " +str(Day) +"-"+month+"-"+str(year))	
	except:
		print("Report Not Available"+" " +str(Day) +"-"+month+"-"+str(year))
		os.remove(zip_target_FO)
	######################################################################################
