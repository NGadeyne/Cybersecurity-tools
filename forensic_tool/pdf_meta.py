#! /usr/bin/env python3
# coding:utf8

import PyPDF2

def get_pdf_meta(file_name):
    pdf_file = PyPDF2.PdfFileReader(open(file_name, "rb"))
    doc_info = pdf_file.getDocumentInfo()
    for info in doc_info:
        print("[+]" + info + " " + doc_info[info])