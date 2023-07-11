import re
import csv
import os

def get_province_lists(mod_directory):
    map_folder = os.path.join(mod_directory, 'map')
    provinces_folder = os.path.join(mod_directory, 'history' , 'provinces')
    province_list = []

    for folder_name in os.listdir(provinces_folder):
        folder_path = os.path.join(provinces_folder, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.txt'):
                    try:
                        if ' - ' in file_name:
                            province_id, province_name = file_name.split(' - ')
                        else:
                            province_id, province_name = file_name.split(None, 1)  # Split on first whitespace
                        province_id = int(province_id.strip())
                        province_name = province_name.strip('.txt')
                        province_dict = {'prov_id': province_id, 'prov_name': province_name}
                        province_list.append(province_dict)
                    except ValueError:
                        print(f"Ignoring file with unexpected name format: {file_name}")
    
    province_list_sorted = sorted(province_list, key=lambda x: x['prov_id'])

    return province_list_sorted

def get_state_list(mod_directory):
    region_file = os.path.join(mod_directory, "map", "region.txt")
    STATE_EXTRACT_REGEX = r"= {\s*(.*?)\s*} #(.*)"
    state_list = []

    with open(region_file, mode="r+", encoding='latin-1') as file:
        for line in file:
            match = re.search(STATE_EXTRACT_REGEX, line)
            if match:
                numbers = match.group(1).split()
                state = match.group(2).strip()
                for number in numbers:
                    state_list.append([number, state])
    
    return state_list

def generate_states_and_provinces(mod_directory):
    try:
        province_list_sorted = get_province_lists(mod_directory)
        state_list = get_state_list(mod_directory)

        with open('listofprovinces.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['prov_id', 'prov_name'])
            writer.writeheader()
            writer.writerows(province_list_sorted)

        with open("listofstates.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Number", "State"])
            writer.writeheader()
            writer.writerows(state_list)

        print(f"States list has been saved to {output_file}")
    except Exception as e:
        print("States and provinces list csvs was not able to be written")
        print("An error occurred:", str(e))
