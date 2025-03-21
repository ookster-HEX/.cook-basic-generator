

def create_file(name, title, description, ingrd_name, ingrd_qty, istrct):{
open(__name__+".cook", "w").write(
        "metadata:[\n\tname:"+__name__+"\n\t]"
    )

}

print("""
    hello world
    is this multiline?
        do indents get processed
""")