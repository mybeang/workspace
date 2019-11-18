import click
import wr_table
import ch_tp_tables

def spar(string):
    return "\n" + "*" * 10 + " {} ".format(string) + "*" * 10 + "\n"

def file_name(filename):
    """input the filename which want to change the table format"""
    if not filename:
        raise LookupError("Please input the right filename and path")
    else:
        f = open(filename, 'r+')
        test_data = f.read()
        table = wr_table.Table(test_data, wr_table.r_dialect)
        print(spar("Input Data"))
        print(test_data)
        print(spar("Output Data"))
        print(table.to_string())

def string_table(string_table):
    """input the string which want to change the table format"""
    if not string_table:
        msg = """
        Please input the right string table. Refer to example
        """
        raise ValueError(msg)
    else:
        table = wr_table.Table(string_table, wr_table.r_dialect)
        print(table.to_string())

@click.command()
@click.option('--filename', help="input the filename which want to change the table format")
@click.option('--stringtable', help="input the string which want to change the table format")
@click.option('--example', is_flag=True, help="display the example")
def change_type(filename, stringtable, example):
    if filename:
        file_name(filename)
    elif stringtable:
        string_table(stringtable)
    elif example:
        wr_table.example()

if __name__=="__main__":
    change_type()

