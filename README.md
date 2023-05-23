## Autoscrape ITTF Rankings

[![](https://img.shields.io/badge/-Dashboard-blue)](https://ittf-autoscrape.onrender.com/) [![Scrape on schedule](https://github.com/kenf1/ITTF-Autoscrape/actions/workflows/scrape.yml/badge.svg?branch=main)](https://github.com/kenf1/ITTF-Autoscrape/actions/workflows/scrape.yml)

This project is a continuation of my previous [ITTF_Rankings](https://github.com/kenf1/TT-DS/tree/main/Rankings) project where I obtained the dataset via R and Python webscraping. In this project, I will be using Python to scrape and build a dashboard of the most current [ITTF Men's Singles rankings](https://www.ittf.com/rankings/).

The __ITTF Men's Singles Rankings__ dataset and SQL database (located in `./data` will be automatically updated on the first of each month. However, I still have the option to update the dataset manually.

***Note:*** To simplify the process and avoid running out of storage on this repo, all files within `./data` folder will be overwritten each time the script is automatically or manually run.