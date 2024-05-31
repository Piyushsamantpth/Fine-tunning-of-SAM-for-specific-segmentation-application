from setuptools import setup, find_packages

setup(
    name='lung_nodule_segmentation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tifffile==2021.7.2',
        'numpy==1.23.5',
        'Pillow==9.4.0',
        'scipy==1.10.1',
        'datasets==2.13.1',
        'patchify==0.2.3',
        'matplotlib==3.7.1',
        'transformers==4.31.0',
        'torch==2.0.1',
        'monai==1.2.0',
        'tqdm==4.65.0',
    ],
    description='A project for fine-tuning the Segment Anything Model (SAM) for lung nodule segmentation.',
    author='Piyush Samant',
    author_email='piyushsamant88@gmail.com',
    url='https://github.com/Piyushsamantpth/Fine-tunning-of-SAM-for-specific-segmentation-application',
)
