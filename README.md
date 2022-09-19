# Topic Extraction for Daily Financial News


## Architecture Diagram

This project uses PySpark, SparkNLP, Databricks and Github Codespaces to extract topics from approximately 1.4M financial news titles from Kaggle.

![databricks (4)](https://user-images.githubusercontent.com/112586823/191080189-694285cc-cc96-439c-9bf7-313a58806685.jpg)

## Media

## User Instructions

To run the FastAPI app, type in terminal:

`$uvicorn fastapi-app:app --reload`

Open the link in the browser and append `/getannotation/{financial_news_heading}` to the URL to get a list of topics found.

Example:

Text: `Microsoft is one of the biggest tech companies listed with Nasdaq.` 

Results: `["Microsoft", "tech", "companies", "Nasdaq"]`

## Steps Taken to Setup Databricks Cluster
1. Create and start cluster
2. Under 'Libraries' tab, install two libraries
    ```spark-nlp``` using PyPI
    ```com.johnsnowlabs.nlp:spark-nlp_2.12:4.1.0``` using Maven
3. Create a new notebook and attach to cluster
4. Run ```$pip install kaggle```
5. Place ```kaggle.json``` in ```/root/.kaggle```
6. Download dataset using ```$kaggle download datasets -d miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests```
7. Move file to ```/dbfs/FileStore```
8. Unzip file using ```$unzip massive-stock-news-analysis-db-for-nlpbacktests.zip```

## Steps Taken to Setup Codespaces
1. Install same python version as on cluster
    
    ```
    sudo apt install build-essential checkinstall
    cd /opt/
    sudo wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz
    sudo tar xzf Python-3.8.10.tgz
    cd Python-3.8.10
    sudo ./configure --enable-optimizations
    sudo make altinstall
    python3.8 -V
    ```
    
2. Create virtualenv with python3.8.10
   ```
    virtualenv --python="/usr/local/bin/python3.8" ~/.venv
    ```
    
3. Install Java 8 for databricks-connect

    ```
    curl -s "https://get.sdkman.io" | bash
    source "$HOME/.sdkman/bin/sdkman-init.sh"
    sdk install java
    sdk install java 8.0.302-open
    java -version
    ```

4. Execute ```make install```

5. Execute ```databricks-connect configure```
    
6. Execute ```databricks-connect test```

7. Set python interpreter in vscode → cmd + shift + P
