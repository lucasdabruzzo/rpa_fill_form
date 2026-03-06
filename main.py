# %%
# RPA to input data into a web form using Selenium
# This script automates the process of filling out a web form with data from a CSV file.

#Process steps:
# 1. Read data from a CSV file
# 2. Check data for validity
# 3. Use Pyautogui to open a web browser and navigate to the form
# 4. Fill out the form fields with the data from the CSV
# 5. Submit the form

# %%
# 1. Read data from a CSV file
# 2. Check data for validity

import pandas as pd

table_path = "produtos.csv" # Path to the CSV file containing the data
table = pd.read_csv(table_path) # Read the CSV file into a DataFrame


# %%
# 3. Use Pyautogui to open a web browser and navigate to the form

import pyautogui as pg
import time

site_url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # URL of the web form to be filled out
pg.PAUSE = 0.5 # Set a pause time between actions to make the automation smoother

pg.press("win") # Press the Windows key to open the Start menu
pg.write("chrome") # Type "chrome" to search for the Chrome browser
pg.press("enter") # Press Enter to open Chrome
pg.write(site_url) # Type the URL of the web form
pg.press("enter") # Press Enter to navigate to the URL

time.sleep(2) # Wait for the page to load before proceeding with filling out the form

pg.press("tab") # Press Tab to focus on the first input field of the form
pg.write("admin@hashtag.com") # Type "admin@hashtag.com" into the first input field (username)
pg.press("tab") # Press Tab to move to the next input field (password)
pg.write("123456") # Type "123456" into the second input field (password)
pg.press("tab")
pg.press("enter") # Press Enter to submit the form

pg.getActiveWindow().maximize() # Maximize the browser window to ensure all elements are visible
time.sleep(2)
pg.click(x=1140, y=364)

# Form is reached and ready to be filled out with data from the CSV file

# %%
# 4. Fill out the form fields with the data from the CSV
time.sleep(2)
pg.PAUSE = 0.2

for products in table.index: # Loop through each product in the DataFrame using its index
    
    pg.press("tab") # Press Tab to focus on the first input field of the form
    pg.write(table.codigo[products])
    pg.press("tab")
    pg.write(table.marca[products])
    pg.press("tab")
    pg.write(table.tipo[products])
    pg.press("tab")
    pg.write(str(table.categoria[products]))
    pg.press("tab")
    pg.write(str(table.preco_unitario[products]))
    pg.press("tab")
    pg.write(str(table.custo[products]))
    pg.press("tab")
    pg.write(str(table.obs[products]))
    pg.press("tab")
    pg.press("enter") # Press Enter to submit the form with the current product data

    for i in range(8): # Loop to go back to first input field after submitting the form
        pg.hotkey("shift", "tab") # Press Tab to move to the next input field for the next product data
    
    time.sleep(0.2) # Wait for a short time before filling out the next product data to ensure the form is ready for the next input

# Code ends here. Script fills out the form with the list of products from CSV file.
