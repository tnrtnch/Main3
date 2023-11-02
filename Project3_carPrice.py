import tkinter as tk
import requests
import time
import pyautogui
import webview

from bs4 import BeautifulSoup
from tkinter import ttk
from selenium import webdriver
from keyboard import press
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from project3_addition import choice_model, choice_brand

def car_price():
    root = tk.Tk()
    root.title("Car price prediction")
    root.geometry("320x320")

    brand_var = tk.StringVar()
    model_var = tk.StringVar()
    year1_var = tk.StringVar()
    engine_var = tk.StringVar()
    transmission_var = tk.StringVar()
    category_var = tk.StringVar()
    cars = []
    result_var = tk.StringVar()
    result_var.set(" "*12 + "0.00 лв.")

    def calculating(event):
        result_var.set(' Car price is calculating!') 

    def submit():
        brand_input = brand_var.get() 
        cars.append(brand_input)
        model_input = model_var.get()
        cars.append(model_input)
        year1_input = year1_var.get()
        cars.append(year1_input)
        engine_input = engine_var.get()
        cars.append(engine_input)
        transmission_input = transmission_var.get()
        cars.append(transmission_input)
        category_input = category_var.get()
        cars.append(category_input)
        result_entry = result_var.get()


        print("The brand is : " + brand_input)
        print("The model is : " + model_input)
        print("The year1 is : " + year1_input)
        print("The year2 is : " + year1_input)
        print("The engine is : " + engine_input)
        print("The transmission is : " + transmission_input)
        print("The category is : " + category_input)
        print(cars)
        time.sleep(4)


        # Searching the Car in the Site
        driver = webdriver.Chrome()
        driver.minimize_window()
        url = "https://www.mobile.bg/pcgi/mobile.cgi"
        driver.get(url)

        time.sleep(4)
        try:
            driver.find_element(By.XPATH, '(//p[@class="fc-button-label"])[1]').click()
        except:
            pass        

        time.sleep(8)
        driver.find_element(By.XPATH, '//a[@class="linkSearch"]').click()
        time.sleep(4)

        # Select brand
        driver.find_element(By.XPATH, '(//select[@class="sw145new"])[1]').click()
        time.sleep(4)

        driver.find_element(By.XPATH, '(//select[@class="sw145new"]//option[@value="{}"])[1]'.format(cars[0])).click()
        time.sleep(4)

        # Select model
        driver.find_element(By.XPATH, '(//select[@class="sw145new"])[2]').click()
        time.sleep(4)

        driver.find_element(By.XPATH, '(//select[@class="sw145new"]//option[@value="{}"])[1]'.format(cars[1])).click()
        time.sleep(4)

        # Select year1
        driver.find_element(By.XPATH, '//select[@name="f10"]').click()
        time.sleep(4)

        driver.find_element(By.XPATH, '//select[@name="f10"]//option[@value="{}"]'.format(cars[2])).click()
        time.sleep(4)

        # Select year2
        driver.find_element(By.XPATH, '(//select[@class="sw145new"])[8]').click()
        time.sleep(4)

        driver.find_element(By.XPATH, '(//select[@class="sw145new"])[8]//option[@value="{}"][1]'.format(cars[2])).click()
        time.sleep(4)

        # Select category
        driver.find_element(By.XPATH, '(//select[@class="sw145new"])[9]').click()
        time.sleep(4)

        driver.find_element(By.XPATH, '(//select[@class="sw145new"]//option[@value="{}"])[1]'.format(cars[3])).click()
        time.sleep(4)

        # Select engine
        driver.find_element(By.XPATH, '(//select[@class="sw145new"])[11]').click()
        time.sleep(4)

        driver.find_element(By.XPATH, '(//select[@class="sw145new"]//option[@value="{}"])[1]'.format(cars[4])).click()
        time.sleep(4)

        # Select transmission
        driver.find_element(By.XPATH, '(//select[@class="sw145new"])[12]').click()
        time.sleep(4)

        driver.find_element(By.XPATH, '(//select[@class="sw145new"]//option[@value="{}"])[1]'.format(cars[5])).click()
        time.sleep(4)

        # Select button
        driver.find_element(By.XPATH, '//input[@value="Т Ъ Р С И"]').click()
        time.sleep(4)

        global second_url
        second_url = driver.current_url

        request_price = requests.get(second_url)
        soup_price = BeautifulSoup(request_price.content, 'lxml')
        link_car = soup_price.find_all("td", attrs={"style":"width:162px;height:40px;padding-left:4px"})
        price_list = []
        count = 0

        for car in link_car:
            car_href = car.a.get("href")
            r_car = requests.get("https:" + str(car_href))
            s_car = BeautifulSoup(r_car.content, 'lxml')
            properties = s_car.find_all("div", attrs={"style":"font-size:16px; margin: 14px 10px 0 0; float:right"})

            for properti in properties:
                price = properti.find("strong", attrs={"style":"color: #09f;"}).text.replace(" лв.","").replace(" EUR","").replace(" ",".")
                price = float(price)
                price_list.append(price)
                count += 1

        if count == 0:
            result_var.set(" "*5 + "No result!")
            print(" "*5 + "No result!")
        else:
            global net_price
            net_price = (sum(price_list) / count)

            print("%.3f" % net_price + " лв.")
            result_var.set(" "*12 + "%.3f" % net_price + " лв.")
 
 
    # creating a label for name using widget Label
    brand = tk.Label(root, text = 'BRAND', font=('calibre',10, 'bold'))
    model = tk.Label(root, text = 'MODEL', font=('calibre',10, 'bold'))
    year1 = tk.Label(root, text = 'YEAR', font=('calibre',10, 'bold'))
    engine = tk.Label(root, text = 'ENGINE', font=('calibre',10, 'bold'))
    transmission = tk.Label(root, text = 'TRANSMISSION', font=('calibre',10, 'bold'))
    category = tk.Label(root, text = 'CATEGORY', font=('calibre',10, 'bold'))
    result = tk.Label(root, text = 'Your car price' , font=('calibre',12, 'bold'))    

    choice_brand
    choice_model

    choice_engine = ['всички типове','Бензинов','Дизелов','Електрически','Хибриден','Plug-in хибрид']
    choice_transmission = ['Без значение','Ръчна','Автоматична','Полуавтоматична']
    choice_category = ['всички категории','Ван','Джип','Кабрио','Комби','Купе','Миниван','Пикап','Седан',
                        'Стреч лимузина','Хечбек']

    # creating a entry for input name using widget Entry
    brand_entry = ttk.Combobox(root,textvariable = brand_var,values=choice_brand)
    # model_entry = tk.Entry(root,textvariable = model_var, font=('calibre',10,'normal')) 
    model_entry = ttk.Combobox(root,textvariable = model_var,values=choice_model)
    year1_entry = tk.Entry(root,textvariable = year1_var, font=('calibre',10,'normal'))
    engine_entry = ttk.Combobox(root,textvariable = engine_var,values=choice_engine)
    transmission_entry = ttk.Combobox(root,textvariable = transmission_var,values=choice_transmission)
    category_entry = ttk.Combobox(root,textvariable = category_var,values=choice_category)
    result_entry = ttk.Entry(root, textvariable = result_var, font=('calibre',10,'normal'))


    # creating a button using the widget Button that will call the "Search" function
    sub_btn=tk.Button(root,text = 'SEARCH', font=('Helveticabold', 14), bg="orange",command= submit) 
    sub_btn.bind("<Button-1>", calculating)


    # placing the label and entry in the required position using grid method
    brand.grid(row=0,column=0,padx=5, pady=14)
    brand_entry.grid(row=1,column=0,padx=7)
    model.grid(row=0,column=1,padx=5, pady=7)
    model_entry.grid(row=1,column=1)
    year1.grid(row=2,column=0,padx=5, pady=7)
    year1_entry.grid(row=3,column=0)
    engine.grid(row=4,column=0,padx=5, pady=7)
    engine_entry.grid(row=5,column=0)
    transmission.grid(row=4,column=1,padx=5, pady=7)
    transmission_entry.grid(row=5,column=1)
    category.grid(row=2,column=1,padx=5, pady=7)
    category_entry.grid(row=3,column=1)

    sub_btn.grid(row=9,column=0)
    result.grid(row=8,column=1,padx=5, pady=8)
    result_entry.grid(row=9,column=1)
            

    root.mainloop()


car_price()