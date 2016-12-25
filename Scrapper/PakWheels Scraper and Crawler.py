
# coding: utf-8

# In[1]:

# Written By: 
# github/irtza ... irtzali@gmail.com
# Modified By Kuldeep Kumar 13bscskkumar@seecs.edu.pk
# Crawling and Scraping Pakwheels.com for Advertisement Images to generate a general Car-DataSet. deep-ALPR test Set..
# Fair-use only..
# For educational Purposes only


# In[2]:

# Basic Libraries 
import pandas as pd
import requests as req
import urllib2 as urllib2
import urllib as urllib
import numpy as np
from bs4 import BeautifulSoup
import os


# In[4]:

# Scraps given pages whose quantity can be managed by iterative variable I set for first 35 pages.
# Beautifies the HTML fetched from the server
# Look for specific Ad Tags
# Extract Image src from the images tags
# Append to a list of links of all the Images 


# Scraps given pages whose quantity can be managed by iterative variable I set for first 35 pages.
# Beautifies the HTML fetched from the server
# Look for specific Ad Tags
# Extract Image src from the images tags
# Append to a list of links of all the Images 


def RequesterAndSimplifier():
    links = []
    url = "http://www.pakwheels.com/used-cars/search/-/"
    for i in range(1500):
        try:
            print i
            r = req.get(url)
            print r
            soup = BeautifulSoup(r.content)
            ad_data = soup.find_all("li" , {"class": "classified-listing"})
            ads = []
            for item in ad_data:
                ads.append(item.find_all("li", {"class":"total-pictures-bar-outer"}))
            content = []
            for ad in ads:
                if  ad:
                    content.append(ad.pop())
            for item in content:
                links.append(item.get("data-src"))
            print len(links)
            print "links appended"
            url = "http://www.pakwheels.com/used-cars/search/-/?page=" + str(i+1)
        except:
            print "Exception"
            i = i - 1;
            continue
    print "Total Links: ", len(links)
    return links
    


# In[ ]:

# Calling the above function for fetching all the links of the Images
links  = RequesterAndSimplifier()


# In[6]:

fileopen = open("links.txt", "w")
for link in links:
    fileopen.writelines(link+"\n")
    
    


# In[55]:

links[0]


# In[7]:

# Download the images from the given list.
# Format the downloading Image as "ID-COMPANY-MODEL-YEAR-DATE"


def download_images_from_list_of_links(links):
    un = 0;
    fileopen = open("links.txt", "w")
    for link in links:
        try:
            fileopen.writelines(link+"\n")
            response = urllib.urlopen(link)
            print str(un) + "downloading from ", link
            rfname = link.split('/')[-1]
            #rfname = rfname.split('_')[-1];
            dir = "images/"+rfname.split('-')[0] +"_"+ rfname.split('-')[1];
            if not os.path.exists(dir):
                os.makedirs(dir)
            un = un + 1;
            local_file = open(dir+"/"+str(un)+"-" + rfname, "wb")
            local_file.write(response.read())
            local_file.close()   
        #except urllib., e:
        #    print "HTTP error ",e
        #except urllib.URLError , e:
        #    print "URL error ",e
        except:
            print "Index Error"
            
    print "DONE downloading!"


# In[ ]:




# In[ ]:

# Calling the above function for downloading all the links of the Images fetched above.
download_images_from_list_of_links(links)


# In[ ]:




# In[ ]:



