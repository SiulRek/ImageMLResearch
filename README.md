# ImageMLResearch

[![Python 3.10–3.12](https://img.shields.io/badge/python-3.10%E2%80%933.12-blue.svg)](https://www.python.org/downloads/)

ImageMLResearch is a toolkit to help with image-based machine learning projects using Python. It includes functions for data handling, preprocessing, plotting, and more. These functions are combined into a single `Researcher` class to make experimentation easier and more efficient. Please note that this toolkit is specifically designed for image classification tasks and does not support regression problems.

For comprehensive usage instructions and API details, refer to the [official documentation](https://imagemlresearch.readthedocs.io/en/api-development/index.html).


## Installation
You can install ImageMLResearch using pip:

```bash
pip install imlresearch
```
 
 upgrade to the latest version:
```bash
pip install --upgrade imlresearch
```

📦 **Core Dependencies**  
This package supports Python 3.10–3.12. When installing, the following core libraries will also be installed:

```
numpy>=1.23.5,<2
tensorflow>=2.13,<2.18
optuna>=3.3,<4.8
opencv-python>=4.8,<4.14
scikit-learn>=1.4,<1.8
seaborn>=0.12.0,<=0.13.2
```

📦 **Optional Dependency for AI Report Generation**

```
openai==1.34.0
```

Install with:
```bash
pip install imlresearch[ai-report]
```

💡 **Optional GPU Support for TensorFlow**  
If you have a compatible GPU and wish to enable GPU acceleration for TensorFlow, you can install the CUDA-enabled version with the following command:

```bash
pip install --cache-dir=/opt/tmp tensorflow[and-cuda]
```

🧪 **Testing**  
The functionality of the code can be tested using the following command:

```python
from imlresearch.api.tests import run_all_tests
run_all_tests()
```
