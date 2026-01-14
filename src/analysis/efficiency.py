import pandas as pd
import numpy as np

def calculate_bsfc(df):
    """Calculate Brake Specific Fuel Consumption (g/kWh)."""

    power_kw = df['Propulsion Power (MW)'] * 1000
    fuel_flow_g = df['Total Main Engine Fuel Flow Rate (kg/h)'] * 1000
  
    valid_mask = (power_kw > 0) & (fuel_flow_g >= 0)

    bsfc = pd.Series(np.nan, index=df.index)

    bsfc[valid_mask] = fuel_flow_g[valid_mask] / power_kw[valid_mask]
    
    bsfc[bsfc > 1000] = np.nan
    
    return bsfc

def calculate_fuel_per_nm(df):
    """Calculate fuel consumption per nautical mile (kg/nm)."""
 
    valid_mask = (df['Distance (nm)'] > 0) & (df['Fuel Consumed (kg)'] >= 0)
  
    fuel_per_nm = pd.Series(np.nan, index=df.index)
    
    fuel_per_nm[valid_mask] = df['Fuel Consumed (kg)'][valid_mask] / df['Distance (nm)'][valid_mask]

    fuel_per_nm[fuel_per_nm > 1000] = np.nan
    
    return fuel_per_nm
