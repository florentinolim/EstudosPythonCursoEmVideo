import requests
def buscar_dados():
    request = get(
        "https://dxib03.energia.org.br:9443/ibmmq/rest/v1/admin/qmgr/QM.DEV.INTEGRACAO/queue/AGENTEBSV1.LISTAR.IN")
    print(request.content)


if __name__ == '__main__':
    buscar_dados()
