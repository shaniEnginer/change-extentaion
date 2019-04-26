import os,sys
folder = input('Enter the path to desier Folder')
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
    #    print(infilename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
    #    print(oldbase)
       newname = infilename.replace('.pyy', '.py')
       print( newname)
       output = os.rename(infilename, newname)
