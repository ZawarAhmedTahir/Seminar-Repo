import urllib.request
import tarfile


file = open("files.txt","r")
list=file.read()

for i in range (0,len(list)):

    if(list[i:i+5]=="-----"):
	
        print(list[i+8:i+15])
        urllib.request.urlretrieve('http://acl-arc.comp.nus.edu.sg/archives/acl-arc-160301-pdf/'+list[i+8:i+15], list[i+8:i+15])
        tar = tarfile.open(list[i+8:i+15])
        tar.extractall()

tar.close()
