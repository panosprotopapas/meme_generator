from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .Quote import Quote

class PdfIngestor(IngestorInterface):
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        tmp = f'.{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        
        file_ref = open(tmp, "r")
        quotes = []
        
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = Quote(parse[0], parse[1])
                quotes.append(new_quote)
                
        file_ref.close()
        os.remove(tmp)
        return quotes