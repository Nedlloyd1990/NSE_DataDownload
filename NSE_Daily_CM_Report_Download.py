import requests
from  zipfile import ZipFile
import pandas as pd
import shutil
import time
import os


months={
	'1':'JAN','2':'FEB','3':'MAR','4':'APR','5':'MAY','6':'JUN',
	'7':'JUL','8':'AUG','9':'SEP','10':'OCT','11':'NOV','12':'DEC'

}
dir_path = os.path.dirname(os.path.realpath(__file__))

if os.path.isdir(dir_path + "/" +"NSE_EQ_zip_Download")==False:
	os.mkdir(dir_path + "/" +"NSE_EQ_zip_Download")


if os.path.isdir(dir_path + "/" +"NSE_EQ_zip_Extract")==False:
	os.mkdir(dir_path + "/" +"NSE_EQ_zip_Extract")




Day=22
year=2020
month=months['5']

filename="cm" + str(Day) + month.upper() + str(year) + "bhav.csv.zip"
filename_EQ_data=filename


zip_EQ=dir_path + "/"+ "NSE_EQ_zip_Download"
unzip_EQ=dir_path + "/" +"NSE_EQ_zip_Extract"

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
