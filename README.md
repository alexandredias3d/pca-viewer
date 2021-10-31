# Principal Component Analysis (PCA) Viewer

This is a simple Dash application that loads a dataset and make a scatter plot to visualize the results.

### How to use

Following are the steps needed to run this application:

1. Install Python 3.9 or greater
2. Install pipenv using pip
   ```
   pip install pipenv
   ```
3. Install third party packages with Pipenv
   ```
   pipenv install
   ```
4. Run the Dash application inside the environment created by pipenv
   ```
   pipenv run python app.py
   ```
5. Load a .CSV file
6. Select the columns to run the PCA algorithm on using the checkboxes
7. Select the column to colorize the plot (optional)
8. Click the button to run the PCA algorithm and plot the data

### Example

![Example of PCA Viewer usage](screenshot/iris-dataset.png?raw=true "PCA results")