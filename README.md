**iPhone Data Pipeline** 

This project focuses on cleaning, transforming, and visualizing a dataset of used iPhones. The goal is to extract meaningful insights from the raw data and present them in a clear and interpretable format.

**Overview**

The pipeline processes an iPhone dataset, including:

Data cleaning (handling missing values, standardizing features, etc.)

Feature engineering

Visualization of key trends in pricing, storage, and model availability

**Project Structure**

src/pipeline.py – Main script that performs all steps of the pipeline: loading, cleaning, analyzing, and plotting

data/ – Folder for storing cleaned or original data (optional)

charts_file.png – Output chart generated from the pipeline script

iphonedatapipeline.py – Original version of the script, kept for reference

README.md – Project overview and usage guide

**Dependencies**

This project uses Python and the following libraries:

pandas

matplotlib

To install the dependencies, run:

pip install pandas matplotlib

**How to Run**

Clone the repository:

git clone https://github.com/vythwahh/iphone-data-pipeline.git


Navigate into the project folder:

cd iphone-data-pipeline


Run the script:

python src/pipeline.py


The script will generate a chart and save it as charts_file.png.

**Notes**

The dataset was manually collected and may require updates in the future.

Further improvements could include deploying the analysis as a web dashboard or exporting cleaned data into a database.
