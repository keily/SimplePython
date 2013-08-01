#codeing:utf-8

#require python 3.2 or later

import os
import codecs

def guess_textfile_encode(filepath): 
    guess_file=open(filepath,'rb') 
    bytes=guess_file.read() 
    guess_file.close() 
     
    #³¢ÊÔ±àÂë 
    def guess_encode(codecs1): 
        if bytes[:3]==codecs.BOM_UTF8: 
            bytes[3:].decode('utf-8') 
            return 'bom-utf-8' 
        else: 
            bytes.decode(codecs1) 
        return codecs1 


    #Ê¹ÓÃµÄ±àÂë 
    use_code=None 
    for code in support_codecs: 
        try: 
            use_code=guess_encode(code) 
            break 
        except: 
            pass 
     
    if use_code is None : 
        print('not support codecs') 
    else: 
        print('codecs of this file is {code}'.format(code=use_code))

if __name__ == "__main__":
    guess_textfile_encode('C:\\Users\\Administrator\\Desktop\\devlog.txt')
