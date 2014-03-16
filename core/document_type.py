# -*- coding: utf-8 -*-
import zipfile
import io 

class types(object):
    oasis_open_document = "oasis_open_document (any version)"
    pdf = "portable document format (any version)"
    xml = "xml"
    html = "html"
    exception = "exception"
    unknown_type = "unknown file type"

def detect_document_type(data):
    if isinstance(data, Exception):
        return types.exception
    if isinstance(data, str):
        data = io.StringIO.StringIO(data)
    try:
        # 1. Sniff for OpenDocument
        magic_bytes_open_document = 'PK'
        data.seek(0)
        first_bytes = data.read(len(magic_bytes_open_document))
        if len(first_bytes) == 0:
            return types.unknown_type
        if first_bytes.decode() == magic_bytes_open_document: # 1.1 Ok it's a ZIP but...
            archive = zipfile.ZipFile(data)
            if 'mimetype' in archive.namelist() and archive.read('mimetype').decode() == 'application/vnd.oasis.opendocument.text': # 1.2 ...if it doesn't have these files it's not an OpenDocument
                return types.oasis_open_document
        # 2. Sniff for PDF
        magic_bytes_pdf = '%PDF'
        data.seek(0)
        first_bytes = data.read(len(magic_bytes_pdf))

        if first_bytes.decode() == magic_bytes_pdf:
            return types.pdf
        # 3. Sniff for HTML and XML
        data.seek(0)
        first_bytes = data.read(200) #200 bytes in, because sometimes there's a really long doctype
        #print first_bytes
        if first_bytes.decode().count('<html') > 0:
            return types.html
        if first_bytes.decode().count('<?xml') > 0:
            return types.xml
    except (UnicodeDecodeError) as exception:
        pass
    finally:
        data.seek(0)
    return types.unknown_type
