from src.table_builders import CsvTableBuilder, ConsoleTableBuilder


def test_simple_2x2_csv_table():
    builder = CsvTableBuilder(column_headers=['Anna', 'Kalle'])
    builder.add_row(['1', '2'])
    builder.add_row(['3', '4'])
    expected = '''\
Anna,Kalle
1,2
3,4
'''
    got = builder.get_csv_text()
    assert expected == got


def test_simple_2x2_text_table():
    builder = ConsoleTableBuilder(column_headers=['Anna', 'Kalle'], column_width=10)
    builder.add_row(['1', '2'])
    builder.add_row(['3', '4'])
    expected = '''\
      Anna     Kalle
         1         2
         3         4
'''
    got = builder.get_string_output()
    assert expected == got
