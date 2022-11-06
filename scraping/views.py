from django.shortcuts import render
from django.shortcuts import render


def home(request):

    result = None
    
    
    
    if 'year' in request.GET:
        
        import time
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.options import Options

        options= Options()
        options.headless=True

        # print(request.GET['from'])


        def Convert(string):
            li = list(string.split("\n"))
            return li

        PATH = "/usr/lib/chromium-browser/chromedriver"
        driver1 = webdriver.Chrome(PATH,options=options)
        driver2 = webdriver.Chrome(PATH,options=options)
        driver3 = webdriver.Chrome(PATH,options=options)    


        loc1=request.GET['from']
        loc2=(request.GET['to'])

        month= request.GET['month']
        year=request.GET['year']
        date=request.GET['date']

        
        # date1="2022-12-20" 
        # date2="20122022"
        # date3="20/12/2022"

        date1=year+"-"+month+"-"+date
        date2=date+month+year
        date3=date+"/"+month+"/"+year



        site1 = "https://paytm.com/flights/flightSearch/"+loc1+"/"+loc2+"/1/0/0/E/"+date1
        site2 = "https://www.flipkart.com/travel/flights/search?trips="+loc1[:3]+"-"+loc2[:3]+"-"+date2+"&travellers=1-0-0&class=e&tripType=ONE_WAY&isIntl=false&source=Search%20Form"
        site3 = "https://flight.easemytrip.com/FlightList/Index?srch="+loc1+"-India|"+loc2+"-India|"+date3+"&px=1-0-0&cbn=0&ar=undefined&isow=true&isdm=true&lang=en-us&&IsDoubleSeat=false&CCODE=IN&curr=INR"

        driver1.get(site1)
        driver2.get(site2)
        driver3.get(site3)

        time.sleep(10)

        prices1 = driver1.find_element("xpath", "/html/body/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div")
        prices2 = driver2.find_element("xpath" , "/html/body/div/div/div[2]/div/div[2]/div[2]/div[3]/div/div[1]/div[3]/div[1]/div")
        prices3 = driver3.find_element("xpath"  , "/html/body/form/div[9]/div[5]/div/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div")


        #print(Convert(prices1.text))
        #print(Convert(prices2.text))
        #print(Convert(prices3.text))


        result=dict()
        result['paytm'] = prices1.text
        result['flipkart'] = prices2.text
        # get the day, hour and actual weather
        result['easemy']=prices3.text
        driver1.quit()
        driver2.quit()
        driver3.quit()
    
    return render(request, 'scraping/webpage.html', {'result': result})
    