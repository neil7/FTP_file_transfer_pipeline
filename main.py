import ftplib
import os

FTP_HOST =  "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

def pipeline_FTP(path):
    # connect to the FTP server
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    # force UTF-8 encoding
    ftp.encoding = "utf-8"
    os.chdir(path)
    files = ftp.nlst()
    for fileName in os.listdir(path):
        if fileName != ".DS_Store" or fileName not in files:
            with open(fileName, "rb") as file:
                # use FTP's STOR command to upload the file
                ftp.storbinary(f"STOR {fileName}", file)
    return ftp

if __name__ == '__main__':
    sourcePath = "/Users/neilsharma/PycharmProjects/Python ETL/Source"
    ftp = pipeline_FTP(sourcePath)
    files = ftp.nlst()
    # for file in ftp.retrlines('LIST'):
    #     files.append(file)
    print("FilesList - ")
    print(files)