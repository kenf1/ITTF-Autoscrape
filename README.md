## Autoscrape ITTF Rankings

[![](https://img.shields.io/badge/-Dashboard-blue)](https://kenf1-ittf-autoscrape-app-8bze4y.streamlit.app/) [![Scrape on schedule](https://github.com/kenf1/ITTF-Autoscrape/actions/workflows/actions.yml/badge.svg)](https://github.com/kenf1/ITTF-Autoscrape/actions/workflows/actions.yml)

This project is a continuation of my previous [ITTF_Rankings](https://github.com/kenf1/TT-DS/tree/main/Rankings) project where I obtained the dataset via R and Python webscraping. In this project, I will be using Python to scrape and build a dashboard of the most current [ITTF Men's Singles rankings](https://www.ittf.com/rankings/).

The __ITTF Men's Singles Rankings__ dataset (located in `data/dataset.csv` will be automatically updated monthly. However, I still have the option to update the dataset manually.

***Note:*** To simplify the process and avoid running out of storage on this repo, both `data/dataset.csv` and `data/metadata.csv` will be overwritten each time the script is automatically or manually run.