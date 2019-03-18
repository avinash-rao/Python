# Project Requirement:
#
#     We have an excel sheet which is having columns of name and email addresses.
#
#     Fetch the name and email address and prepare an Offer Letter. Offer Letter Template is available in doc form. Replace name and email id in the template and create a new doc with the name. So the total number of offer letters is equal to the total number of offer letters.
#
#     Convert newly created offer letter to the pdf file.
#
#     Prepare a mail and send the pdf file. Email id in the excel sheet will be the to_email of the send mail.
#
#     Log logging mechanism.

import sys
import os
import comtypes.client
import logging
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from docx import Document
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import ntpath
import time

# Global variables
g_logger = logging.getLogger(__name__)

# This class is responsible to generate offer letter
# and will return the new file name
class CreateOfferLetter:

    # Constructor
    def __init__(self, offer_letter_template, name, email):
        self.__offer_letter_template = offer_letter_template
        self.__name = name
        self.__email = email
        self.__new_offer_letter = ""

    # Call function
    def __call__(self):

        g_logger.debug("Name: %s", self.__name)
        g_logger.debug("Email: %s", self.__email)
        g_logger.debug("Offer Letter Template Name: {}".format(self.__offer_letter_template))

        _file = open(self.__offer_letter_template, 'rb')
        _doc = Document(_file)

        # Start traversing over doc file
        for paragraph in _doc.paragraphs:

            # Search for the name. If it is present then replace it
            if '[Name]' in paragraph.text:
                inline = paragraph.runs
                # Loop added to work with runs (strings with same style)
                for i in range(len(inline)):
                    if '[Name]' in inline[i].text:
                        text = inline[i].text.replace('[Name]', self.__name)
                        inline[i].text = text

            if '[Email Id]' in paragraph.text:
                inline = paragraph.runs
                # Loop added to work with runs (strings with same style)
                for i in range(len(inline)):
                    if '[Email Id]' in inline[i].text:
                        text = inline[i].text.replace('[Email Id]', self.__email)
                        inline[i].text = text

        # name could have whitespaces. Replace it by underscore
        self.__name = self.__name.replace(" ", "_")
        self.__new_offer_letter = self.__name.replace(" ", "_") + "_Offer_Letter.docx"
        g_logger.debug("New offer letter name: %s", self.__new_offer_letter)

        # If this file already Present, then remove it
        if os.path.exists(self.__new_offer_letter):
            g_logger.info("New offer letter file {} already exist. Deleting older one.".format(self.__new_offer_letter))
            os.remove(self.__new_offer_letter)

        _doc.save(self.__new_offer_letter)
        _file.close()
        return self.__new_offer_letter

    # Destructor
    def __del__(self):
        del self.__offer_letter_template
        del self.__name
        del self.__email

# class to read Excel sheet and insert the data in the document created by OfferLetter class object
class ExcelSheetReader:

    # Constructor
    def __init__(self, _excel_file_name):
        self.__file_name = _excel_file_name

    # Call Function
    def __call__(self):
        g_logger.debug("Excel File Name: {}".format(self.__file_name))

        df = pd.read_excel(self.__file_name, sheet_name="Worksheet")
        names = df["Name"]
        emails = df["Email Address"]

        if len(names) != len(emails):
            g_logger.error("Excel file %s is invalid/corrupted", self.__file_name)

        _details = {}
        for i in range(len(names)):
            _details[names[i]] = emails[i]

        g_logger.error("_details:\n{}".format(_details))

        return _details

class Word2PdfConverter:
    def __init__(self, input_file):
        self.__input_file = os.path.abspath(ntpath.basename(input_file))
        self.__output_file = os.path.splitext(ntpath.basename(input_file))[0] + ".pdf"
        self.__output_file = os.path.abspath(self.__output_file)
        self.__word_format_pdf = 17

    def __call__(self):

        g_logger.debug("input file name: {}".format(self.__input_file))
        g_logger.debug("output file name: {}".format(self.__output_file))

        # Error the log and return false if input file not present
        if not os.path.exists(self.__input_file):
            g_logger.error("input doc file {} not exist".format(self.__output_file))
            return False

        # Error the log and return false if output file already present
        if os.path.exists(self.__output_file):
            g_logger.info("output pdf file {} already exist. Deleting older one.".format(self.__output_file))
            os.remove(self.__output_file)

        # create COM object
        word = comtypes.client.CreateObject('Word.Application')
        # key point 1: make word visible before open a new document
        word.Visible = True
        # key point 2: wait for the COM Server to prepare well.
        time.sleep(3)

        # convert docx file 1 to pdf file 1
        doc = word.Documents.Open(self.__input_file)
        doc.SaveAs(self.__output_file, FileFormat=self.__word_format_pdf)
        doc.Close()
        word.Quit()

        # Delete newly created doc file
        if os.path.exists(self.__input_file):
            os.remove(self.__input_file)

        return self.__output_file

class SendMail:
    def __init__(self, to_name, to_email, attach_file_name):
        self.__to_name = to_name
        self.__to_email = to_email
        self.__attach_file_name = attach_file_name

        # change these according to your requirements
        self.__from_email = ""
        self.__from_email_password = ""
        self.__subject = "Congrats {} - Offer Letter!!".format(self.__to_name)
        self.__body = "Hi {},\n\n"\
                "Please find your formal offer letter.\n\n"\
                "Request you to please accept the offer & share your acceptance.\n\n"\
                "Regards,\n"\
                "Pankaj Choudhary\n"\
                "Founder of cppsecrets.com".format(self.__to_name)

    def __call__(self):
        g_logger.debug("self.__to_name: {}".format(self.__to_name))
        g_logger.debug("self.__to_email: {}".format(self.__to_email))
        g_logger.debug("self.__attach_file_name: {}".format(self.__attach_file_name))
        g_logger.debug("self.__from_email: {}".format(self.__from_email))
        g_logger.debug("self.__subject: {}".format(self.__subject))
        g_logger.debug("self.__body: {}".format(self.__body))
        msg = MIMEMultipart()
        msg['From'] = self.__from_email
        msg['To'] = self.__to_email
        msg['Subject'] = self.__subject

        msg.attach(MIMEText(self.__body, 'plain'))

        attachment = open(self.__attach_file_name, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + self.__attach_file_name)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.__from_email, self.__from_email_password)
        server.sendmail(self.__from_email, self.__to_email, text)
        server.quit()

        attachment.close()

        # Delete pdf file
        if os.path.exists(self.__attach_file_name):
            os.remove(self.__attach_file_name)

def main():
    global g_logger
    logging.basicConfig(filename="Send_Offer_Letter.log", filemode='w', level=logging.DEBUG, )
    g_logger.info("Staring the script")
    details = ExcelSheetReader("python.xlsx")()
    g_logger.debug("main() - details: {}".format(details))
    for name in details.keys():
        offer_letter = CreateOfferLetter("Offer_Letter_TempLate.docx", name, details[name])()
        offer_letter = Word2PdfConverter(offer_letter)()
        SendMail(name, details[name], offer_letter)()

if __name__ == '__main__':
    main()


