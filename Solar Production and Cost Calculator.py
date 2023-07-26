def calculate_solar_production_percentage(input_voltage, pv_voltage, battery_voltage, load_in_kw):
  """Calculates the solar production in percentage.

  Args:
    input_voltage: The input voltage.
    pv_voltage: The PV voltage.
    battery_voltage: The battery voltage.
    load_in_kw: The load in kW.

  Returns:
    The solar production in percentage.
  """

  solar_production = (pv_voltage - battery_voltage) / (input_voltage - battery_voltage)
  solar_production_percentage = solar_production * 100

  return solar_production_percentage


def main():
  input_voltage = float(input("Enter the input voltage: "))
  pv_voltage = float(input("Enter the PV voltage: "))
  battery_voltage = float(input("Enter the battery voltage: "))

  # Ask user to select option to enter load in kW or W
  load_in_unit = input("Enter load in kW (k) or W (w): ")

  if load_in_unit == "k":
    load_in_kw = float(input("Enter the load in kW: "))
  else:
    load_in_w = float(input("Enter the load in W: "))
    load_in_kw = load_in_w / 1000

  hours_of_solar_run = float(input("Enter the hours of solar run: "))

  solar_production_percentage = calculate_solar_production_percentage(
      input_voltage, pv_voltage, battery_voltage, load_in_kw)

  print("Solar production percentage:", solar_production_percentage)

  # Calculate the power produced by the solar panels
  power_produced_by_solar_panels = 2.01 * hours_of_solar_run

  # Ask user to enter cost of electricity
  cost_of_electricity = float(input("Enter the cost of electricity: "))

  # Ask user to enter number of days
  number_of_days = float(input("Enter the number of days: "))

  # Calculate the cost of electricity per day
  cost_of_electricity_per_day = power_produced_by_solar_panels * cost_of_electricity

  # Calculate the cost of electricity over 30 days
  cost_of_electricity_over_30_days = cost_of_electricity_per_day * number_of_days

  print("Power produced per day:", power_produced_by_solar_panels)
  print("Cost of electricity per day:", cost_of_electricity_per_day)
  print("Cost of electricity over 30 days:", cost_of_electricity_over_30_days)


if __name__ == "__main__":
  main()
