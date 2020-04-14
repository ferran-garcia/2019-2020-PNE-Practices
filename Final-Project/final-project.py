import http.server
import pathlib
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import json

list_genes = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA", "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
bases = ["A", "C", "T", "G"]
FOLDER = "../Session-04/"
TEXT = ".txt"
SERVER_EN = 'rest.ensembl.org'
ALWAYS_PARAMS = '?content-type=application/json'
conn = http.client.HTTPConnection(SERVER_EN)
# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True



# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        req_line = self.requestline.split(' ')

        args = (req_line[1]).split("?")
        first_arg = args[0]
        contents = Path('Error.html').read_text()
        self.send_response(404)
        if first_arg == "/":
            contents = Path('form-1.html').read_text()
            contents += Path('form-2.html').read_text()
            contents += Path('form-3.html').read_text()
            contents += Path('form-4.html').read_text()
            self.send_response(200)
        else:
            if first_arg in '/listSpecies':
                ENDPOINT = '/info/species'
                conn.request("GET", ENDPOINT + ALWAYS_PARAMS)
                resp1 = conn.getresponse()
                data_ = resp1.read().decode("utf-8")
                api_info = json.loads(data_)
                contents = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>RESULT</title>
                </head>
                <body>
                """
                contents += f"<h2> Species List</h2>"
                if '?' not in req_line[1]:
                    for e in api_info['species']:
                        contents += f"<p>{e['display_name']}</p>"
                else:
                    second_arg = args[1]
                    seq_args = second_arg.split("=")
                    sp_name = api_info['species']
                    counter = 0
                    for i in sp_name:
                        if counter < int(seq_args[-1]):
                            contents += f"<p>{i['display_name']}</p>"
                            counter += 1
                contents += '<a href="/">Main Page</a>'
                contents += "</body></html>"
                self.send_response(200)
            elif first_arg in '/karyotype':
                second_arg = args[1]
                seq_args = second_arg.split("=")
                ENDPOINT = '/info/assembly/'
                PARAMS = seq_args[-1] + ALWAYS_PARAMS
                conn.request("GET", ENDPOINT + PARAMS)
                resp1 = conn.getresponse()
                data_ = resp1.read().decode("utf-8")
                api_info = json.loads(data_)
                contents = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>SEQUENCE</title>
                </head>
                <body>
                """
                contents += f"<h2> Karyotype of the species: {seq_args[-1]}</h2>"
                for i in api_info['karyotype']:
                    contents += f"<p>{i}</p>"
                contents += '<a href="/">Main page</a>'
                contents += "</body></html>"
                self.send_response(200)
            elif first_arg in "/chromosomeLength":
                second_arg = args[1]
                seq_args = second_arg.split("=") #Queda la especie junto con el cromosoma
                args_def = seq_args[0].split("&")   #Separamos especie y cromosoma
                ENDPOINT = '/info/assembly/'
                PARAMS = args_def[0] + ALWAYS_PARAMS
                conn.request("GET", ENDPOINT + PARAMS)
                resp1 = conn.getresponse()
                data_ = resp1.read().decode("utf-8")
                api_info = json.loads(data_)
                contents = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>GENE</title>
                </head>
                <body>
                """
                contents += f"<h2> Chromosome: {seq_args[-1]} Species: {args_def[0]}</h2>"
                for e in api_info['top_level_region']:
                    if e['name'] == seq_args[-1]:
                        contents += f"<p>{e['length']}</p>"
                contents += '<a href="/">Main page</a>'
                contents += "</body></html>"
                self.send_response(200)
            elif first_arg == '/operation':
                msg_oper = (seq_args[1]).split("&")
                seq0 = Seq(msg_oper[0])
                contents = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>GENE</title>
                </head>
                <body>
                """
                contents += "<h2>Sequence</h2>"
                contents += f"<p>{msg_oper[0]}</p>"
                contents += "<h2>Operation</h2>"
                if seq_args[-1] == "INFO":
                    contents += "<p>Info<p>"
                    contents += "<h2>Result</h2>"
                    contents += f"<p>The length of the sequence is: {seq0.len()}</p>"
                    for e in bases:
                        contents += f"<p>{e} : {seq0.count_base(e)} ({round(seq0.count_base(e)*(100/seq0.len()), 2)}%)</p>"
                    contents += '<a href="/">Main page</a>'
                    contents += "</body></html>"
                    self.send_response(200)
                elif seq_args[-1] == "COMP":
                    contents += "<p>Comp<p>"
                    contents += "<h2>Result</h2>"
                    contents += f"<p>{seq0.complement()}</p>"
                    contents += '<a href="/">Main page</a>'
                    contents += "</body></html>"
                    self.send_response(200)
                elif seq_args[-1] == "REV":
                    contents += "<p>Rev<p>"
                    contents += "<h2>Result</h2>"
                    contents += f"<p>{seq0.reverse()}</p>"
                    contents += '<a href="/">Main page</a>'
                    contents += "</body></html>"
                    self.send_response(200)



        # Open the form1.html file
        # Read the index from th

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()