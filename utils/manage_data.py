import pandas as pd
from datetime import date

def import_expenses(input_path):
    """
    Import expenses data from a CSV file.

    Parameters:
    - input_path: Path to the input CSV file

    Returns:
    - DataFrame: DataFrame containing the expenses data
    """
    try:
        expenses_df = pd.read_csv(input_path)
    except FileNotFoundError:
        expenses_df = pd.DataFrame()

    return expenses_df

def add_rows(expenses_df, receipt_data):
    """
    Add rows to the expenses DataFrame from the receipt_data in the function call.

    Parameters:
    - expenses_df: DataFrame containing the expenses data
    - receipt_data: Dictionary containing the expense items to be added to the DataFrame

    Returns:
    - DataFrame: Updated expenses DataFrame with the new rows added
    """

    print(f"Adding rows to expenses DataFrame")

    # Process each item and append to the DataFrame
    new_rows = []
    for item in receipt_data['items']:

        print(f"Adding item: {item['name']}")
        new_row = {
            "Date": receipt_data.get("date", date.today().isoformat()),
            "Vendor": receipt_data.get("vendor", ""),
            "Name": item.get("name", ""),
            "Quantity": item.get("quantity", 1),
            "Price": item.get("price", 0),
            "Category": item.get("category", "Uncategorized"),
            "Payment method": receipt_data.get("payment_method", "Unknown"),
        }
        new_rows.append(new_row)

    # Convert the list of new rows to a DataFrame
    new_rows_df = pd.DataFrame(new_rows)

    print(f"New rows added: {new_rows_df.shape[0]}")
    # Concatenate the new rows DataFrame to the existing expenses DataFrame
    if expenses_df.empty:
        expenses_df = new_rows_df
    else:
        expenses_df = pd.concat([expenses_df, new_rows_df], ignore_index=True)

    return expenses_df


def write_expenses(expenses_df, output_path):
    """
    Write the expenses DataFrame to a CSV file.

    Parameters:
    - expenses_df: DataFrame containing the expenses data
    - output_path: Path to the output CSV file
    """
    expenses_df.to_csv(output_path, index=False)