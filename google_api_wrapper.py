import gspread
from oauth2client.service_account import ServiceAccountCredentials

table_name = 'Chats Saver For Vladimir'


def write(double_array):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open(table_name)
    spreadsheet.values_clear("Лист1!A1:C10000")

    worksheet = spreadsheet.get_worksheet(0)
    worksheet.insert_rows(double_array)
    print("Data written successfully.")
