import http.server
import socketserver
import os
import subprocess


try:
    output = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], stderr=subprocess.DEVNULL)
    git_toplevel = output.decode().strip()
    os.chdir(git_toplevel)
except:
    pass
 
for subdir, dirs, files in os.walk('./'):
    for file in files:
      print(file)

PORT = 8000  # Change this to the port you want to use
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Serving file:", httpd.server_bind)
    httpd.serve_forever()
