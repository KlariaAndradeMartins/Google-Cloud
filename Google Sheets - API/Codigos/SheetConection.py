from datetime import date
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account
from requests import request


from typing import Any, List, Optional, TypedDict

#gera as credenciais necessariasn
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'Keys.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ldIrs5Ooc2bFnE9QGZeBDpLpnYtEK72R2Akcs22BXfk'

# from ayx import Alteryx

# def get_input() -> list:
#     input = []
#     alteryxData = Alteryx.read('#1')
#     for _, row in alteryxData.iterrows():
#         input.append([
#             row['Empresa'],
#             row['Data'],
#             row['Competência'],
#             row['Horas']])
#     return input

def get_input() -> list:
    input = []
    input.append([
        'teste',
        'KyrosTeste',
        '23/06/2022',
        '150'])
    return input


def process(data: list): 
    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    #Reading the sheet
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range="Página1!A1:C15").execute() #Linhas do google sheet
    values = result.get('values', [])
    sheet_range = len(values)

    #Competencia,empresa, hora e data
    Dados = data

    #Rigthing on the sheet
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Página1!A"+str(sheet_range+1), valueInputOption="USER_ENTERED", body={"values":Dados}).execute()
    print(request)

if __name__=='__main__':
    input = get_input()
    process(input)