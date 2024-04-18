# COVID19 Data Pipeline Automation using Apache Airflow
A final project at DigitalSkola, development of an end-to-end data pipeline for managing COVID19 data from Jawa Barat.  
- Staging Area: Utilized MySQL database as the staging area for initial data storage
- Data Processing Steps: 
  - Extracted data from the COVID19 API. 
  - Transformed and aggregated the data to facilitate analysis.
  - Populated predetermined facts and dimension tables for structured storage. 
- Scheduling Tool: Leveraged Apache Airflow as the scheduling tool to orchestrate and automate pipeline workflow 
- Target Database: Deployed PostgreSQL as the target database to store processed data. 


## ETL Architecture Diagram
![Screenshot 2022-07-20 150201](https://user-images.githubusercontent.com/75570657/179929690-0f4bfa0e-7102-4bb0-9338-1c0766f55b60.png)

## Integration Design Diagram
![Screenshot 2022-07-20 150255](https://user-images.githubusercontent.com/75570657/179929899-8988a439-c06f-4091-b2b2-5615fcbbc117.png)


## File Structure 
![satructure](https://user-images.githubusercontent.com/75570657/179929313-c4186375-03b2-4eea-9ada-e4a9345578e0.png)
