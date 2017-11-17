import sys
import re
import profile

day = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','today','yesterday','tomorrow']
month = ['january','february','march','april','june','july','august','september','october','november','december','jan','feb','mar','apr','may','jun','jul','aug','sep','sept','oct','nov','dec']
time_word = ['day','month','year','pm','am','p.m','a.m','midnight','noon','yesterday']
dep_word = ['in','on','later','next','after','before','at']
patterns = ['\d+\w\d+\w\d+','\d+']

def searchFilter(pattern, word):
    match=re.search(pattern, word)
    if match:
        return True
    else:
        return False

def timeFilter(problem_sen):
    text = problem_sen.replace('@','').replace('"',"").replace("'","").replace("#","").replace("[","").replace("]","").replace(","," ").lower()
    lis_word = text.split(" ")
    return_str = ""
    count = 0
    length = len(lis_word)
    next_word = 0
    while count < length:
        #print(lis_word[count])
        for pat in (day + month + time_word + dep_word):
            new_pat = str(pat)+"\\."
            if searchFilter(new_pat, lis_word[count]) or pat == lis_word[count]:
                return_str = return_str +  " " + str(lis_word[count]).replace(".","")
        for time_pat in patterns:
            if searchFilter(time_pat, lis_word[count]):
                return_str = return_str+" "+str(lis_word[count])

        count += 1

        if (len(return_str) <= 1):
            if return_str in dep_word:
                return_str = ""

    return return_str

def main():
    problem_lis = ["9 1/2","today, I am stephane egly and I will cook five eggs at 9:30am for $ 5000 $ in san francisco","7, 500","6.12%","It was stephane's second visit to Italy with 3 friends in UA414 on January, 19 2017 @3.45.20 p.m and spent us$ 10,000.5 which is 6.12% of his income .","It was stephane's second visit to Italy with 3 friends in UA414 on January, 19 2017 @3.45.20 pm and spent us$ 10,000.5 which is 60.32% of his income .","January 8 2017,10.50 am.","January 19, 2017 @ 3:45 pm","today","Jim was playing basketball at 5 25 20 am PST on evening","Jim was playing basketball at 5.25.20pm PST on Wednesday","Jim was playing basketball at 5 25am PST on evening","Jim was playing basketball at 5.25pm PST on Wednesday","First , according to the Caijing report , Luneng 's privatization process lasted  11   years   (   1995   -   2006   )  .","When I was back in China  this   year  , I tutored little girls at two relatives homes , feeling  14   -   17  is a very dangerous age group for girls .","The time has been set for 5:00 p.m. sharp ,  February   11   (   Sunday   )   ,   2007  .","Poster 's Site : mitbbs.com BBS (  Wed   Jan   17  10:09:13  2007  )","was the trains from delhi late yesterday?","tomorrow at 9am pacific time","Today is 25 of September of 2003, exactly at 10:49:41 with timezone -03h","2 dates: october 27 1994 to be put into effect on june 1 1995","2 dates: i am looking for a date june 4th 1996 so july 3rd 2013","i am looking for a date june 4th 1996 to july 3rd 2013","11. 12. 2014, 08:45:39","2016-02-04T20:16:26+00:00","13/03/2014","06-17-2014","19 February 2013 year 09:10","10:06am Dec 11, 2014","20 Mar 2013 10h11","Fri, 12 Dec 2014 10:55:50","2:21 p.m., December 11, 2014","8:25 a.m. Dec. 12, 2014","December 10, 2014, 11:02:21 pm","Aug. 9, 2012 at 2:57 p.m.","April 9, 2013 at 6:11 a.m.","Wed Aug 05 12:00:00 EDT 2015","Nov 25 2014 10:17 pm EST","may God have mercy on him","we will travel in may 2009","we may travel next may","[Sept] 04, 2014.","Tuesday Jul 22, 2014","10:04am EDT","Friday","November 19, 2014 at noon","December 13, 2014 at midnight"]
    ans_dic = {}
    for sen in problem_lis:
        try:
            ans_dic[str(sen)]=timeFilter(str(sen))
        except all as e:
            print("Exception throws"+str(e))
    for key in ans_dic:
        print(str(key)+" --> "+str(ans_dic[key]))

if __name__ == "__main__":
    #main()
    profile.run('print(main()); print')
