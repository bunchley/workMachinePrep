
import webbrowser, os, sys

#open client central
program_path = r"C:\Path\To\Your\Program.exe" 
#open kc

# open SD
#open notes
# market information
## WSJ, Bloomberg
urls=[
    "http://www.wsj.com",
    "http://www.bloomberg.com",
    "http://www.cnbc.com"
]

print('News Displayed:')
for url in urls:
    print(url)
    webbrowser.open(url)


