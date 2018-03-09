import os
import time
import tweepy
consumer_key =LhN03ZHAEoBP7keWUU1wlTbr7
consumer_secret =B2bpNFcxdAn1yccXIBHceRa8eONohcXjLzDPkmlZseSWbuz96y
access_token =4212984612-cID27mOl5dUU3pFFqCe3TpagciKKNrWnIQUidPI
access_token_secret=fle15UVk1pyBJEL119GK3zpwyTGaaHDqnFYSoiUaXqgzK


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
b=1
a=0
while a<=2 :
    img="/home/user/desktop/img"+str(b)+".jpg"
    cmd="fswebcam -F 3 --fps 20 -r 800x600"+img
    os.system(cmd)
    print("pic taken")
    file=open(img,'rb')
    data=file.read()
    api.update_with_media(img,status="nice one")
    print("wait for 5 seconds for selfie")
    time.sleep(5)
    a+=1
    b+=1
    print("success")
