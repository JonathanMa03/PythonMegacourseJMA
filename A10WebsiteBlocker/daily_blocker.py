import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.instagram.com","www.reddit.com"]
final_list=[redirect + " " + i for i in website_list]
final_string_block="\n".join(final_list)

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
        print("Working Hours...")
        with open(hosts_path,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
            print("Fun Hours...")
    time.sleep(5)


            
