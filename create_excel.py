import pandas as pd

# Load the Kalman filter results
results = pd.read_csv('kalman_results.csv')

# Create Excel writer
with pd.ExcelWriter('Temperature_Analysis.xlsx', engine='openpyxl') as writer:
    # Sheet 1: Raw data
    results.to_excel(writer, sheet_name='Data', index=False)
    
    # Sheet 2: Statistics
    stats = pd.DataFrame({
        'Metric': ['Mean', 'Std Dev', 'Min', 'Max', 'Range'],
        'Sensor_A_Close': [
            results['Sensor_A_Close'].mean(),
            results['Sensor_A_Close'].std(),
            results['Sensor_A_Close'].min(),
            results['Sensor_A_Close'].max(),
            results['Sensor_A_Close'].max() - results['Sensor_A_Close'].min()
        ],
        'Sensor_B_Far': [
            results['Sensor_B_Far'].mean(),
            results['Sensor_B_Far'].std(),
            results['Sensor_B_Far'].min(),
            results['Sensor_B_Far'].max(),
            results['Sensor_B_Far'].max() - results['Sensor_B_Far'].min()
        ],
        'Bulb_Estimate': [
            results['Bulb_Estimate'].mean(),
            results['Bulb_Estimate'].std(),
            results['Bulb_Estimate'].min(),
            results['Bulb_Estimate'].max(),
            results['Bulb_Estimate'].max() - results['Bulb_Estimate'].min()
        ]
    })
    stats.to_excel(writer, sheet_name='Statistics', index=False)
    
    # Sheet 3: Key time points
    key_times = [0, 100, 200, 300, 400, 500, 600]
    indices = [t//10 for t in key_times]
    key_data = results.iloc[indices].copy()
    key_data.to_excel(writer, sheet_name='Key_Points', index=False)

print('Excel file created: Temperature_Analysis.xlsx')
print('\nSheets:')
print('1. Data - Complete time series (61 points)')
print('2. Statistics - Mean, Std, Min, Max, Range')
print('3. Key_Points - Samples at t=0,100,200,300,400,500,600s')
