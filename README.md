# Manufacturing BOM Cleaning Pipeline

Python pipeline developed to clean and standardize BOM data for MPS and CTB analysis in a manufacturing environment.

## Project Objective

This project automates the BOM cleaning process usually performed manually by production planners and MPS teams.

The pipeline reduces manual cleaning time and prepares BOM data for future supply chain analysis.

## Technologies Used

- Python
- Pandas

## Main Tasks

- Import BOM CSV file
- Remove unnecessary columns
- Remove empty columns
- Validate duplicates
- Filter specific Finished Goods
- Standardize column names
- Clean text columns
- Validate data types
- Sort data
- Export clean BOM file

## Final Output

Clean BOM dataset ready for:
- MPS analysis
- CTB analysis
- Supply chain planning
- Manufacturing analytics

## Output File

```text
clean_bom_project.csv