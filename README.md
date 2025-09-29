# ImageMLResearch
ImageMLResearch is a toolkit to help with image-based machine learning projects using Python. It includes functions for data handling, preprocessing, plotting, and more. These functions are combined into a single `Researcher` class to make experimentation easier and more efficient. Please note that this toolkit is specifically designed for image classification tasks and does not support regression problems.

For comprehensive usage instructions and API details, refer to the [official documentation](https://imagemlresearch.readthedocs.io/en/api-development/index.html).


## Installation
You can install ImageMLResearch using pip:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ imlresearch
```
 
 upgrade to the latest version:
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ --upgrade imlresearch
```

📦 **Dependencies**  
This package supports Python 3.10–3.12. When installing, the following libraries and their specific versions will also be installed:

```
tensorflow==2.17.0  
pandas==2.2.2  
matplotlib==3.8.0  
openai==1.34.0  
optuna==3.6.1  
seaborn==0.13.2  
scikit-learn==1.4.1.post1  
opencv-python==4.8.1.78  
```

⚠️ **Important**  
If your current environment already contains different versions of these libraries, `pip` may raise conflicts during installation.  
To avoid such issues, it is **strongly recommended** to install ImageMLResearch in a **clean virtual environment**.

💡 **Optional**  
If you have a compatible GPU and wish to enable GPU acceleration for TensorFlow, you can install the CUDA-enabled version with the following command:

```bash
pip install --cache-dir=/opt/tmp tensorflow[and-cuda]
```

🧪 **Testing**  
The functionality of the code can be tested using the following command:

```python
from imlresearch.tests import run_all_tests
run_all_tests()
```
