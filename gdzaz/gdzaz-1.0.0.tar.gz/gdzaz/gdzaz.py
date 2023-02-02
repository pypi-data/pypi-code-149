from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os, wget
from datetime import datetime

def login ():
    dir_cred = os.environ['GOOGLE_DRIVE_CREDENTIALS']
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(dir_cred)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(dir_cred)
    else:
        gauth.Authorize()
    return GoogleDrive(gauth)

def listarItens(id, maxResults=100,exibirResultado=False, apenasPasta=False, apenasArquivos=False) -> list:
    """
        Lista os itens do id passado.

        :param id: id do item no google
        :type id: str
        :value id: '133' ou '123,456,485'

        :returns: list[{'id':'str','nome':'str','tipo':'str'}].
    """
    drive = login()   
    query = f"'{id}' in parents and trashed=false"
    if apenasPasta:
        query = f"'{id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
    elif apenasArquivos:
        query = f"'{id}' in parents and mimeType != 'application/vnd.google-apps.folder' and trashed=false"

    lista = []

    for file_list in drive.ListFile({'q': query,'maxResults':maxResults}):
        #print('Received %s files from Files.list()' % len(file_list)) # <= 10
        for file in file_list:
            lista.append({'id':file['id'], 'nome':file['title'], 'tipo':file['mimeType']})
            if exibirResultado:
                print('title: %s, id: %s, tipo: %s' % (file['title'], file['id'],file['mimeType'])) 
    
    return lista    

def uploadArquivo(listaArquivos,pastaId, atualizar = False, link=False):
    drive = login()
    lista = []
    if atualizar:
        lista = listarItens(pastaId)
        
    data = datetime.now().strftime('%Y%m%d')
    #downloadTemp = os.environ['GOOGLE_DRIVE_PATH_TEMP']+data
    downloadTemp = 'C:/Users/user/Downloads/teste/google_temp/'+data
    if link:
        for i in range(0,len(listaArquivos)):
            nome = listaArquivos[i].split('/')[-1]  
            if not os.path.exists(downloadTemp):
                os.makedirs(downloadTemp)

            wget.download(listaArquivos[i],downloadTemp)
            listaArquivos[i] = f'{downloadTemp}/{nome}'

    item = drive.CreateFile({'parents': [{'kind':'drive#fileLink', 'id':pastaId}]})
    for arquivo in listaArquivos:
        nome = arquivo.split('/')[-1]   
        
        item['title'] = nome
        if atualizar:
            i = list(filter(lambda a: a['nome'] == nome, lista))
            if len(i) > 0:
                item['id'] = i[0]['id']           
        item.SetContentFile(arquivo)
        item.Upload()

    return listarItens(apenasArquivos=True,id=pastaId)


    
def criarArquivo(nome,conteudo,pastaId):
    drive = login()
    item = drive.CreateFile({'parents': [{'kind':'drive#fileLink', 'id':pastaId}]})
    item['id'] = '1-Nq-F0xOmySOouH8IQywkm7WUSYHAveW'
    item['title'] = nome
    item.SetContentString(conteudo)
    item.Upload()

def criarPasta(nome,pastaId):
    drive = login()
    item = drive.CreateFile({'parents': [{'kind':'drive#fileLink', 'id':pastaId}]})    
    item['title'] = nome
    item['mimeType'] = 'application/vnd.google-apps.folder'
        #item.SetContentFile(arquivo)
    item.Upload()

def downloadItem(id,nome):
    drive = login()
    file = drive.CreateFile({'id': id})
    file.GetContentFile(nome)
    return True

def downlodPasta(id,destino, exibirResultado = False):
    """
        Download de todos arquivos da pasta informada pelo ID

        :param id - Id da pasta no Google Driver
        :param destino - Caminho destino para onde os arquivos serão gravados
        :param exibirResultado - Se True o resultado dera exibido no log
    """
    if not os.path.exists(destino):
        os.makedirs(destino)

    lista = listarItens(id,exibirResultado=False)
    res = []
    for item in lista:
        if item['tipo'] != 'application/vnd.google-apps.folder':
            resDownload = downloadItem(item['id'],f"{destino}/{item['nome']}")
            r = {'nome':item['nome'],'status':resDownload}
            res.append(r)
            if exibirResultado:
                print(r)
 

def criarVariasPastas(idGravar, nome_pasta, lista):
    for item in lista:
        id = item['id']
        if item['nome'] == nome_pasta:
            lista = listarItens(id, apenasPasta=True)
            return id
    
    criarPasta(nome_pasta,idGravar)
    lista = listarItens(idGravar, apenasPasta=True)
    item1 = list(filter(lambda a: a['nome'] == nome_pasta, lista))
    if len(item1) > 0:
        return item1[0]['id']    
    return id

def uploadPastaPorNome(destino,origem, id = '', atualizar = True, link=False):
    """
    Upload de lista de arquivos, cria as pastas caso não exista

    :param destino (str) - 'vero/bases'
    :desc destino - Caminho onde os arquivos serão gravados no Drive

    :param origem (list) - ['C:/Users/Propostas_20230119093527.csv',...]
    :desc origem - Lista dos arquivos a serem gravados

    :param id (str) - '5465454sdsd5646sds' 
    :value - ''
    :desc id - Id da pasta raiz, caso não seja informado a pasta raiz será a root

    :param atualizar (bolean) - True
    :value default - True
    :desc atualizar - Caso seja True ele ira atualizar o arquivo pelo nome
    """

    funcRoot = lambda a: a if a != '' else 'root'
    destino = destino.split('/')
    id2 = funcRoot(id)

    for item in destino:
        lista = listarItens(id2, apenasPasta=True, apenasArquivos=True)
        id2 = criarVariasPastas(id2, item,lista)

    return uploadArquivo(origem,id2,atualizar,link)