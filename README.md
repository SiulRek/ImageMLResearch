# ImageMLResearch
ImageMLResearch is a toolkit to help with image-based machine learning projects using Python. It includes functions for data handling, preprocessing, plotting, and more. These functions are combined into a single `Researcher` class to make experimentation easier and more efficient. Please note that this toolkit is specifically designed for image classification tasks and does not support regression problems.

## Installation
You can install ImageMLResearch using pip:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ imlresearch
```

📦 **Dependencies**

When installing this package, the following libraries and their specific versions will also be installed:

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
