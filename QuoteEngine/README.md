## Quote Engine Module

Responsible for ingesting four types of files that contain quotes (`.csv`, `.pdf`, `.docx`, and `.txt`) of the form `<body> - <author>` (`.pdf`, `.docx`, and `.txt`) and of the form `<body>,<author>` (`.csv`). 

The Quote class has two values, `body` and `author`.

The `Ingestor` class  checks whether one of the sub-ingestor classes can ingest a given file type, and if one is found, assings the parsing of the file to that sub-ingestor parser.

Each of the four allowed file types mentioned above has a separate sub-ingestor class (e.g. `DocxIngestor`); a child of the `IngestorInteface` abstract class. Each sub-ingestor class has two instance methods:

- `can_ingest` which decides whether the sub-ingestor can parse a file. 

   ```python
   can_ingest(path_to_file) -> bool
   ```
   
- `parse` which parses each body-author pair in the file into a separate Quote object.
 	```python
   parse(path_to_file) -> List[Quote]
   ```



