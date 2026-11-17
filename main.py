import argparse, csv, io, json
from pathlib import Path
from table_extract import extract_tables

def main():
    parser=argparse.ArgumentParser(description="Extract HTML tables to CSV or JSON.")
    parser.add_argument("html",type=Path)
    parser.add_argument("--table",type=int,default=1,help="1-based table index")
    parser.add_argument("--format",choices=("csv","json"),default="csv")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    try: tables=extract_tables(args.html.read_text(encoding="utf-8"))
    except OSError as exc: parser.error(str(exc))
    if args.table<1 or args.table>len(tables): parser.error(f"table index out of range; found {len(tables)} table(s)")
    rows=tables[args.table-1]
    if args.format=="json": result=json.dumps(rows,indent=2,ensure_ascii=False)
    else:
        buffer=io.StringIO(newline="")
        csv.writer(buffer).writerows(rows)
        result=buffer.getvalue().rstrip("\n")
    if args.output: args.output.write_text(result+"\n",encoding="utf-8")
    else: print(result)
    return 0

if __name__=="__main__": raise SystemExit(main())
