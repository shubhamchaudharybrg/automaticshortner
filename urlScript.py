import urllib.request as url
import webbrowser as wb
#import numpy as np
import csv

shortner = input("Enter shortner url : ")    # Asks url of shortner site e.g. za.gl
browser = wb.open(shortner)                  # opens browser
f1 = open("url.csv",'r')                    
f2 = open("shortUrl.csv",'w')                 
#urls = np.genfromtxt("B:/Website/url.csv",delimiter=' ')
urls = csv.reader(f1,delimiter=' ')          # reads csv file having all required urls to be shortned
#print(list(urls))
surls = csv.writer(f2,delimiter=' ')         # writes output csv file with shortned urls
surls.writerow(['abcd','fghi'])
        
#print(urls)

