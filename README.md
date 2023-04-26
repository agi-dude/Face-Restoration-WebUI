# FaceRestoration WebUI Based on GFPGAN and CodeFormer

This repository contains a FaceRestoration WebUI based on the GFPGAN and CodeFormer models. It provides an easy-to-use interface for users to upload images and restore them using these state-of-the-art models.

## Requirements

Before running this application, ensure that you have Python 3.x installed on your system. If you do not have Python 3.x installed on your system, you can install the latest version (Python 3.10) by following these steps:

1. Go to the official Python download page at https://www.python.org/downloads/.
2. Scroll down to the "Python 3.10.0" section (or the latest version available at the time of installation) and click on the appropriate installer for your operating system.
3. Run the installer and follow the on-screen instructions to complete the installation.

Once Python 3.10 is installed, you can proceed with installing the required packages.
Navigate to the root directory and run the following command to install the requirements:

```pip install -r requirements.txt```

After doing this, download the Models to the root directory from [here](https://drive.google.com/file/d/1gtgzJBd3whhKjtd4g5-SoS8wwN-YC0ZC/view?usp=share_link)

## How to Run

To run the application, navigate to the root directory of the repository and execute the following command:

```python Main.py```

This will start the web server on your local machine. To access the application, open your web browser and navigate to the following URL:

http://localhost:7860

From there, you can upload your images and restore them using the GFPGAN and CodeFormer models.

## Credits

The FaceRestoration WebUI is based on the GFPGAN and CodeFormer models developed by the following authors:

- [Tao Yang](https://github.com/TencentARC/GFPGAN)
- [Xintao Wang](https://github.com/xinntao/CodeFormer)

We are grateful for their contributions to the computer vision community.
