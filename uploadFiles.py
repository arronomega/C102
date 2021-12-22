from os import access
import os
import dropbox
class transferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_2):
        #C:\Users\mikat\Dropbox\hallo
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        
        for root, dirs, files in os.walk(file_from):
            rel_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,rel_path)
        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))

def main():
    access_token='sl.A-m5zPC5xsNjQEpgSxFN24xiTxH8hYGD7tYkXGN8d7sYFk1hcEH8PfPQ1kRcUi8orcMut7wc6SViafJMSyig04q6Q46K2URUSpzfb_hzcwFacnzBKH1XVgNNXRiWYmGXJdHm_Ec'
    transferdata=transferData(access_token)
    file_from = input("Enter file path to transfer :")
    file_2 =  input("Enter destination path :")
    transferdata.upload_file(file_from,file_2)
    print("file has been moved")
main()