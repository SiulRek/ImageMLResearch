import os


def _stringify_elements(iterable):
    """
    Recursively converts the elements in an iterable to strings.

    Args:
        - iterable: The iterable to be converted.

    Returns:
        - The converted iterable with all elements as strings.
    """
    if isinstance(iterable, dict):
        return {key: _stringify_elements(elem) for key, elem in iterable.items()}
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
        return f"{iterable:.4f}"
    msg = f"Values of Type {type(iterable)} cannot be converted to string."
    raise ValueError(msg)


def _transpose_nested_dicts(nested_dict):
    """
    Transposes a nested dictionary.

    Args:
        - nested_dict (dict[str, dict[str, (int|float|bool|str)]]): The
            nested dictionary to transpose.

    Returns:
        - dict[str, dict[str, (int|float|bool|str)]]: The transposed nested
            dictionary.
    """
    transposed_dict = {}
    for outer_key, inner_dict in nested_dict.items():
        for inner_key, value in inner_dict.items():
            if inner_key not in transposed_dict:
                transposed_dict[inner_key] = {}
            transposed_dict[inner_key][outer_key] = value
    return transposed_dict


class MarkdownFileWriter:
    """
    A helper class to write to a Markdown file.

    Args:
        - file_path (str): The file path where the Markdown file will be
            saved.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_dir = os.path.dirname(file_path)
        self.file_lines = []

    def write_title(self, title, level=1, page_break=True):
        """
        Writes a title to the file.

        Args:
            - title (str): The text of the title.
            - level (int, optional): The level of the title, where 1 is the
                highest level. Defaults to 1.
            - page_break (bool, optional): Whether to insert a page break
        """
        if page_break:
            page_break = '\n<div style="page-break-after: always;"></div>\n'
            self.file_lines.append(page_break)
        title = f"{'#' * level} <span style=\"color:blue;\">{title}</span>\n"
        self.file_lines.append(title)

    def write_text(self, text):
        """
        Writes a plain text paragraph to the file.

        Args:
            - text (str): The text to write.
        """
        self.file_lines.append(f"{text}\n")

    def write_key_value(self, key, value):
        """
        Writes a key-value pair in bullet point format to the file.

        Args:
            - key (str): The key text.
            - value (str): The value text.
        """
        self.file_lines.append(f"*    *{key}*: {value}\n")

    def write_key_value_table(self, table_data, key_label="Key", value_label="Value"):
        """
        Writes a table with key-value pairs, where each row contains a key and a
        value.

        Args:
            - table_data (dict[str, (int|float|bool|str)]): Dictionary
                containing key-value pairs.
            - key_label (str, optional): Label of the key column. Defaults
                to "Key".
            - value_label (str, optional): Label of the value column.
                Defaults to "Value".
        """
        if not table_data:
            return

        table_data = _stringify_elements(table_data)
        elements = list(table_data.keys()) + list(table_data.values())
        max_elem_len = max(len(elem) for elem in elements)

        key_header = f"{key_label}".ljust(max_elem_len)
        value_header = f"{value_label}".ljust(max_elem_len)

        self.file_lines.append(f"| {key_header} | {value_header} |")
        self.file_lines.append(f"| {'-' * max_elem_len} | {'-' * max_elem_len} |")
        for key, value in table_data.items():
            padded_key = f"{key}".ljust(max_elem_len)
            padded_value = f"{value}".ljust(max_elem_len)
            self.file_lines.append(f"| {padded_key} | {padded_value} |")
        self.file_lines.append("\n")

    def write_nested_table(self, nested_table_data, transpose=False):
        """
        Writes a nested table with outer keys as column headers and inner keys
        as row headers.

        Args:
            - nested_table_data (dict[str, dict[str,(int|float|bool|str)]]):
                Dictionary of dictionaries.
            - transpose (bool, optional): Whether to transpose the table.
        """
        if not nested_table_data:
            return

        if transpose:
            nested_table_data = _transpose_nested_dicts(nested_table_data)

        nested_table_data = _stringify_elements(nested_table_data)

        def max_elem_length(elements):
            return max(len(elem) for elem in elements)

        headers = list(nested_table_data.keys())
        inner_dict = nested_table_data[headers[0]]
        row_labels = list(inner_dict.keys())

        max_elem_len = 0
        for inner_dict in nested_table_data.values():
            previous_max_elem_len = max_elem_len
            if set(inner_dict.keys()) != set(row_labels):
                for label in inner_dict.keys():
                    if label not in row_labels:
                        row_labels.append(label)
            max_elem_len = max(max_elem_len, previous_max_elem_len)
        max_elem_len = max(max_elem_len, max_elem_length(headers + row_labels))

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
            label = f"{label}"
            row = f"| {label.ljust(max_elem_len)} | "
            for header in headers:
                value = nested_table_data[header].get(label, "N/A").ljust(max_elem_len)
                row += f"{value} | "
            self.file_lines.append(row)
        self.file_lines.append("\n")

    def create_link(self, path, hyperlink_text=None):
        """
        Creates a Markdown hyperlink to a given path.

        Args:
            - path (str): The file path for the link.
            - hyperlink_text (str, optional): The hyperlink text. Defaults
                to "[Link]".

        Returns:
            - str: The Markdown formatted hyperlink.
        """
        relative_path = os.path.relpath(path, self.file_dir)
        markdown_path = relative_path.replace(os.sep, "/")
        link = f"./{markdown_path}"
        hyperlink_text = hyperlink_text or "[Link]"
        return f"[{hyperlink_text}]({link})"

    def write_figure(self, figure_name, path):
        """
        Writes a Markdown image link to the file.

        Args:
            - figure_name (str): The alt text for the figure.
            - path (str): The file path to the figure.
        """
        figure_link = self.create_link(path, figure_name)
        self.file_lines.append(f"!{figure_link}\n")

    def save_file(self):
        """ Saves the file to the specified file path. """
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write("\n".join(self.file_lines))

    def clear_file(self):
        """ Clears all the content of the current file. """
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
