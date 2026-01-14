import pandas as pd

def clean_data(df):
    """Clean the dataset by handling missing values and ensuring consistency."""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    fuel_columns = [col for col in df.columns if 'Fuel Flow Rate' in col]
    df[fuel_columns] = df[fuel_columns].fillna(0)

    power_columns = [col for col in df.columns if 'Power (MW)' in col]
    df[power_columns] = df[power_columns].fillna(0)

    df['Sea Temperature (Celsius)'] = df['Sea Temperature (Celsius)'].interpolate()

    df = df.dropna(subset=['Vessel Name', 'Start Time', 'End Time'])
    
    return df
