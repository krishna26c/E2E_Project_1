import configparser
import Base.Initiate_browser

def readconfigData(section,key):
    cnf_Reader = configparser.ConfigParser()
    cnf_Reader.read("../Config/Configfile.cfg")
    cnf_Reader.get(section, key)
    return cnf_Reader.get(section, key)

def fetchelement(section, key):
    cnf_Reader = configparser.ConfigParser()
    cnf_Reader.read("../Config/Element.cfg")
    cnf_Reader.get(section, key)
    return cnf_Reader.get(section, key)

'''print(readconfigData("Details", "Aplication_url"))
print(readconfigData("Details", "Browser"))
print(fetchelement("Registration", "username"))
print(fetchelement("Registration", "password"))
print(fetchelement("WelcomePage", "welcomeText"))
print(fetchelement("WelcomePage", "errormsg"))'''