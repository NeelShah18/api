import wget

def main():
    print("Start downlaoding")
    i = 600
    suc = 0
    fail = 0
    total = 0
    while i < 700:
        url = "https://r5---sn-tt1e7n7e.c.lh3.googleusercontent.com/videoplayback?id=4325e034ba1e30d0&itag=22&source=webdrive&begin=0&requiressl=yes&mm=30&mn=sn-tt1e7n7e&ms=nxu&mv=u&pl=19&sc=yes&ei=v9r_WZyUCo2CugKEkY_QBg&app=fife&driveid=0B1SWFcTWOZ3wQ3Vpd1pERVJKRkk&mime=video/mp4&lmt=1498632722142055&mt=1509939547&ip=65.39.33.95&ipbits=8&expire=1509947103&cp=TUlLWVRTX1BQUUJCSTpGS3AyV2Y2eVhrLUVseW9JbzRxcWUyUDNnYmp2VlFIZzVFbXM2cEFnWE9YN1c0aXhMOEMwUnlLQVIyUUY5ZjM&sparams=ip,ipbits,expire,id,itag,source,requiressl,mm,mn,ms,mv,pl,sc,ei,app,driveid,mime,lmt,cp&signature=43A10BCA32D127E1F3FBC924CE57229270812249.795AA9D1108BF6235A3978B38739E6DAF9654661&key=ck2&title=One-Piece-Episode-"+str(i)+"-English-Sub-[WATCHOP.IO]-auto"
        print("File dpwnloading number "+str(i))
        total = total+1
        try:
            file = wget.download(url)
            print("File downlaoding completed number "+str(i))
            suc = suc+1
        except:
            print("Erro in dpwnloaing file number: "+str(i))
            fal = fail+1
        i=i+1
    return {"total":total, "suc":suc, "fail":fail}

if __name__ == '__main__':
    x = main()
    print(x)
