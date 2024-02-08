import covid19

def get_covid19_stats(country):
    """
    Get COVID-19 statistics for a specific country.
    """
    try:
        covid_data = covid19.get(data=True)
        country_data = covid_data.get(country, {})

        if not country_data:
            return f"No COVID-19 data available for {country}."

        stats = {
            'Country': country_data.get('Country', 'N/A'),
            'Confirmed Cases': country_data.get('Cases', 'N/A'),
            'Recovered': country_data.get('Recovered', 'N/A'),
            'Deaths': country_data.get('Deaths', 'N/A'),
            'Active Cases': country_data.get('Active', 'N/A'),
            'Last Update': country_data.get('Updated', 'N/A')
        }

        return stats

    except Exception as e:
        return f"Error fetching COVID-19 data: {str(e)}"

if __name__ == "__main__":
    # Get user input for the country
    country_input = input("Enter the country: ").strip()

    # Get COVID-19 statistics for the specified country
    country_stats = get_covid19_stats(country_input)

    # Display the statistics
    print("\nCOVID-19 Statistics:")
    for key, value in country_stats.items():
        print(f"{key}: {value}")
