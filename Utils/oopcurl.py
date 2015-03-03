'''
Created on 29.10.2009

@author: jungle
'''
import pycurl
import random
import sys
import StringIO
PROXY_TYPE = {None:None,0:pycurl.PROXYTYPE_HTTP, 1:pycurl.PROXYTYPE_SOCKS4, 2:pycurl.PROXYTYPE_SOCKS5}
class Post:
    def __init__(self,proxies=None,proxytype=None,trys=3):
        self.headers = [
        'Accept-Language: en-us;q=0.7,en;q=0.3',
        'Accept-Charset: windows-1251,utf-8;q=0.7,*;q=0.7',
        'Keep-Alive: 300',
        'Connection: keep-alive',
        'Expect:'
        ]
        self.trys = trys
        self.proxytype = PROXY_TYPE[proxytype]
        self.proxies = proxies
        if self.proxies != None: self.proxy = random.choice(self.proxies)
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.COOKIELIST, '')
        self.curl.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; en; rv:1.9.2) Gecko/20100115 MRA 5.6 (build 03278) Firefox/3.6 (.NET CLR 3.5.30729)")
        self.curl.setopt(pycurl.FOLLOWLOCATION, 1)
        self.curl.setopt(pycurl.FAILONERROR,1)
##        self.curl.setopt(pycurl.VERBOSE,1)
        self.curl.setopt(pycurl.ENCODING,'gzip,deflate')
        self.curl.setopt(pycurl.AUTOREFERER,1)
        self.curl.setopt(pycurl.SSL_VERIFYPEER,False)
        self.curl.setopt(pycurl.HTTPHEADER, self.headers)
        if self.proxies != None:
             self.curl.setopt(pycurl.PROXYTYPE,self.proxytype)
             self.curl.setopt(pycurl.PROXY,self.proxy)
        self.referer = ''
    def set_trys(self,trys):
        self.trys = trys
    def get(self,url):
        self.curl.setopt(pycurl.POST, 0)
        return self.__perform(url)
    def post(self,url,data):
        self.curl.setopt(pycurl.POSTFIELDS, data)
        return self.__perform(url)
    def post_multipart(self,url,data):
        self.curl.setopt(pycurl.HTTPPOST, data)
        return self.__perform(url)
    def get_login(self,n=8,onlyletter=True):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        beta = "1234567890"
        if not onlyletter: gamma = alpha + beta
        else: gamma = alpha
        res = random.choice(alpha)
        for x in range(n-1):
            res += random.choice(gamma)
        return res
    def get_pass(self,n=8):
        alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
        res = ""
        for x in range(n):
            res += random.choice(alpha)
        return res
    def get_acaunt(self):
	   f = file("requests.txt")
	   while True:
		  line = f.readline()
		  if len(line) == 0:
			 break
		  print line.strip() #Avoid strip: print line,
	   f.close()

    def info(self):
        "Return a dictionary with all info on the last response."
        m = {}
        m['effective-url'] = self.curl.getinfo(pycurl.EFFECTIVE_URL)
        m['http-code'] = self.curl.getinfo(pycurl.HTTP_CODE)
        m['total-time'] = self.curl.getinfo(pycurl.TOTAL_TIME)
        m['namelookup-time'] = self.curl.getinfo(pycurl.NAMELOOKUP_TIME)
        m['connect-time'] = self.curl.getinfo(pycurl.CONNECT_TIME)
        m['pretransfer-time'] = self.curl.getinfo(pycurl.PRETRANSFER_TIME)
        m['redirect-time'] = self.curl.getinfo(pycurl.REDIRECT_TIME)
        m['redirect-count'] = self.curl.getinfo(pycurl.REDIRECT_COUNT)
        m['size-upload'] = self.curl.getinfo(pycurl.SIZE_UPLOAD)
        m['size-download'] = self.curl.getinfo(pycurl.SIZE_DOWNLOAD)
        m['speed-upload'] = self.curl.getinfo(pycurl.SPEED_UPLOAD)
        m['header-size'] = self.curl.getinfo(pycurl.HEADER_SIZE)
        m['request-size'] = self.curl.getinfo(pycurl.REQUEST_SIZE)
        m['content-length-download'] = self.curl.getinfo(pycurl.CONTENT_LENGTH_DOWNLOAD)
        m['content-length-upload'] = self.curl.getinfo(pycurl.CONTENT_LENGTH_UPLOAD)
        m['content-type'] = self.curl.getinfo(pycurl.CONTENT_TYPE)
        m['response-code'] = self.curl.getinfo(pycurl.RESPONSE_CODE)
        m['speed-download'] = self.curl.getinfo(pycurl.SPEED_DOWNLOAD)
        m['ssl-verifyresult'] = self.curl.getinfo(pycurl.SSL_VERIFYRESULT)
        m['filetime'] = self.curl.getinfo(pycurl.INFO_FILETIME)
        m['starttransfer-time'] = self.curl.getinfo(pycurl.STARTTRANSFER_TIME)
        m['redirect-time'] = self.curl.getinfo(pycurl.REDIRECT_TIME)
        m['redirect-count'] = self.curl.getinfo(pycurl.REDIRECT_COUNT)
        m['http-connectcode'] = self.curl.getinfo(pycurl.HTTP_CONNECTCODE)
        m['httpauth-avail'] = self.curl.getinfo(pycurl.HTTPAUTH_AVAIL)
        m['proxyauth-avail'] = self.curl.getinfo(pycurl.PROXYAUTH_AVAIL)
        m['os-errno'] = self.curl.getinfo(pycurl.OS_ERRNO)
        m['num-connects'] = self.curl.getinfo(pycurl.NUM_CONNECTS)
        m['ssl-engines'] = self.curl.getinfo(pycurl.SSL_ENGINES)
        m['cookielist'] = self.curl.getinfo(pycurl.INFO_COOKIELIST)
        m['lastsocket'] = self.curl.getinfo(pycurl.LASTSOCKET)
        m['ftp-entry-path'] = self.curl.getinfo(pycurl.FTP_ENTRY_PATH)
        return m
    def __perform(self,url):
        num = 0
        while num < self.trys:
            try:
                resp = StringIO.StringIO()
                self.curl.setopt(pycurl.WRITEFUNCTION, resp.write)
                self.curl.setopt(pycurl.TIMEOUT, 150)
                self.curl.setopt(pycurl.URL, url)
                self.referer = url
                self.curl.perform()
                the_page = resp.getvalue()
                resp.close()
                return the_page
            except pycurl.error, msg:
                num +=1
                if self.proxies != None:
                    self.proxy = random.choice(self.proxies)
                    self.curl.setopt(pycurl.PROXYTYPE,self.proxytype)
                    self.curl.setopt(pycurl.PROXY,self.proxy)
                print "Error:",msg
    def set_referer(self,referer):
        self.curl.setopt(pycurl.REFERER,referer)