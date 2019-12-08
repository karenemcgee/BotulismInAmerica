# A Look at Botulism Through History

This project uses historical data from the Centers for Disease Control and Prevention (https://www.cdc.gov/botulism/index.html) to explore and analyze trends in Botulism in the United States since 1897. 

After initial exploration, analysis, and cleanup of the raw data using Jupyter Notebook, all of the data was pulled into a SQLite database due to the overall portability and easy accessibility of SQLite via Flask app. In Flask, we created multiple routes to serve up each of the JSONs needed for our analysis. We used D3, Plotly, and Observable to create dynamic visualizations into which we fed the JSON and CSV data. To style our HTML, we used a free Bootstrap theme called Lux, customized to fit our needs.

### TOXIN DETAIL: TOTAL NUMBER OF CASES BY BOTULISM TYPES, TOXIN TYPES

This first visualization is a dynamic bar chart that shows the total number of cases of botulism since 1897 broken down by botulism type (select one: foodborne, infant, or wound) and toxin type. 



In addition to the data visualizations, this web page also provides:
* A full view of all of the raw data
* Details about how the data was cleaned
* Information about the history of botulism, each of its types and toxins, and safety and prevention tips

## Deployment
1. Clone this repository, making sure all file structures remain the same
2. Run the Flask app to activate LocalHost
3. Open your LocalHost server to view the data
