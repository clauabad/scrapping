from datetime import datetime

def transform_date(date_str):
    try:
        # Remove extra spaces
        date_str = ' '.join(date_str.split())
        # Replace periods in time format (e.g., 'p.m.' to 'PM')
        date_str = date_str.replace('a.m.', 'AM').replace('p.m.', 'PM').replace('a.m', 'AM').replace('p.m', 'PM')
        # Append the current year since it's missing in the date_str
        current_year = datetime.now().year
        date_str_with_year = f"{date_str} {current_year}"
        # Parse the date string
        date_obj = datetime.strptime(date_str_with_year, '%B %d, at %I:%M %p %Y')
        transformed_date = date_obj.strftime('%Y-%m-%d %H:%M')
        return transformed_date
    except ValueError as e:
        print(f"Error transforming date: {e}")
        return 'N/A'