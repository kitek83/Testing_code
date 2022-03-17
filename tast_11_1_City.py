def city_functions(city_name,country_name,population=''):
    if population:
        formatted_name = f'{city_name},{country_name} - {population=}'
    else:
        formatted_name = f'{city_name},{country_name}'
    return formatted_name.title()
