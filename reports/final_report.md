# Cruise Ship Performance Analysis Report

## Introduction
This report analyzes the performance trends of two cruise ships, Vessel 1 and Vessel 2, focusing on propulsion efficiency, power generation, and overall energy efficiency using the provided dataset.

## Methodology
- **Data Cleaning**: Handled missing values and ensured consistency
- **Feature Engineering**: Calculated total fuel consumption, electrical power, and distance traveled
- **Efficiency Metrics**: Computed BSFC and fuel per nautical mile
- **KPIs**: Selected based on IMO SEEMP guidelines, focusing on operational efficiency

## Key Findings

1. **Propulsion Efficiency**:
   - Both vessels show similar BSFC (Brake Specific Fuel Consumption) distributions
   - Vessel 2 has slightly higher fuel consumption per nautical mile
   - Both vessels operate most frequently in the 10-20 MW propulsion power range

2. **Electrical Power Consumption**:
   - Vessel 1 shows more consistent electrical power demand
   - Vessel 2 exhibits higher peak electrical loads
   - Both vessels maintain base electrical loads around 5-8 MW

## Analysis Details

### Power Consumption Patterns
- Propulsion power distribution shows bi-modal patterns for both vessels
- Main operating points are observed at:
  - Low power (5-10 MW): port maneuvering
  - Medium power (15-20 MW): normal cruising
- Electrical consumption follows expected patterns with:
  - Base hotel load (5-8 MW)
  - Peak loads during high HVAC demand periods

### Efficiency Metrics
- BSFC values indicate:
  - Normal operating range: 180-220 g/kWh
  - Higher values during low-load conditions
  - Similar efficiency patterns between vessels

## Recommendations
1. Optimize propulsion power management during low-load operations
2. Implement load leveling strategies for electrical systems
3. Consider operation profile adjustments to maximize time in efficient power ranges

## Repository Navigation
- Raw data: `data/raw/data.csv`
- Notebooks: `notebooks/`
  - `data_exploration.ipynb`
  - `efficiency_analysis.ipynb`
  - `vessel_comparison.ipynb`
- Figures: `reports/figures/`
  - `propulsion_power_distribution.png`
  - `electrical_power_distribution.png`
  - `bsfc_distribution.png`