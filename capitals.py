countries = input().split(", ")
capitals = input().split(", ")
final_information = {countries[index]: capitals[index] for index in range(len(capitals))}
for country, capitals in final_information.items():
    print(f"{country} -> {capital}")
