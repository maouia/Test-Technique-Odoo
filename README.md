# Odoo 15 Customization Project

This project is based on Odoo 15, sourced directly from the GitHub repository. It includes customizations for managing post publications and web scraping functionalities.

## Setup

1. **Odoo Version**: The project uses Odoo 15 from the GitHub version. Please ensure you have the correct branch or tag for the Odoo 15 release.

2. **Python Virtual Environment**: A Python virtual environment (`venv`) is created for this project to manage dependencies. Due to the large size of the Odoo folder and the virtual environment, these are not included in the repository. To set up your own environment, follow these steps:
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On Unix or MacOS: `source venv/bin/activate`
   - Install the required packages: `pip install -r requirements.txt`

## Web Scraping

The project utilizes `BeautifulSoup4` and `requests` for web scraping. A Jupyter notebook for testing the scraping script is located in the `scraping_test` folder. The script is designed to extract data from a selected website that matches the project’s needs.

## Custom Models

Custom models for managing post publications are developed and located in the `custom_models/posts_management` folder. These models facilitate the creation and management of posts within the Odoo system.

## Notes

- Ensure that all dependencies are installed before running the project.
- If you encounter issues with large file uploads, consider adjusting GitHub settings or using a different method to manage large files.

For further details or to contribute, please refer to the project's issues and pull requests on GitHub.
