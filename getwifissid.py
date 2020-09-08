import subprocess
p=subprocess.Popen("netsh wlan show profiles".split(),stderr=subprocess.PIPE,stdout=subprocess.PIPE)
out,err=p.communicate()
out=out.decode('utf-8')
wifi_ssid={}
for item in out.split('\r\n'):
    if " All User Profile     :" in item:
        wifi_ssid[item.split(':')[1].strip()] = {'name':'','Authentication':'','Cipher':'','Security key':'','Key Content':''}
        
for ssid in wifi_ssid:
    if " " in ssid:
        cmnd='netsh wlan show profile name = "%s" key=clear'%(ssid)
    else:
        cmnd='netsh wlan show profile name = %s key=clear'%(ssid)
    p=subprocess.Popen(cmnd.split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err=p.communicate()
    out=out.decode('utf-8')
    wifi_ssid[ssid]['name']=ssid
    for item in out.split('\r\n'):
        if "Authentication" in item:
            wifi_ssid[ssid]['Authentication']=item.split(':')[1].strip()
        if "Cipher" in item:
            wifi_ssid[ssid]['Cipher']=item.split(':')[1].strip()
            
        if "Security key" in item:
            wifi_ssid[ssid]['Security key']=item.split(':')[1].strip()
            
        if "Key Content" in item:
            wifi_ssid[ssid]['Key Content']=item.split(':')[1].strip() 
            
print("Found %s Profiles"%(len(wifi_ssid)))
print("Exporting details to out.txt")
f=open("out.txt","w")    
for ssid in wifi_ssid:
    f.write(wifi_ssid[ssid]['name']+' : '+wifi_ssid[ssid]['Key Content']+'\n')
print("Exported %s Profiles"%(len(wifi_ssid)))
            