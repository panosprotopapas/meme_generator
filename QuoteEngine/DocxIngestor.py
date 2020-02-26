from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .Quote import Quote

class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        doc = docx.Document(path)
        quotes = []
        
        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split('-')
                new_quote = Quote(parsed[0], parsed[1])
                quotes.append(new_quote)
                
        return quotes