# Harbinger

A messenger of love and propaganda

## Hardware
- [Adafruit Matrix Portal Starter Kit](https://www.adafruit.com/product/4812)
- 4 x [Mini magnet feet](https://www.adafruit.com/product/4631)

## Software

### Behavior
The device fetches data needed for all modules on power up and scrolls the active module's message across the rgb matrix. The messages refreshes after every 4 hours. A refresh can also be forced manually by pressing the *DOWN* button at the end of a message scroll (this will reset the 4 hour countdown as well). 

The device signals that messages are being fetched by displaying 'Connecting...' on the matrix.

The top level module, [code.py](code.py), is the controller responsible for updating modules, refreshing the display, scrolling the message and listening to button presses.

### Modules
1. [Cupid](cupid/cupid.py) - Displays a heartwarming message. 
    
    The message is fetched from on a Google Sheet accessed via the [Google Sheets API](https://developers.google.com/sheets/api). If the message is not changed after 20 refresh cycles it module displays a *'No love...'* cry.
    
    <img src="https://user-images.githubusercontent.com/18386420/136154583-1e70e1b5-f8b6-4610-926c-b464f7f66768.gif" width=40% height=40%>

### Privacy
The project stores sensitive information like WiFi passwords, tokens and API keys in a file called **secrets.py** that is not public (following [Adafruits' CircuitPython framework recommendation](https://learn.adafruit.com/adafruit-magtag/internet-connect)). In this fashion, the actual Google Sheet URLs are stored in secrets.py. The URL format is:
```
https://sheets.googleapis.com/v4/spreadsheets/*google_sheet_code*/values/*spreadsheet_tab_name*?alt=json&key=*API_key*
```
