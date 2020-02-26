from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import Quote
from .DocxIngestor import DocxIngestor
from .CsvIngestor import CsvIngestor
from .PdfIngestor import PdfIngestor
from .TxtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CsvIngestor, PdfIngestor, TxtIngestor]
    
    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
                
    