import os


def _stringify_elements(iterable):
    """
    Recursively convert the elements in an iterable to strings.

    Parameters
    ----------
    iterable : iterable
        The iterable to be converted.

    Returns
    -------
    iterable
        The converted iterable with all elements as strings.
    """
    if isinstance(iterable, dict):
        return {
            key: _stringify_elements(elem) for key, elem in iterable.items()
        }
    if isinstance(iterable, list):
        return [_stringify_elements(elem) for elem in iterable]
    if isinstance(iterable, tuple):
        return tuple(_stringify_elements(elem) for elem in iterable)
    if isinstance(iterable, set):
        return {_stringify_elements(elem) for elem in iterable}
    if isinstance(iterable, str):
        return iterable
    if isinstance(iterable, (int, bool)):
        return str(iterable)
    if isinstance(iterable, float):
        value = f"{iterable:.4f}" if iterable > 1e-3 else f"{iterable:.4e}"
        return value
    msg = f"Values of type {type(iterable)} cannot be converted to string."
    raise ValueError(msg)


def _transpose_nested_dicts(nested_dict):
    """
    Transpose a nested dictionary.

    Parameters
    ----------
    nested_dict : dict of dict
        The nested dictionary to transpose.

    Returns
    -------
    dict of dict
        The transposed nested dictionary.
    """
    transposed_dict = {}
    for outer_key, inner_dict in nested_dict.items():
        for inner_key, value in inner_dict.items():
            transposed_dict.setdefault(inner_key, {})[outer_key] = value
    return transposed_dict


class MarkdownFileWriter:
    """
    A helper class to write to a Markdown file.

    Parameters
    ----------
    file_path : str
        The file path where the Markdown file will be saved.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_dir = os.path.dirname(file_path)
        self.file_lines = []

    def page_break(self):
        """Insert a page break in the file."""
        self.file_lines.append(
            '\n<div style="page-break-after: always;"></div>\n'
        )

    def write_title(self, title, level=1, page_break=False):
        """
        Write a title to the file.

        Parameters
        ----------
        title : str
            The text of the title.
        level : int, optional
            The level of the title, by default 1.
        page_break : bool, optional
            Whether to insert a page break, by default False.
        """
        if page_break:
            self.page_break()
        title = (
            f"{'#' * level} <span style='color:rgb(105, 169, 201);'>"
            f"{title}</span>\n"
        )
        self.file_lines.append(title)

    def write_text(self, text):
        """
        Write a plain text paragraph to the file.

        Parameters
        ----------
        text : str
            The text to write.
        """
        self.file_lines.append(f"{text}\n")

    def write_key_value(self, key, value):
        """
        Write a key-value pair in bullet point format.

        Parameters
        ----------
        key : str
            The key of the entry.
        value : str
            The value of the entry.
        """
        self.file_lines.append(f"*    *{key}*: {value}\n")

    def write_key_value_table(
        self, table_data, key_label="Key", value_label="Value"
    ):
        """
        Write a table with key-value pairs.

        Parameters
        ----------
        table_data : dict
            Key-value pairs to be displayed in the table.
        key_label : str, optional
            Label of the key column, by default "Key".
        value_label : str, optional
            Label of the value column, by default "Value".
        """
        if not table_data:
            return

        table_data = _stringify_elements(table_data)
        elements = list(table_data.keys()) + list(table_data.values())
        max_elem_len = max(len(elem) for elem in elements)

        key_header = f"{key_label}".ljust(max_elem_len)
        value_header = f"{value_label}".ljust(max_elem_len)

        self.file_lines.append(f"| {key_header} | {value_header} |")
        self.file_lines.append(
            f"| {'-' * max_elem_len} | {'-' * max_elem_len} |"
        )

        for key, value in table_data.items():
            padded_key = f"{key}".ljust(max_elem_len)
            padded_value = f"{value}".ljust(max_elem_len)
            self.file_lines.append(f"| {padded_key} | {padded_value} |")
        self.file_lines.append("\n")

    def write_nested_table(self, nested_table_data, transpose=False):
        """
        Write a nested table with outer keys as column headers.

        Parameters
        ----------
        nested_table_data : dict of dict
            Dictionary of dictionaries representing the table.
        transpose : bool, optional
            Whether to transpose the table, by default False.
        """
        if not nested_table_data:
            return

        if transpose:
            nested_table_data = _transpose_nested_dicts(nested_table_data)

        nested_table_data = _stringify_elements(nested_table_data)

        headers = list(nested_table_data.keys())
        row_labels = list(nested_table_data[headers[0]].keys())

        max_elem_len = max(
            len(header) for header in headers + row_labels
        )

        header_row = (
            f"| {' ' * max_elem_len} | "
            + " | ".join(header.ljust(max_elem_len) for header in headers)
            + " |"
        )
        self.file_lines.append(header_row)
        self.file_lines.append(
            f"| {'-' * max_elem_len} | "
            + " | ".join("-" * max_elem_len for _ in headers)
            + " |"
        )

        for label in row_labels:
            row = f"| {label.ljust(max_elem_len)} | "
            for header in headers:
                value = nested_table_data[header].get(label, "N/A").ljust(
                    max_elem_len
                )
                row += f"{value} | "
            self.file_lines.append(row)
        self.file_lines.append("\n")

    def create_link(self, path, hyperlink_text=None):
        """
        Create a Markdown hyperlink to a given path.

        Parameters
        ----------
        path : str
            The file path for the link.
        hyperlink_text : str, optional
            The hyperlink text, by default None.

        Returns
        -------
        str
            The Markdown formatted link.
        """
        relative_path = os.path.relpath(path, self.file_dir)
        markdown_path = relative_path.replace(os.sep, "/")
        link = f"./{markdown_path}"
        return f"[{hyperlink_text or '[Link]'}]({link})"

    def write_figure(self, figure_name, path):
        """
        Write a Markdown image link to the file.

        Parameters
        ----------
        figure_name : str
            The alt text for the figure.
        path : str
            The file path to the figure.
        """
        self.file_lines.append(f"!{self.create_link(path, figure_name)}\n")

    def save_file(self):
        """Save the file to the specified file path."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write("\n".join(self.file_lines))

    def clear_file(self):
        """Clear all the content of the current file."""
        self.file_lines = []


if __name__ == "__main__":
    nested_table_data = {
        "Model 1": {
            "Metric 1": 10.30303,
            "Metric 2": 10.30303,
            "Metric 3": 10.30303,
        },
        "Model 2": {
            "Metric 1": "0.85",
            "Metric 2": "0.75",
            "Metric 3": "0.65",
            "Metric 4": "0.95",
        },
    }

    writer = MarkdownFileWriter("example.md")
    writer.write_title("Example Markdown File")
    writer.write_text("This is an example Markdown file.")
    writer.write_nested_table(nested_table_data)
    writer.save_file()
