import webbrowser

def  open_link(link):
	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
	webbrowser.open_new(link)