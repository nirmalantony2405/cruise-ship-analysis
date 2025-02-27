import pandas as pd

def engineer_features(df):
    """Engineer additional features for analysis."""
    # Total main engine fuel flow rate
    fuel_cols = [col for col in df.columns if 'Main Engine' in col and 'Fuel Flow Rate' in col]
    df['Total Main Engine Fuel Flow Rate (kg/h)'] = df[fuel_cols].sum(axis=1)
    
    # Total electrical power consumption (excluding propulsion)
    electrical_cols = ['Power Galley 1 (MW)', 'Power Galley 2 (MW)', 'Power Service (MW)',
                      'HVAC Chiller 1 Power (MW)', 'HVAC Chiller 2 Power (MW)', 'HVAC Chiller 3 Power (MW)',
                      'Scrubber Power (MW)', 'Bow Thruster 1 Power (MW)', 'Bow Thruster 2 Power (MW)',
                      'Bow Thruster 3 Power (MW)', 'Stern Thruster 1 Power (MW)', 'Stern Thruster 2 Power (MW)']
    df['Total Electrical Power Consumption (MW)'] = df[electrical_cols].sum(axis=1)
    
    # Total generator power
    generator_cols = [col for col in df.columns if 'Diesel Generator' in col and 'Power' in col]
    df['Total Generator Power (MW)'] = df[generator_cols].sum(axis=1)
    
    # Distance traveled per interval (5 minutes = 5/60 hours)
    df['Distance (nm)'] = df['Speed Over Ground (knots)'] * (5 / 60)
    
    # Fuel consumed per interval
    df['Fuel Consumed (kg)'] = df['Total Main Engine Fuel Flow Rate (kg/h)'] * (5 / 60)
    
    return df