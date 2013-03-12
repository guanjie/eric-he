'''
Created on Jun 7, 2012

@author: humancool
'''
import hashlib
def file_to_hash(path, m = hashlib.sha1()):
    
    with open(path, 'r') as f:
        
        s = f.read(8192)
        
        while s:
            m.update(s)
            s = f.read(8192)
    
    return m.hexdigest()


def main():
    print file_to_hash("tapsense_connect_ios_master_ba73b3a1.zip")


if __name__=="__main__":
    main()








