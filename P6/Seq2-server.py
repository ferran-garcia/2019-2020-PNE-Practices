import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

list_genes = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA", "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
bases = ["A", "C", "T", "G"]
FOLDER = "../Session-04/"
TEXT = ".txt"
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
            second_arg = args[1]
            seq_args = second_arg.split("=")   #Utilizar seq_args[-1] para operations como la operacion
            if req_line[1] == '/ping?':
                contents = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>RESULT</title>
                </head>
                <body>
                <h2>PING OK!</h2>
                <p>The SEQ2 server is running :)</p>
                """
                contents += '<a href="/">Main Page</a>'
                contents += "</body></html>"
                self.send_response(200)
            elif seq_args[0] == "sequence":
                contents = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>SEQUENCE</title>
                </head>
                <body>
                """
                for e in range(len(list_genes)):
                    if e == int(seq_args[1]):
                        contents += f"<h2> Sequence number {e}</h2>"
                        contents += f"<p>{list_genes[e]}</p>"
                        contents += '<a href="/">Main page</a>'
                        contents += "</body></html>"
                        self.send_response(200)
            elif seq_args[0] == "gene":
                seq0 = Seq("")
                contents = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>GENE</title>
                </head>
                <body>
                """
                contents += f"<h2> Gene: {seq_args[1]}</h2>"
                seq0 = str(seq0.read_fasta(FOLDER+seq_args[1]+TEXT))
                contents += f"<textarea readonly rows = 20 cols = 80>{seq0}</textarea>"
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