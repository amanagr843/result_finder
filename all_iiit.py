from selenium import webdriver
from datetime import datetime
import numpy as np
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
name=[]
roll=[]
cgpa=[]
sgpa=[]
class iiit():
    def __init__(self,rollno,dateofbirth):
         self.browser=webdriver.Chrome("chromedriver.exe")
         self.rollno=rollno
         self.dateofbirth=dateofbirth
    def open(self):
        self.browser.get("http://122.252.250.253:83/result.aspx")
        iroll=self.browser.find_elements_by_css_selector("form input")[5]
        idate=self.browser.find_elements_by_css_selector("form input")[6]
        iroll.send_keys(self.rollno)
        idate.send_keys(self.dateofbirth)
        for d in range(79,84):
            try:
                self.browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option['+str(d)+']').click()
                for i in np.arange(1,13):
                    try:
                        self.browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option['+str(i)+']').click()
                        if i==2:
                            for l in np.arange(1,29):
                                try:
                                    self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l)+"']")
                                    self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l)+"']").click()
                                    try:
                                        btn1=self.browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_requestID"]')
                                        btn1.send_keys(Keys.ENTER)

                                    except:
                                        try:
                                            idate3=self.browser.find_elements_by_css_selector("form input")[6]
                                            idate3.click()
                                        except:
                                            source=self.browser.page_source
                                            data=bs(source,"html.parser")
                                            name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                                            roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                                            cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                                            sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)

                                    self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l+1)+"']").click()
                                    btn1=self.browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_requestID"]')
                                    btn1.send_keys(Keys.ENTER)

                                except:
                                    try:
                                        idate3=self.browser.find_elements_by_css_selector("form input")[6]
                                        idate3.click()
                                    except:
                                        source=self.browser.page_source
                                        data=bs(source,"html.parser")
                                        name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                                        roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                                        cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                                        sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)
                        elif i<=7:
                            if i%2 == 1:
                                for l in np.arange(1,32):
                                    try:
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l)+"']")
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l)+"']").click()
                                        try:
                                            btn1=self.browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_requestID"]')
                                            btn1.send_keys(Keys.ENTER)

                                        except:
                                            try:
                                                idate3=self.browser.find_elements_by_css_selector("form input")[6]
                                                idate3.click()
                                            except:
                                                source=self.browser.page_source
                                                data=bs(source,"html.parser")
                                                name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                                                roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                                                cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                                                sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l+1)+"']").click()
                                        btn1=self.browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_requestID"]')
                                        btn1.send_keys(Keys.ENTER)

                                    except:
                                        try:
                                            idate3=self.browser.find_elements_by_css_selector("form input")[6]
                                            idate3.click()
                                        except:
                                            source=self.browser.page_source
                                            data=bs(source,"html.parser")
                                            name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                                            roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                                            cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                                            sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)
                            else:
                                for l in np.arange(1,31):
                                    try:
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l)+"']")
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l)+"']").click()
                                        try:
                                            btn1=self.browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_requestID"]')
                                            btn1.send_keys(Keys.ENTER)

                                        except:
                                            try:
                                                idate3=self.browser.find_elements_by_css_selector("form input")[6]
                                                idate3.click()
                                            except:
                                                source=self.browser.page_source
                                                data=bs(source,"html.parser")
                                                name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                                                roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                                                cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                                                sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l+1)+"']").click()
                                        btn1=self.browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_requestID"]')
                                        btn1.send_keys(Keys.ENTER)

                                    except:
                                        try:
                                            idate3=self.browser.find_elements_by_css_selector("form input")[6]
                                            idate3.click()
                                        except:
                                            source=self.browser.page_source
                                            data=bs(source,"html.parser")
                                            name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                                            roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                                            cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                                            sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)
                        else:
                            if i%2 == 1:
                                for l in np.arange(1,31):
                                    try:
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l)+"']")
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l)+"']").click()
                                        try:
                                            btn1=self.browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_requestID"]')
                                            btn1.send_keys(Keys.ENTER)

                                        except:
                                            try:
                                                idate3=self.browser.find_elements_by_css_selector("form input")[6]
                                                idate3.click()
                                            except:
                                                source=self.browser.page_source
                                                data=bs(source,"html.parser")
                                                name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                                                roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                                                cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                                                sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l+1)+"']").click()
                                        btn1=self.browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_requestID"]')
                                        btn1.send_keys(Keys.ENTER)

                                    except:
                                        try:
                                            idate3=self.browser.find_elements_by_css_selector("form input")[6]
                                            idate3.click()
                                        except:
                                            source=self.browser.page_source
                                            data=bs(source,"html.parser")
                                            name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                                            roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                                            cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                                            sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)
                            else:
                                for l in np.arange(1,32):
                                    try:
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l)+"']")
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l)+"']").click()
                                        try:
                                            btn1=self.browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_requestID"]')
                                            btn1.send_keys(Keys.ENTER)

                                        except:
                                            try:
                                                idate3=self.browser.find_elements_by_css_selector("form input")[6]
                                                idate3.click()
                                            except:
                                                source=self.browser.page_source
                                                data=bs(source,"html.parser")
                                                name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                                                roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                                                cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                                                sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)
                                        self.browser.find_element_by_xpath("//td[not(contains(@class,'ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled'))]/a[text()='"+str(l+1)+"']").click()
                                        btn1=self.browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_requestID"]')
                                        btn1.send_keys(Keys.ENTER)

                                    except:
                                        try:
                                            idate3=self.browser.find_elements_by_css_selector("form input")[6]
                                            idate3.click()
                                        except:
                                            source=self.browser.page_source
                                            data=bs(source,"html.parser")
                                            name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                                            roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                                            cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                                            sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)
                    except:
                        try:
                            idate3=self.browser.find_elements_by_css_selector("form input")[6]
                            idate3.click()
                        except:
                            source=self.browser.page_source
                            data=bs(source,"html.parser")
                            name.append(data.find("div",{"class","col-sm-10"}).findAll("span")[0].text)
                            roll.append(data.find("div",{"class","col-sm-10"}).findAll("span")[1].text)
                            cgpa.append(data.find("table").findAll("tr")[1].findAll("td")[3].text)
                            sgpa.append(data.find("table").findAll("tr")[1].findAll("td")[4].text)
            except:
                    pass
"""
for j in range(2,10):
    o=iiit("2017UGEC00"+str(j)+"R","hdejhf")
    o.open()
for y in range(10,63):
"""
o=iiit("2017UGCS014R","hdejhf")
o.open()
dat=pd.DataFrame({"Rollno":roll,"Name":name,"Cgpa":cgpa,"sgpa":sgpa})
dat=dat.drop_duplicates(subset="Rollno")
dat.to_csv("final_1.csv")
