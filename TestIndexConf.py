import ConfigParser
import Confing
import json

config = ConfigParser.ConfigParser()
config.read(Confing.Options["RootPath"] + "//" +  "Config.cfg")
test =  config.get("Sleep","TemeSleep")
print json.loads(test)
