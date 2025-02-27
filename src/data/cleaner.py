import pandas as pd

def clean_data(df):
    """Clean the dataset by handling missing values and ensuring consistency."""
    # Convert timestamps
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # Fill missing fuel flow rates with 0 
    fuel_columns = [col for col in df.columns if 'Fuel Flow Rate' in col]
    df[fuel_columns] = df[fuel_columns].fillna(0)
    
    # Fill missing power values with 0 
    power_columns = [col for col in df.columns if 'Power (MW)' in col]
    df[power_columns] = df[power_columns].fillna(0)
    
    # Interpolate environmental data where appropriate
    df['Sea Temperature (Celsius)'] = df['Sea Temperature (Celsius)'].interpolate()
    
    # Remove rows with critical missing data 
    df = df.dropna(subset=['Vessel Name', 'Start Time', 'End Time'])
    
    return df