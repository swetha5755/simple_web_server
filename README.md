# EX01 Developing a Simple Webserver

# Date:30.11.2024
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body>
        <h1 align="center">Device Properties(SWETHA S 24005755)</h1>
        <ol type="1">
            <h3 align ="center">Device name - DESKTOP-MOHHBTU</h3>
            <h3 align ="center">Processor - 13th Gen Intel(R) Core(TM) i5-1335U 1.30 GHz</h3>
            <h3 align ="center">Installed RAM - 16.0 GB (15.7 GB usable)</h3>
            <h3 align ="center">Device ID - 15EEA3B2-7EF5-4DEC-903D-577382C3C005</h3>
            <h3 align ="center">Product ID - 00342-42709-10446-AAOEM</h3>
            <h3 align ="center">System type - 64-bit operating system, x64-based processor</h3>
            <h3 align ="center">Pen and touch - No pen or touch input is available for this display</h3>
        </ol>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()        


```
# OUTPUT:
 ![alt text](<Screenshot 2024-12-01 003455.png>)
![Screenshot 2024-12-02 113910](https://github.com/user-attachments/assets/eb6f116b-749d-4eb4-bada-055f11b06537)

# RESULT:
The program for implementing simple webserver is executed successfully.
