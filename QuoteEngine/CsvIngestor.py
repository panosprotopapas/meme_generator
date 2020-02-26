from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .Quote import Quote

class CsvIngestor(IngestorInterface):
    allowed_extensions = ['csv']
    
    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        df = pandas.read_csv(path, header = 0)
        quotes = []
        
        for index, row in df.iterrows():
            new_quote = Quote(row["body"], row["author"])
            quotes.append(new_quote)
            
        return quotes
    