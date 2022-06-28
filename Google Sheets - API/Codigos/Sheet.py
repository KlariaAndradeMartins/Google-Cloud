from datetime import date
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account
from requests import request

from ayx import Alteryx


#gera as credenciais necessariasn
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# SERVICE_ACCOUNT_FILE = 'Keys.json'

TOKEN = {
    "type": "service_account",
    "project_id": "lanchonete-352816",
    "private_key_id": "88c6bad19f6af0a1e9662c2dcf6f8292b724082c",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDANdRoNmXPtSce\nsw9htB10ikX+4mbURpT7AtwrT4pfFeBW3XljaklKSaxaxGgrheVvFJQCzcuu+9ak\nRf+sHLvE0j/m5BOS50hrHDp+BprvA1SOlQMJL9UA4tMgfxuHRGRPBkc0VUIUaoMM\nwkuvn6qqq39KuA0qEsQNrsekwW1exbzBqHpE1/aKMFmUwN6V3jg4AOdmKNH6wfrz\nXqdrP1h9NtnGKUxmLcta85OhSeZmyA1N3yMBP+TOIjT37nU/Md2FVTawXrN6IkYW\n7pEZQ+FdrVt7RA5tOFDZrorTxZ5FHHSMK3bB5PqqI3u7Z6miudkAVssItU+HIYwM\ny4H17hlBAgMBAAECggEANAM9D9hMk7jzNZkB3BAX+m3ihBcy+VWCQiyjdKrpCFMM\nqqTzEMZ1v78Q/1zvzXtFu1nntZyH9jma+0gf6Cy8WQYGGc51R4cDr0xrvae+7FfL\n3WuQbz981ekLdds/kUqeFE5gHVbG82xhOyYmwgckcVvILemBUnXSjNtTlg9rr728\n0OZos6pcDpPh3xnNxWfShM+Bju+ENoq0XwT3R0j5PLRl51aksCesIsSmrJcnlnbE\n1DC31nEGVKtMvNq9fdrrCyaRKMyBo759Qw6HRoO1YBQgP8ZK6cN0dC1XvTHMGw+e\n/7v2Vu4BpogaecTCwiRnsTUE3zdLEHFk2rt8duwR2wKBgQD3eUakrrYMrxThSNlx\njM4g/Wga7eEJeWisJJxXiUqEZFwEpVF4oFIARwJ/xjNV6WAkl7ajjymDDhiAOQCZ\nsV4dE1oSlkuvuTvM2Q0cbPyyswrBnL/ylBTM/tpkacBFInhx+4MMYpHFM56W8ibd\nOI4Z/Z57Pv0FtbsQiUDdcDhJbwKBgQDG1SD2Gbycl7tvA9OqgvsPUQdaJPWuZCmF\nhVRvRoPfiqUjs9tp+wv+xzjV4dxWc6DO4WXiA4JPOEffUBT+V2ENM/6zuBCC1GSh\nIe/xn3eT44nY5tSAqZOsR0wbduzl321oghQ1eBkTzpAF6M/oeIgPrgakj+l2/x30\nvtudHk+QTwKBgEhP6bKJUqzWJBXIQbGKYVkGcvsbc1xfW5ShhgWWGm4hHTpGTE4h\nGpT2KubHNYzvCqbmpfmZBZpD7ijZfzFpwIRieTlhLXCFgdHTwp8Bwb09z/DPKs9p\nMcLM3Wfl9sa80dEMmzhtPQcQlFCrJWwS8ILrtvlwaGLYvXaRhKCv/+KFAoGBAKEf\nzRohOQrcmnMX8srWYYTD8OVH1h9/43Xj2cxipDLeM3x/H2r+mXXZE2GfKeKUyNdd\nKCbDGTIBNZztVFXXkToVzGzu19JtMy6wRbTTuR8K4IX4aHPq91RAYphPAyI0sIBk\nCORbclbuqR9gzjpgkkHCkHeCd3qKuke+8lCcY3VZAoGBALsWXOcZUZOmqTgX2Hy0\nRllDv/mpvfQvx2JsEw9VeA4fvFiRKDzdEKX/SvL5RzFTLquTPJ+imsGIdPjeYAcX\nXfjSz/fiCtioqlvhM38Bn4wtJ7rr2X8UmbxYKEL9f3oGlKyJQWfHUGaWs4vw24aT\nxC6yFtsA6A21+LPBMmh6az6w\n-----END PRIVATE KEY-----\n",
    "client_email": "mailto:lanchoneteteste@lanchonete-352816.iam.gserviceaccount.com",
    "client_id": "115233952638247783368",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/lanchoneteteste%40lanchonete-352816.iam.gserviceaccount.com"
  }


credentials = None
credentials = service_account.Credentials.from_service_account_info(
        TOKEN,
        scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ldIrs5Ooc2bFnE9QGZeBDpLpnYtEK72R2Akcs22BXfk'

def get_input() -> list:
    input = []
    alteryxData = Alteryx.read('#1')
    for _, row in alteryxData.iterrows():
        input.append([
            row['Empresa'],
            row['Data'],
            row['Competência'],
            row['Horas']])
    return input


""" Teste Local """
# def get_input() -> list:
#     input = []
#     input.append([
#         'teste',
#         'KyrosTeste',
#         '23/06/2022',
#         '150'])
#     return input


def process(data: list): 
    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    #Reading the sheet
    sheet = service.spreadsheets()

    result = sheet.values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range="Página1!A1:C15"
        ).execute() #Linhas do google sheet

    values = result.get('values', [])
    sheet_range = len(values)

    #Competencia,empresa, hora e data
    Dados = data

    #Rigthing on the sheet
    request = sheet.values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range="Página1!A"+str(sheet_range+1),
        valueInputOption="USER_ENTERED",
        body={"values":Dados}
        ).execute()

    print(request)


if __name__=='__main__':
    input = get_input()
    process(input)
