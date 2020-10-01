from src.table_builders import CsvTableBuilder, ConsoleTableBuilder, HtmlTableBuilder


def test_simple_2x2_csv_table():
    builder = CsvTableBuilder()
    builder.set_headers(['Anna', 'Kalle'])
    builder.add_row(['1', '2'])
    builder.add_row(['3', '4'])
    expected = 'Anna,Kalle\n1,2\n3,4'
    got = builder.get_csv_text()
    assert expected == got


def test_simple_2x2_text_table():
    builder = ConsoleTableBuilder(column_width=10)
    builder.set_headers(['Anna', 'Kalle'])
    builder.add_row(['1', '2'])
    builder.add_row(['3', '4'])
    # TODO: Fill in expected string below!
    expected = ''
    got = builder.get_string_output()
    assert expected == got


def test_simple_2x2_html_table():
    builder = HtmlTableBuilder()
    builder.set_headers(['Anna', 'Kalle'])
    builder.add_row(['1', '2'])
    builder.add_row(['3', '4'])
    expected = '''\
<table>
  <tr><td>Anna</td><td>Kalle</td></tr>
  <tr><td>1</td><td>2</td></tr>
  <tr><td>3</td><td>4</td></tr>
</table>
'''
    got = builder.get_html()
    assert expected == got
