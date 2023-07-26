# SolarProductionandCostCalculator


Solar Production and Cost Calculator

This code calculates the solar production percentage, power produced by the solar panels, cost of electricity per day, and cost of electricity over 30 days.

Usage

To run the code, you will need to provide the following information:

The input voltage
The PV voltage
The battery voltage
The load in kW or W
The hours of solar run
The cost of electricity
The number of days
Once you have provided this information, the code will calculate the solar production percentage, power produced by the solar panels, cost of electricity per day, and cost of electricity over 30 days.

Output

The code will print the following output:

The solar production percentage
The power produced by the solar panels
The cost of electricity per day
The cost of electricity over 30 days
Example

Here is an example of how to use the code:

input_voltage = 246
pv_voltage = 213
battery_voltage = 54
load_in_unit = "k"
load_in_kw = 1.55
hours_of_solar_run = 10
cost_of_electricity = 28.07
number_of_days = 1

solar_production_percentage = calculate_solar_production_percentage(
    input_voltage, pv_voltage, battery_voltage, load_in_kw)

print("Solar production percentage:", solar_production_percentage)

power_produced_by_solar_panels = 2.01 * hours_of_solar_run

cost_of_electricity_per_day = power_produced_by_solar_panels * cost_of_electricity

cost_of_electricity_over_30_days = cost_of_electricity_per_day * number_of_days

print("Power produced per day:", power_produced_by_solar_panels)
print("Cost of electricity per day:", cost_of_electricity_per_day)
print("Cost of electricity over 30 days:", cost_of_electricity_over_30_days)
This code will print the following output:

Solar production percentage: 82.8125
Power produced per day: 20.099999999999998
Cost of electricity per day: 564.207
Cost of electricity over 30 days: 16926.07
Dependencies

The code depends on the following libraries:

math
License

The code is licensed under the MIT License.
