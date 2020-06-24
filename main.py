import json
import tkinter

import requests


def get_prices():
    global data
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start':'1', 'limit':'10', 'convert':'USD'}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': '###API_YOUR_KEY###'}
    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data

def show_labels():
    for i in range(10):
        tkinter.Label(main_win, text=data["data"][i]["id"], font=("Helvetica, 12")).grid(row=i+1, column=0)
        tkinter.Label(main_win, text=data["data"][i]["name"], font=("Helvetica, 12")).grid(row=i+1, column=1)
        tkinter.Label(main_win, text="%.2f" % data["data"][i]["quote"]["USD"]["price"], font=("Helvetica, 12")).grid(row=i+1, column=2)
        tkinter.Label(main_win, text=str(data["data"][i]["quote"]["USD"]["percent_change_24h"]) + "%", font=("Helvetica, 12")).grid(row=i+1, column=3)
    win_timestamp = tkinter.Label(main_win, text=data["status"]["timestamp"], font=("Helvetica", 8))
    win_timestamp.grid(row=12, column=2, columnspan=2)

def update_data():
    # Fetches the new data from API and refreshes labels
    get_prices()
    show_labels()

get_prices()

main_win = tkinter.Tk()
main_win.title("TW_Koshelek")
title_label = tkinter.Label(main_win, text="Crypto top 10", font=("Helvetica", 20))
title_label.grid(row=0, column=0, columnspan=4)
show_labels()
refresh_button = tkinter.Button(main_win, text="Refresh", command=update_data).grid(row=12, column=0, columnspan=2)
main_win.mainloop()
