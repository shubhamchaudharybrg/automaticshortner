import urllib.request as url
import webbrowser as wb
#import numpy as np
import csv

shortner = input("Enter shortner url : ")
browser = wb.open(shortner)
f1 = open("url.csv",'r')
f2 = open("shortUrl.csv",'w')
#urls = np.genfromtxt("B:/Website/url.csv",delimiter=' ')
urls = csv.reader(f1,delimiter=' ')
#print(list(urls))
surls = csv.writer(f2,delimiter=' ')
surls.writerow(['abcd','fghi'])
        
#print(urls)

