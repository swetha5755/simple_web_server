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

                         
