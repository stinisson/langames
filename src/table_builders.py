class HtmlTableBuilder:
    """Produces HTML table code to be inserted into a larger HTML document"""

    def __init__(self):
        self.rows = []

    def set_headers(self, column_headers):
        self.headers = column_headers

    def add_row(self, cells):
        self.rows.append(cells)

    def get_html(self):
        rows_html = self._get_row_html(self.headers)
        for row in self.rows:
            rows_html += self._get_row_html(row)
        return f"<table>\n{rows_html}</table>\n"

    # This method name begins with '_' which is
    # convention for 'private' in Python. It is
    # available outside of the class however,
    # it is just a convention!
    # Also, it could have been a local function
    # in get_html method, it is a matter of taste!
    # Or, a static method, as PyCharm suggests...
    def _get_row_html(self, cells):
        cells_html = ""
        for cell in cells:
            cells_html += f"<td>{cell}</td>"
        return f"  <tr>{cells_html}</tr>\n"


class ConsoleTableBuilder:
    """Produces a simple string to be printed to standard output (console)"""

    def __init__(self, column_width):
        self.column_width = column_width

    def set_headers(self, column_headers):
        self.result = self._format_row(column_headers)

    def add_row(self, cells):
        self.result += self._format_row(cells)

    def get_string_output(self):
        return self.result

    def _format_row(self, values):
        fmtstr = '{:>' + str(self.column_width) + '}'
        result = ''
        for value in values:
            result += fmtstr.format(value)
        return result + "\n"


# TODO: implement this class by filling in the methods
# Hint 1: look in test_tablebuilders.py for expected behaviour!
# Hint 2: CSV stands for comma-separated-values
class CsvTableBuilder:
    """Produces an output string with comma separated values to written to file"""

    def __init__(self):
        pass

    def set_headers(self, column_headers):
        pass

    def add_row(self, cells):
        pass

    def get_csv_text(self):
        pass
