# Lung Nodule Segmentation with fine-tuning of the SAM

This project involves fine-tuning the Segment Anything Model (SAM) for lung nodule segmentation. It includes two main notebooks: one for training the model and one for testing the model.

## Installation

To set up the environment, install the required dependencies listed in the `requirements.txt` file:

```sh
pip install -r requirements.txt

#Directory Structure

Ensure that your project directory is structured as follows:

project/
├── SAM_training.ipynb
├── sam_test.ipynb
├── requirements.txt
├── README.md
└── setup.py

# Dataset
Make sure to place your dataset files in the appropriate paths specified in the notebooks.

For example:

Training images: ../../2 Extracted Data/smaller set to practice /stack_image.tiff
Training masks: ../../2 Extracted Data/smaller set to practice /stack_GT.tiff
Test images: ../../2 Extracted Data/Test/stack_test_image.tiff

Model Checkpoint
After training, the model checkpoint is saved as SAM 256 X 256.pth. This file is loaded in the testing notebook to make predictions.

Acknowledgments
This project utilizes the Segment Anything Model (SAM) from Facebook AI Research.
