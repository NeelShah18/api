import urllib.request
import sys
from bs4 import BeautifulSoup
import csv
import os
import json

def main():
    url_list = []
    final_data = {}
    folder_num = 1
    final_list = []
    try:
        #Change the path here! - Locationof CSV file downloaded from website
        with open('/home/neel/Downloads/data.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            next(readCSV)
            for row in readCSV:
                url_list.append(row[20])
     
        for url in url_list:
            print(url) 
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
            req = urllib.request.Request(url, headers=headers)
            res = urllib.request.urlopen(req)
            resData = res.read()
            soup = BeautifulSoup(resData, 'html.parser')
         
            data = soup.find_all('img')[0]
          
            server_image_link = str(data.get('src'))
         
            
            try:
                all_image_url = []
                i = 1 
                while(i < 50):
                    j = 0
                    while(j < 10):
                        try:
                            print(str(i)+str(j))
                            image_url = server_image_link[:-5]+str(i)+"_"+str(j)+".jpg"
                            data2 = urllib.request.urlopen(image_url).read()
                            all_image_url.append(image_url)
                            #Change the path here! - Create folder where all file is stored
                            directory  = "/home/neel/Downloads/"+str(folder_num)+"/"
                            if not os.path.exists(directory):
                                os.makedirs(directory)
                            with open( directory+str(i)+str(j)+".jpg", "wb" ) as code :
                                code.write(data2)
                            j = j+1
                        except:
                            j = j+1
                            continue    
                    i = i+1
                    

            except Exception as e:
                #print("there!")
                data3 = urllib.request.urlopen(str(data.get('src'))).read()
                #Change the path here! - Create folder where all file is stored
                directory  = "/home/neel/Downloads/"+str(folder_num)+"/"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                with open( directory+str(1)+".jpg", "wb" ) as code :
                    code.write(data3)

                final_data = {'Name': str(folder_num), 
                                   'Image_ulrs':all_image_url,
                                   'Folder_name': str(folder_num),
                                   'Address': str(data.get('title')),
                                    }
                final_list.append(final_data)
                folder_num = folder_num + 1

        print("Done!")
        #Output jsonfile
        #Structure: data: list of dictonaries
        #every dic contains Name, Image_urls, Folder_name, Address
        with open('final_data.json', 'w') as fp:
            json.dump({'By':"Malai","data":final_list}, fp)
            
        
    except Exception as e:
        print("--Unsecessfull Scraping--")

if __name__=='__main__':
    main()