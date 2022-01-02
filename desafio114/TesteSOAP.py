import requests

url = "https://desenv-servicos.energia.org.br:9442/ws/local/cag/AgenteBSv1?wsdl"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
#headers = {'Content-type': 'content_type_value'}
body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://xmlns.energia.org.br/MH/v1" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:v11="http://xmlns.energia.org.br/BM/v1" xmlns:v12="http://xmlns.energia.org.br/BO/v1">
   <soapenv:Header>
      <oas:Security>
         <!--Optional:-->
         <oas:UsernameToken>
            <!--Optional:-->
             <oas:Username>sgpintegracao</oas:Username>
            <!--Optional:-->
            <oas:Password>sgp$$01</oas:Password>
         </oas:UsernameToken>
      </oas:Security>
   </soapenv:Header>
   <soapenv:Body>
      <v11:agenteRequest>
         <v11:agente>
            <v12:sigla>TAMANDUAMIRIM</v12:sigla>
         </v11:agente>
      </v11:agenteRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

#response = requests.get(url, data=body,headers=headers)
print(response.headers)
print(response.status_code)
#print(response.content)

# ,headers=headers
