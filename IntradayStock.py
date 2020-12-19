# Intraday stock function for getting a stock's real-time price
# Developped by The Finant: https://github.com/TheFinant
# Contact : thefinant@gmail.com




def intraday_stock(Stock):
    
        # We'll start by installing wkhtmltopdf tool on our computer, saving screenshots of a spécific website :
        # wkhtmltopdf is available at https://wkhtmltopdf.org/
        # We'll next install and import the Imgkit library, a wkhtmltopdf python wrapper
        # Imgkit library is avaiable at https://pypi.org/project/imgkit/
        import imgkit
    
        # We'll next install and use Google's Tesseract-OCR tool, for converting an image's content to text data 
        # Tesseract-OCR is available at https://github.com/tesseract-ocr/tesseract
        # We'll next install and import the pytesseract library, a Google's Tesseract-OCR python wrapper
        # Pytesseract library is available at https://pypi.org/project/pytesseract/
        import pytesseract 
    
        # We'll finally install and use the Python imaging library
        from PIL import Image
    
        Stock_Googlesearch = 'https://www.google.com/search?q='+ Stock +'%20stock&hl=en'
    
        # Let's start by taking a screenshot of Google's stock research page 
        # You may need to update the wkhtmltopdf application path, depending on your installation parameters 
        config = imgkit.config(wkhtmltoimage= r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe')
        imgkit.from_url(Stock_Googlesearch,'Stock_Googlescreenshot.jpg',config=config)
    
        Stock_Googlescreenshot = Image.open('Stock_Googlescreenshot.jpg')
    
        # The Pytesseract python module will be calling Google's Tesseract-OCR API
        # You may need to update the Tesseract-OCR application path, depending on your installation parameters 
        pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    
        # The Pytesseract module will be converting Google's screenshot to text data (STR) 
        Stock_Googledata = pytesseract.image_to_string(Stock_Googlescreenshot)
    
        # Converting Google's text data from string object to list object
        Stock_Googledatalist = Stock_Googledata.splitlines()
    
        # acquiring the list length 
        Googledatalist_len = len(Stock_Googledatalist)
    
        
        # The following loop's will be filtring the data to keep the stock's price
        
        
        for i in range (0,Googledatalist_len):
        
            try:
    
                Stock_Googledatalist_split = Stock_Googledatalist[i].split()

            
                if "." in Stock_Googledatalist_split[0]:
                
                    if "," in Stock_Googledatalist_split[0]:  
                        Stock_Googledatalist_split[0] = Stock_Googledatalist_split[0].replace(',','')
                    
                    Stock_value = float(Stock_Googledatalist_split[0])
                    return Stock_value
                    break
            
            except (IndexError,ValueError):
            
                continue
            

   