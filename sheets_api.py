from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
from pprint import pprint as pp


sheet_identifier = '1dJqHVOZdQb9HePhqjjLM1CcEMIsPq0l2u59XuHJZb0g' #production data excel

credentials_file = "dchproduction-e272739c5edc.json"

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]


credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scope)

# service = build("sheets", "v4", credentials=credentials)
# request = service.spreadsheets().get(spreadsheetId=sheet_identifier, ranges=[], includeGridData=False)
# sheet_props = request.execute()

client = gspread.authorize(credentials)
sheet = client.open("Production report 2023-24").worksheet('daily data')
# data = sheet.get_all_records()
sheet.update_cell(1421,2,200)
# row = sheet.row_values(3)
# pp(row)
# col = sheet.col_values(3)
# pp(col)
# pp(data)