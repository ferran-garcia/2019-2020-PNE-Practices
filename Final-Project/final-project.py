import http.server
import pathlib
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import json

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
            contents = Path('listspecies.html').read_text()
            contents += Path('karyotype.html').read_text()
            contents += Path('chromosomeLength.html').read_text()
            contents += Path('geneseq.html').read_text()
            contents += Path('geneinfo.html').read_text()
            contents += Path('geneCalc.html').read_text()
            contents += Path('genelist.html').read_text()
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
                    <title>LIST OF SPECIES</title>
                </head>
                <body style="background-color: lightblue;">
                """
                contents += f"<h2> Species List</h2>"
                contents += f"<p>The total number of species in ensembl is: {len(api_info['species'])}</p>"
                if len(args) == 1 or ((args[1])[-1] == '='):
                    for e in api_info['species']:
                        contents += f"<p>-{e['display_name']}</p>"
                else:
                    second_arg = args[1]
                    seq_args = second_arg.split("=")
                    sp_name = api_info['species']
                    counter = 0
                    contents += f"<p>The limit the user has selected is: {seq_args[-1]}</p>"
                    for i in sp_name:
                        if counter < int(seq_args[-1]):
                            contents += f"<p>-{i['display_name']}</p>"
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
                    <title>KARYOTYPE</title>
                </head>
                <body style="background-color: lightblue;">
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
                args_def = seq_args[1].split("&")   #Separamos especie y cromosoma
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
                    <title>CHROMOSOME LENGTH</title>
                </head>
                <body style="background-color: lightblue;">
                """
                contents += f"<h2> Chromosome: {seq_args[-1]} Species: {args_def[0]}</h2>"
                for e in api_info['top_level_region']:
                    if e['name'] == seq_args[-1]:
                        contents += f"<p>The length of the chromosome is:   {e['length']}</p>"
                contents += '<a href="/">Main page</a>'
                contents += "</body></html>"
                self.send_response(200)
            elif first_arg == "/geneList":
                ENDPOINT = '/overlap/region/human/'
                second_arg = args[1]
                seq_args = second_arg.split("&")
                values_for_params = []
                contents = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>CHROMOSOME LENGTH</title>
                </head>
                <body style="background-color: lightblue;">
                """
                for e in seq_args:
                    e = e.split('=')
                    values_for_params.append(e[-1])
                PARAMS = values_for_params[0] + ':' + values_for_params[1] + '-' + values_for_params[2] + '?feature=gene;content-type=application/json'
                conn.request("GET", ENDPOINT + PARAMS)
                resp1 = conn.getresponse()
                data_1 = resp1.read().decode("utf-8")
                api_info_genelist = json.loads(data_1)
                contents += f"<h2>The genes in the chromosome {values_for_params[0]} that start at {values_for_params[1]} and end at {values_for_params[2]} are:</h2>"
                for i in api_info_genelist:
                    contents += f"<p>{i['external_name']}</p>"
                contents += '<a href="/">Main page</a>'
                contents += "</body></html>"
                self.send_response(200)
            else:
                ENDPOINT1 = '/xrefs/symbol/homo_sapiens/'
                second_arg = args[1]
                seq_args = second_arg.split("=")
                PARAMS1 = seq_args[-1] + ALWAYS_PARAMS
                conn.request("GET", ENDPOINT1 + PARAMS1)
                resp1 = conn.getresponse()
                data_1 = resp1.read().decode("utf-8")
                api_info_id = json.loads(data_1)
                gene_id = api_info_id[0]
                gene_id = gene_id['id']
                contents = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>GENE</title>
                </head>
                <body style="background-color: lightblue;">
                """
                if first_arg == "/geneSeq":
                    ENDPOINT2 = '/sequence/id/'
                    PARAMS2 = gene_id + ALWAYS_PARAMS
                    conn.request("GET", ENDPOINT2 + PARAMS2)
                    resp2 = conn.getresponse()
                    data_2 = resp2.read().decode("utf-8")
                    api_info_seq = json.loads(data_2)
                    contents += f"<h2>The sequence of the gene {seq_args[-1]}</h2>"
                    contents += f"<textarea>{api_info_seq['seq']}</textarea>"
                elif first_arg == '/geneInfo':
                    ENDPOINT2 = '/lookup/id/'
                    PARAMS2 = gene_id + ALWAYS_PARAMS
                    conn.request("GET", ENDPOINT2 + PARAMS2)
                    resp2 = conn.getresponse()
                    data_2 = resp2.read().decode("utf-8")
                    api_info_gene = json.loads(data_2)
                    contents += f"<h2>Information about the gene: {seq_args[-1]}</h2>"
                    contents += f"<p>The start: {api_info_gene['start']}</p>"
                    contents += f"<p>The end: {api_info_gene['end']}</p>"
                    contents += f"<p>This gene is located in the chromosome: {api_info_gene['seq_region_name']}</p>"
                elif first_arg == "/geneCalc":
                    ENDPOINT2 = '/sequence/id/'
                    PARAMS2 = gene_id + ALWAYS_PARAMS
                    conn.request("GET", ENDPOINT2 + PARAMS2)
                    resp2 = conn.getresponse()
                    data_2 = resp2.read().decode("utf-8")
                    api_info_seq = json.loads(data_2)
                    seq0 = Seq(api_info_seq['seq'])
                    contents += f"<h2>Some calculations of the gene: {seq_args[-1]}</h2>"
                    contents += f"<p>The length of the sequence is: {seq0.len()}</p>"
                    for e in bases:
                        contents += f"<p>{e} : {seq0.count_base(e)} ({round(seq0.count_base(e)*(100/seq0.len()), 2)}%)</p>"
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