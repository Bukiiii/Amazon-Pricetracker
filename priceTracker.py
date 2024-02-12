import requests as r
import bs4
from datetime import datetime
import time
import schedule
import smtplib

base_url= 'https://amazon.de'
url_list = ['https://www.amazon.de/dp/B0BDJHR5DD', 'https://www.amazon.de/Apple-iPhone-Pro-128-Titan-Blau/dp/B0CHX53QY9/ref=sr_1_1?crid=N4N6JYPMZXU7&keywords=iphone+15+pro&qid=1707747358&sprefix=iphone+%2Caps%2C118&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1']
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

base_response = r.get(base_url, headers=headers)
cookies = base_response.cookies
print('Code wird ausgeführt...')
def track_prices():
    print(datetime.now)
    i=0
    for prod in url_list:
        product_response = r.get(url_list[i], headers=headers, cookies=cookies)
        soup = bs4.BeautifulSoup(product_response.text, features='lxml')
        price_integral = str(soup.find(class_="a-price-whole"))
        price_decimal = str(soup.find(class_="a-price-fraction"))
        price_integral = price_integral.replace('<span class="a-price-whole">', '')
        price_integral = price_integral.replace('.', '')
        price_integral = price_integral.replace('<span class="a-price-decimal">,</span></span>', '')
        price_decimal = price_decimal.replace('<span class="a-price-fraction">', '')
        price_decimal = price_decimal.replace('</span>', '')

        price = price_integral+'.'+price_decimal
        i=i+1
        #if(matrix < 21.950):
        #send_mail('https://www.potti.de/details/audi-a4-40-tfsi-matrix-acc-naviplus-aud-af-17852738')
        print(price)
    
def send_mail(url_variable):                                                            #Still in process  sending mail doesnt work atm
    recipents = ['']                                                                    #Needs to be filled with email recipents who you want to send the mail to
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login()                                                              #This needs to be filled inside() with ur google login data
    subject = 'Tante Emi Onkel Boobo der Matrix ist gesunken ich werde schwach!!!'
    body = 'LOS SCHNAPPT IHN EUCH:' + url_variable
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        '',                                                                     #Needs to be filled with the email who sends it
        recipents,
        msg
    )
    server.quit()
     

track_prices()
schedule.every(30).minutes.do(track_prices)
while True:
    schedule.run_pending()
    time.sleep(1)
    
    