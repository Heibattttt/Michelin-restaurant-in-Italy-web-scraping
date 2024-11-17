import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML

def Advanced_Search_Engine(dataframe):
    """
    Creates an interactive search interface for filtering restaurant data.

    Args:
        dataframe (pandas.DataFrame): DataFrame containing restaurant information
        Required columns: restaurantName, region, city, priceRange, cuisineType, creditCards, facilitiesServices, website, address
        Optional columns: phonenumber, description

    Output:
           The function returns as output a table in HTML format with the restaurants that match the criteria selected in input by the user. 
           The table will contain the name of the restaurant, the city, the address, website, the type of cuisine, accepted cards and available services.
    """

    # Initialize UI styling for the user interface 
    display(HTML('''
        <style>
        .widget-dropdown {
            width: 200px !important;
        }
        .button-primary {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 3px;
        }
        .restaurant-table {
            width: 100% !important; /* Increase table width to take full available space */
        }
        </style>'''))

    def optimize_dataframe(df):
        """Optimize DataFrame for filtering operations."""
        df = df.copy(deep=True)

        # Normalize string columns for consistent comparison
        for col in ['region', 'city']:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip().str.capitalize()

        # Map price range to categorical values for logical indexing
        price_mapping = {
            'Economic': 0,
            'Affordable': 1,
            'Expensive': 2,
            'Luxury': 3
        }
        
        df['priceRange'] = pd.Categorical(
            df['priceRange'],
            categories=list(price_mapping.keys()),
            ordered=True)
        
        df['priceRange2'] = df['priceRange'].map(price_mapping)
        
        return df

    def get_unique_list_values(column):
        """Extract unique values from comma-separated strings or lists."""
        if column not in dataframe.columns:
            return []
        
        unique_vals = set()
        series = dataframe[column].dropna()
        
        for value in series:
            if isinstance(value, str):
                items = [item.strip() for item in value.split(',')]
                unique_vals.update(filter(None, items))
            elif isinstance(value, list):
                unique_vals.update(filter(None, value))
                
        return sorted(list(unique_vals))

    def is_valid_city(city):
        """Validate city name to ensure it contains no numbers."""
        if not isinstance(city, str):
            return False
        city = city.strip()
        return city.isalpha()

    # Initialize dataframe and extract unique values
    df = optimize_dataframe(dataframe)
    try:
        unique_regions = sorted(df['region'].dropna().unique())
        unique_cards = get_unique_list_values('creditCards')
        unique_services = get_unique_list_values('facilitiesServices')
    except Exception as e:
        print(f"Error getting unique values: {str(e)}")
        unique_regions, unique_cards, unique_services = [], [], []

    # Create interface widgets
    region_dropdown = widgets.Dropdown(
        options=[''] + unique_regions,
        description='Region:',
        style={'description_width': 'initial'})

    city_dropdown = widgets.Dropdown(
        options=[],
        description='City:',
        style={'description_width': 'initial'})

    price_options = ['', 'Economic', 'Affordable', 'Expensive', 'Luxury']
    
    min_price_dropdown = widgets.Dropdown(
        options=price_options,
        description='Min Price:',
        style={'description_width': 'initial'})

    max_price_dropdown = widgets.Dropdown(
        options=price_options,
        description='Max Price:',
        style={'description_width': 'initial'})

    card_checkboxes = [widgets.Checkbox(value=False, description=card) for card in unique_cards]

    service_checkboxes = [widgets.Checkbox(value=False, description=service) for service in unique_services]

    cuisine_box = widgets.VBox([])
    output_area = widgets.Output()

    def update_cities(change):
        """Update available cities based on selected region and filter out invalid city names."""
        selected_region = change['new']
        if selected_region:
            city_mask = df['region'] == selected_region
            unique_cities = sorted(df.loc[city_mask, 'city'].unique())
            valid_cities = [city for city in unique_cities if pd.notna(city) and is_valid_city(city)]
            city_dropdown.options = [''] + valid_cities
        else:
            city_dropdown.options = []
        city_dropdown.value = ''
        update_cuisines({'new': ''})

    def update_cuisines(change):
        """Update available cuisines based on selected city."""
        selected_city = change['new']
        cuisine_box.children = []

        if selected_city and 'cuisineType' in df.columns:
            city_data = df.loc[df['city'] == selected_city].copy()

            if not city_data.empty:
                cuisines = set()
                for cuisine_list in city_data['cuisineType'].dropna():
                    if isinstance(cuisine_list, str):
                        cuisines.update(c.strip() for c in cuisine_list.split(',') if c.strip())

                if cuisines:
                    cuisine_box.children = [widgets.Checkbox(value=False, description=cuisine) for cuisine in sorted(cuisines)]

    def apply_filters():
        """Apply all selected filters and return filtered DataFrame."""
        filtered_df = df.copy()
        mask = pd.Series(True, index=filtered_df.index)
    
        # Filter by region
        if region_dropdown.value:
            mask &= (filtered_df['region'] == region_dropdown.value)
    
        # Filter by city
        if city_dropdown.value:
            mask &= (filtered_df['city'] == city_dropdown.value)
    
        # Filter by selected cuisines
        selected_cuisines = [cb.description for cb in cuisine_box.children if cb.value]
        if selected_cuisines:
            cuisine_mask = df['cuisineType'].apply(lambda x: all(cuisine in str(x) for cuisine in selected_cuisines) if pd.notna(x) else False)
            mask &= cuisine_mask
    
        # Filter by price range
        if min_price_dropdown.value:
            min_idx = price_options.index(min_price_dropdown.value) - 1
            if min_idx >= 0:
                mask &= (filtered_df['priceRange2'] >= min_idx)
        if max_price_dropdown.value:
            max_idx = price_options.index(max_price_dropdown.value) - 1
            if max_idx >= 0:
                mask &= (filtered_df['priceRange2'] <= max_idx)
    
        # Filter by selected credit cards
        selected_cards = [cb.description for cb in card_checkboxes if cb.value]
        if selected_cards:
            card_mask = filtered_df['creditCards'].apply(
                lambda x: isinstance(x, list) and all(card in x for card in selected_cards))
            mask &= card_mask

        # Filter by selected services
        selected_services = [cb.description for cb in service_checkboxes if cb.value]
        if selected_services:
            service_mask = filtered_df['facilitiesServices'].apply(
                lambda x: isinstance(x, list) and all(service in x for service in selected_services))
            mask &= service_mask
    
        return filtered_df.loc[mask]

    def show_selection(button):
        """Display filtered results showing only essential restaurant information."""
        with output_area:
            clear_output(wait=True)
            try:
                filtered_data = apply_filters()

                if filtered_data.empty:
                    print("No restaurants match the selected criteria.")
                else:
                    display_data = filtered_data[['restaurantName', 'address', 'city', 'website',"cuisineType","creditCards","facilitiesServices"]].copy()

                    if 'website' in display_data.columns:
                        display_data['website'] = display_data['website'].apply(
                            lambda x: f'<a href="{x}" target="_blank">{x}</a>' if pd.notna(x) else '')

                    display_data.columns = ['Restaurant Name', 'Address', 'City', 'Website',"cuisineType","creditCards","Services"]

                    print(f"Found {len(display_data)} matching restaurants:")
                    display(HTML(display_data.to_html(
                        escape=False,
                        classes='restaurant-table',
                        index=False
                    )))
                    display_data.to_csv('filtered_results.csv', index=False)
                
                    # HTML
                    with open('filtered_results.html', 'w') as f:
                        f.write(display_data.to_html(escape=False, index=False))
                    print("Results have been saved to 'filtered_results.csv' and 'filtered_results.html'.")

            except KeyError as ke:
                print(f"Missing required column in data: {ke}")
            except Exception as e:
                print(f"Error displaying results: {str(e)}")

    def reset_selection(button):
        """Reset all filters to default values."""
        region_dropdown.value = ''
        city_dropdown.value = ''
        min_price_dropdown.value = ''
        max_price_dropdown.value = ''
        for cb in card_checkboxes + list(cuisine_box.children) + service_checkboxes:
            cb.value = False
        with output_area:
            clear_output()
            print("Filters reset.")

    # Set up widget observers
    region_dropdown.observe(update_cities, names='value')
    city_dropdown.observe(update_cuisines, names='value')

    # Create interface buttons
    submit_button = widgets.Button(
        description="Apply Filters",
        button_style='primary',
        icon='search')
    
    submit_button.add_class('button-primary')
    submit_button.on_click(show_selection)

    reset_button = widgets.Button(
        description="Reset",
        button_style='warning',
        icon='refresh')
    
    reset_button.on_click(reset_selection)

    # Create layout
    filter_sections = [
        widgets.VBox([
            widgets.HTML("<h3>Location</h3>"),
            region_dropdown,
            city_dropdown
        ], layout=widgets.Layout(margin='10px')),
        widgets.VBox([
            widgets.HTML("<h3>Price Range</h3>"),
            min_price_dropdown,
            max_price_dropdown
        ], layout=widgets.Layout(margin='10px'))]

    if 'cuisineType' in df.columns:
        filter_sections.append(widgets.VBox([
            widgets.HTML("<h3>Cuisines</h3>"),
            cuisine_box
        ], layout=widgets.Layout(margin='10px')))

    if card_checkboxes:
        filter_sections.append(widgets.VBox([
            widgets.HTML("<h3>Accepted Cards</h3>"),
            widgets.VBox(card_checkboxes)
        ], layout=widgets.Layout(margin='10px')))

    if service_checkboxes:
        filter_sections.append(widgets.VBox([
            widgets.HTML("<h3>Facilities/Services</h3>"),
            widgets.VBox(service_checkboxes)
        ], layout=widgets.Layout(margin='10px')))

    # Display final layout
    display(widgets.VBox([
        widgets.HBox(filter_sections, layout=widgets.Layout(flex_wrap='wrap')),
        widgets.HBox([submit_button, reset_button], layout=widgets.Layout(margin='10px')),
        output_area]))