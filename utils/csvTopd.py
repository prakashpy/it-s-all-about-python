"""
implementing code to filter csv file based on requested columns
"""

import pandas as pd
import os




def filter_csv(return_as="json"):
    """
    Filter down our data to something displayable based on parameters from the main page.

    :param return_as: json or numpy (default json)
    :returns: the filtered dataset
    """

    my_path = os.path.split(os.path.realpath(__file__))[0]
    csv_path = os.path.join(my_path, "..", "..", "..", "data", "merged_data.csv")
    data = pd.read_csv(csv_path)
    columns = []

    columns.extend("new_column_name")

    data = data.loc[:, columns]

    if return_as == "json":
        return data.to_json(orient="records")
    elif return_as == "numpy":
        return data
    else:
        raise ValueError("return_as must be json or numpy, not " + str(return_as))

if __name__ == "__main__":
    filter_csv()