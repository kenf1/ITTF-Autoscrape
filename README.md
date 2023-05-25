## Autoscrape ITTF Rankings

[![](https://img.shields.io/badge/-Dashboard-blue)](https://ittf-autoscrape.onrender.com/) [![Scrape on schedule](https://github.com/kenf1/ITTF-Autoscrape/actions/workflows/scrape.yml/badge.svg?branch=main)](https://github.com/kenf1/ITTF-Autoscrape/actions/workflows/scrape.yml)

This project is a continuation of my previous [ITTF_Rankings](https://github.com/kenf1/TT-DS/tree/main/Rankings) project where I obtained the dataset via R and Python webscraping. In this project, I will be using Python to scrape all ITTF rankings and build a dashboard of the most current [ITTF Men's Singles rankings](https://www.ittf.com/rankings/).

The following table is a reference for how the files inside `./data` are named.

|Full Name|Shorthand|
|---|---|
|Men’s Singles|MS|
|Women’s Singles|WS|
|Men’s Doubles Pairs|MD|
|Women’s Doubles Pairs|WD|
|Men’s Doubles Individuals|MDI|
|Women’s Doubles Individuals|WDI|
|Mixed Doubles Pairs|XD|
|Mixed Doubles Individuals|XDI|

All of the `.csv` datasets and `player_rank.db` SQL database (located in `./data` will be automatically updated on the first of each month. However, I still have the option to update the dataset manually.

***Note:*** To simplify the process and avoid running out of storage on this repo, all files within `./data` folder will be overwritten each time the script is automatically or manually run.

### Streamlit App

To run streamlit app, run the following in Shell:

```{shell}
cd app
python3 -m streamlit run Home.py
```

or

```{shell}
sh startApp.sh
```
