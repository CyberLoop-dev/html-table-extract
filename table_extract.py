from html.parser import HTMLParser

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth=0; self.tables=[]; self.table=None; self.row=None; self.cell=None

    def handle_starttag(self,tag,attrs):
        tag=tag.lower()
        if tag=="table":
            if self.depth==0: self.table=[]
            self.depth+=1
        elif self.depth==1 and tag=="tr":
            self.row=[]
        elif self.depth==1 and tag in ("td","th") and self.row is not None:
            self.cell=[]

    def handle_data(self,data):
        if self.depth==1 and self.cell is not None: self.cell.append(data)

    def handle_endtag(self,tag):
        tag=tag.lower()
        if self.depth==1 and tag in ("td","th") and self.cell is not None:
            self.row.append(" ".join("".join(self.cell).split()))
            self.cell=None
        elif self.depth==1 and tag=="tr" and self.row is not None:
            if self.row: self.table.append(self.row)
            self.row=None
        elif tag=="table" and self.depth:
            self.depth-=1
            if self.depth==0 and self.table is not None:
                if self.table: self.tables.append(self.table)
                self.table=None

def extract_tables(source):
    parser=TableParser()
    parser.feed(source)
    parser.close()
    result=[]
    for table in parser.tables:
        width=max((len(row) for row in table),default=0)
        result.append([row+[""]*(width-len(row)) for row in table])
    return result
