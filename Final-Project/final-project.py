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
bases = ['A', 'C', 'T', 'G']


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

        args = (req_line[1]).split("?") #With this .split() we separate the instruction that the program has to perform from the input
        first_arg = args[0]
        contents = Path('Error.html').read_text()
        self.send_response(404)
        try:
            if first_arg == "/": #This If will bring us to the main page were we choose what we are going to perform and the output
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
                    ENDPOINT = '/info/species' #This is the ENSEMBL REST API endpoint that will get us the list of species
                    conn.request("GET", ENDPOINT + ALWAYS_PARAMS)
                    resp1 = conn.getresponse()
                    data_ = resp1.read().decode("utf-8")
                    api_info = json.loads(data_)
                    if len(args) > 1:
                        args_2 = args #We change this to avoid the index out of range error
                        second_arg = args_2[1]
                        seq_args = second_arg.split("=")
                    list_species = []
                    if seq_args[1] == '' or (len(seq_args[1]) == 5 and 'json' in seq_args[1]): #This If includes any type of request line that doesn't have a limit, puts every species in a list
                        for e in api_info['species']:
                            list_species.append(e['display_name'])
                    else: #This Else will be used when we put a limit in a request line
                        if len(seq_args) == 3:
                            seq_args = (seq_args[1]).split('&')
                            sp_name = api_info['species']
                            counter = 0
                            for i in sp_name:
                                if counter < int(seq_args[0]):
                                    list_species.append(i['display_name'])
                                    counter += 1
                        else:
                            sp_name = api_info['species']
                            counter = 0
                            for i in sp_name:
                                if counter < int(seq_args[1]):
                                    list_species.append(i['display_name'])
                                    counter += 1
                    if 'json=1' in req_line[1]: #This If is for the advanced part, when we want the output in json format
                        if len(args) == 1 or ('0123456789' not in seq_args[1]):
                            dict_json = {'ListSpecies': list_species}
                            contents = json.dumps(dict_json)
                            self.send_response(200)
                        else:
                            dict_json = {'ListSpecies': {'Limit': seq_args[0], 'Species': list_species}}
                            contents = json.dumps(dict_json)
                            self.send_response(200)
                    else: #This is used when we don't select the json option, we just want it in HTML format
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
                        if not len(args) == 1 or ((args[1])[-1] == '='):
                            contents += f"<p>The limit the user has selected is: {seq_args[-1]}</p>"
                        for i in list_species:
                            contents += f"<p>-{i}</p>"
                        contents += '<a href="/">Main Page</a>'
                        contents += "</body></html>"
                        self.send_response(200)
                elif first_arg in '/karyotype':
                    second_arg = args[1]
                    seq_args = second_arg.split("=")
                    if '&' in seq_args[1]: #This If is for the advanced part, will separate the species from the json=1 when the option is selected
                        sp_arg = (seq_args[1]).split('&')
                        sp_arg = sp_arg[0] #This will be the name of the species we are going to take the karyotype of
                    else:
                        sp_arg = seq_args[-1]
                    ENDPOINT = '/info/assembly/'
                    PARAMS = sp_arg + ALWAYS_PARAMS
                    conn.request("GET", ENDPOINT + PARAMS)
                    resp1 = conn.getresponse()
                    data_ = resp1.read().decode("utf-8")
                    api_info = json.loads(data_)
                    karyotype_list = []
                    for i in api_info['karyotype']: #This loop will store every chromosome in a list
                        karyotype_list.append(i)
                    if 'json=1' in req_line[1]:
                        dict_json = {'species':{sp_arg:{'chromosomes': karyotype_list}}}
                        contents = json.dumps(dict_json)
                    else:
                        contents = """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>KARYOTYPE</title>
                        </head>
                        <body style="background-color: lightblue;">
                        """
                        contents += f"<h2> Karyotype of the species: {seq_args[-1]}</h2>" #The variable between the {} will be the name of the species, same as sp_arg
                        for e in karyotype_list:
                            contents += f"<p>{e}</p>"
                        contents += '<a href="/">Main page</a>'
                        contents += "</body></html>"
                    self.send_response(200)
                elif first_arg in "/chromosomeLength":
                    second_arg = args[1]
                    seq_args = second_arg.split("=") #With this .split() we are getting the species and the chromosome together
                    args_def = seq_args[1].split("&")   #With this .split() we separate the species and chromosome
                    chromosome = seq_args[-1] #This variable will store the name of the chromosome
                    if 'json' in seq_args[2]: #This If will be used when we want the output in json format
                        args_json = seq_args[2].split('&')
                        chromosome = args_json[0]
                    ENDPOINT = '/info/assembly/'
                    PARAMS = args_def[0] + ALWAYS_PARAMS #args_def[0] is the name of the species that we want to know something about
                    conn.request("GET", ENDPOINT + PARAMS)
                    resp1 = conn.getresponse()
                    data_ = resp1.read().decode("utf-8")
                    api_info = json.loads(data_)
                    chromo_length = ''
                    for e in api_info['top_level_region']: #The top_level_region key, refers to the chromosome of which we want to know the length about
                        if e['name'] == chromosome:
                            chromo_length += str(e['length'])
                    if 'json=1' in req_line[1]: #This if will be used when we check the json option
                        dict_json = {'species':{args_def[0]:{'Chromosome':{chromosome:{'The length of the chromosome is:': chromo_length}}}}}
                        contents = json.dumps(dict_json)
                    else:
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
                        contents += f"<p>The length of the chromosome is:   {chromo_length}</p>"
                        contents += '<a href="/">Main page</a>'
                        contents += "</body></html>"
                    self.send_response(200)
                elif first_arg == "/geneList":
                    ENDPOINT = '/overlap/region/human/'
                    second_arg = args[1]
                    seq_args = second_arg.split("&") #With this .split(), we put on a list the arguments; start, end and chromosome
                    values_for_params = []
                    contents = """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>GENE LIST</title>
                    </head>
                    <body style="background-color: lightblue;">
                    """
                    for e in seq_args: #In this for we are putting on a list only the numbers, with the earlier .split() we got together the value it self and the name for ex. start=300
                        e = e.split('=')
                        values_for_params.append(e[-1])
                    PARAMS = values_for_params[0] + ':' + values_for_params[1] + '-' + values_for_params[2] + '?feature=gene;content-type=application/json'
                    conn.request("GET", ENDPOINT + PARAMS)
                    resp1 = conn.getresponse()
                    data_1 = resp1.read().decode("utf-8")
                    api_info_genelist = json.loads(data_1)
                    contents += f"<h2>The genes in the chromosome {values_for_params[0]} that start at {values_for_params[1]} and end at {values_for_params[2]} are:</h2>"
                    gene_in_chromo = []
                    for i in api_info_genelist: #In this loop we put on a list the different genes in the range and the chromosome selected in the main page
                        contents += f"<p>{i['external_name']}</p>"
                        gene_in_chromo.append(i['external_name'])
                    contents += '<a href="/">Main page</a>'
                    contents += "</body></html>"
                    if 'json=1' in req_line[1]:  #This if will be used when we check the json option
                        contents = ''
                        dict_json = {'chromosome': values_for_params[0], 'Start': values_for_params[1], 'End': values_for_params[2], 'Genes': gene_in_chromo}
                        contents = json.dumps(dict_json)
                    self.send_response(200)
                else: #In this else, as you can see, we are acceding to two dictionaries already without caring about the endpoint, that is because they will be used in al three endpoints
                    ENDPOINT1 = '/xrefs/symbol/homo_sapiens/'
                    second_arg = args[1]
                    seq_args = second_arg.split("=")
                    gene_name = seq_args[1] #With the .split() above and this slicing, gene_name is going to be the name of the gene that we write in the main page
                    if 'json' in seq_args[1]: #This If is from the advanced section, will separte the json=1 of the gene name when the option is selected
                        args_json = seq_args[1].split('&')
                        gene_name = args_json[0]
                    PARAMS1 = gene_name + ALWAYS_PARAMS
                    conn.request("GET", ENDPOINT1 + PARAMS1)
                    resp1 = conn.getresponse()
                    data_1 = resp1.read().decode("utf-8")
                    api_info_id = json.loads(data_1)
                    gene_id = api_info_id[0]
                    gene_id = gene_id['id']
                    ENDPOINT2 = '/sequence/id/'
                    PARAMS2 = gene_id + ALWAYS_PARAMS
                    conn.request("GET", ENDPOINT2 + PARAMS2)
                    resp2 = conn.getresponse()
                    data_2 = resp2.read().decode("utf-8")
                    api_info_seq = json.loads(data_2)
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
                        gene_seq = ''
                        gene_seq += api_info_seq['seq']  #gene_seq will be the sequence of bases of the selected gene
                        if 'json=1' in req_line[1]: #This if will be used when we check the json option
                            dict_json = {'Gene name:':{gene_name:{'Sequence':gene_seq}}}
                            contents = json.dumps(dict_json)
                        else:
                            contents += f"<h2>The sequence of the gene {gene_name}</h2>"
                            contents += f"<textarea readonly rows = 20 cols = 80>{gene_seq}</textarea>"
                            contents += '<a href="/">Main page</a>'
                            contents += "</body></html>"
                    elif first_arg == '/geneInfo':
                        ENDPOINT3 = '/lookup/id/' #This is an extra dictionary that we will ned for this specific endpoint
                        PARAMS3 = gene_id + ALWAYS_PARAMS
                        conn.request("GET", ENDPOINT3 + PARAMS3)
                        resp3 = conn.getresponse()
                        data_3 = resp3.read().decode("utf-8")
                        api_info_gene = json.loads(data_3)
                        seq0 = Seq(api_info_seq['seq']) #We import the class Seq from Seq1, it will be useful for the things we have to do in this endpoint
                        if 'json=1' in req_line[1]: #This if will be used when we check the json option
                            dict_json = {'gene': gene_name, 'Start': api_info_gene['start'], 'End': api_info_gene['end'], 'Length': seq0.len(), 'Chromosome': api_info_gene['seq_region_name'], 'ID': gene_id}
                            contents = json.dumps(dict_json)
                        else:
                            contents += f"<h2>Information about the gene: {gene_name}</h2>"
                            contents += f"<p>The start: {api_info_gene['start']}</p>"
                            contents += f"<p>The end: {api_info_gene['end']}</p>"
                            contents += f"<p>The length of the gene's sequence is: {seq0.len()}</p>"
                            contents += f"<p>This gene is located in the chromosome: {api_info_gene['seq_region_name']}</p>"
                            contents += f"<p>The ID of the gene is: {gene_id}</p>"
                            contents += '<a href="/">Main page</a>'
                            contents += "</body></html>"
                    elif first_arg == "/geneCalc":
                        seq0 = Seq(api_info_seq['seq']) #We import the class Seq from Seq1, it will be useful for the things we have to do in this endpoint
                        if 'json=1' in req_line[1]: #This if will be used when we check the json option
                            for e in bases:
                                contents += f"<p>{e} : {seq0.count_base(e)} ({round(seq0.count_base(e) * (100 / seq0.len()), 2)}%)</p>"
                            dict_json = {'Gene': gene_name, 'Length': seq0.len(), 'A':{seq0.count_base('A'): {'Percentage': (round(seq0.count_base('A') * (100 / seq0.len()), 2))}}, 'C':{seq0.count_base('C'): {'Percentage': (round(seq0.count_base('C') * (100 / seq0.len()), 2))}}, 'T':{seq0.count_base('T'): {'Percentage': (round(seq0.count_base('T') * (100 / seq0.len()), 2))}}, 'G':{seq0.count_base('G'): {'Percentage': (round(seq0.count_base('G') * (100 / seq0.len()), 2))}}}
                            contents = json.dumps(dict_json)
                        else: #This will be used when the json option is not selected
                            contents += f"<h2>Some calculations of the gene: {gene_name}</h2>"
                            contents += f"<p>The length of the sequence is: {seq0.len()}</p>"
                            for e in bases:
                                contents += f"<p>{e} : {seq0.count_base(e)} ({round(seq0.count_base(e)*(100/seq0.len()), 2)}%)</p>"
                            contents += '<a href="/">Main page</a>'
                            contents += "</body></html>"
                        self.send_response(200)

        #All the exceptions below, are to avoid certain type of errors, instead of that it will send you tu the error page
        except ValueError:
            contents = Path('Error.html').read_text()
            contents += f"<p>This is a ValueError type </p>"
            self.send_response(404)

        except KeyError:
            contents = Path('Error.html').read_text()
            contents += f"<p>This is a KeyError type </p>"
            self.send_response(404)

        except IndexError:
            contents = Path('Error.html').read_text()
            contents += f"<p>This is an IndexError type </p>"
            self.send_response(404)
        except TypeError:
            contents = Path('Error.html').read_text()
            contents += f"<p>This is a TypeError type </p>"
            self.send_response(404)

        # Open the form1.html file
        # Read the index from th
        print(contents)
        # Define the content-type header:
        if 'json=1' in req_line:
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', len(str.encode(contents)))

        else:
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