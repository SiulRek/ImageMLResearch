from os import name

from imlresearch.utils.general.batch_utils import unbatch_dataset_if_batched
from imlresearch.utils.general.get_sample_from_distribution import (
    get_sample_from_distribution,
)
from imlresearch.utils.general.logger import Logger
from imlresearch.utils.general.markdown_file_writer import MarkdownFileWriter
from imlresearch.utils.general.search_files_with_name import search_files_with_name
from imlresearch.utils.general.time_utils import get_datetime, get_duration, add_durations
from imlresearch.utils.general.transform_figures_to_files import transform_figures_to_files
from imlresearch.utils.general.send_chatgpt_prompt import send_chatgpt_prompt