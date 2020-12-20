# Intraday stock prices 
A simple python function for getting free real-time stock prices
## :chart_with_upwards_trend:  What it does

Intraday stock prices is a Python function that you may easily use within your **financial applications**. It allows you to get free and real-time stock prices, of compagnies all aound the world. 

The function uses Google's financial data to provide the stock information.  It is simple to use, to customise and to maintain. 

 ##  :bulb: How it works
 
Intraday stock prices scans the stock data you're looking for from Google's research page. It then converts,reads and filters such data in order to give you the stock current price as an integer object.

![Composition 1](https://user-images.githubusercontent.com/65517595/102719243-3d6a6f80-42ed-11eb-982d-338b2b9218c7.jpg)

The function requieres additional libraries and tools to scan, convert and process the data :

- **Wkhtmltopdf** (https://wkhtmltopdf.org/) : a tool for taking screenshots of a specific website and saving them as image files
  
- **The Imgkit python library** (https://pypi.org/project/imgkit/) : a wkhtmltopdf python wrapper

- **Google's Tesseract-OCR** (https://github.com/tesseract-ocr/tesseract) :  a tool for converting an image's content to text data 

- **The Pytesseract library** (https://pypi.org/project/pytesseract/): a Google's Tesseract-OCR python wrapper

 
##   :electric_plug:Getting Started

You will first need to download and install the previously mentionned tools and libraries. Depending on your installation paths, you may need to update the function code :

<img src="https://user-images.githubusercontent.com/65517595/102720538-419a8b00-42f5-11eb-9e53-f9aa623449b0.jpg" width="700" height="260">

You may then call the function from your program, specifying which compagnie's stock price you would like to have.

Please consider the following subjects : 

- the function argument should be a **string**. You are however free to type the compagny's name or its stock ticker.

- The result display may take few seconds, since it is using the Google's Tesseract-OCR application to convert the screenshot to textual data. 


<img src="https://user-images.githubusercontent.com/65517595/102722201-d3a79100-42ff-11eb-8886-392fb80f8d72.jpg" width="700" height="183">


## 🤝 Contributing

Contributions, issues and feature requests are welcome.
Feel free to check issues page if you want to contribute.


## :+1: Licence

This project is GPL-3.0 licensed.


