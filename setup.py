from setuptools import setup, find_packages
from youtube_downloader import download_youtube_video
from text_copier import copy_text
from form_handler import fill_form_and_upload_document

# Example usage
#download_youtube_video('https://youtube.com/example', '/path/to/download')
#copy_text('/path/source.txt', '/path/destination.txt')
#fill_form_and_upload_document('https://example.com/form', {'name': 'John', 'email': 'email@example.com'}, '/path/to/document.pdf')




# Read the contents of your requirements.txt file
with open("requirements.txt") as f:
    required = f.read().splitlines()

# Read the contents of your README.md file for the project description
with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="self-operating-computer",
    version="1.4.6",
    packages=find_packages(),
    install_requires=required,  # Add dependencies here
    entry_points={
        "console_scripts": [
            "operate=operate.main:main_entry",
        ],
    },
    package_data={
        # Include the file in the operate.models.weights package
        "operate.models.weights": ["best.pt"],
    },
    long_description=long_description,  # Add project description here
    long_description_content_type="text/markdown",  # Specify Markdown format
    # include any other necessary setup options here
)
