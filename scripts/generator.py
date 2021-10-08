import os
import pandas as pd


def generate_txt(file_name, save_location, data_dict):
    try:
        with open(f"{os.path.join(save_location, file_name)}.txt", "x") as f:
            inf = [[key, data_dict[key]] for key in data_dict.keys()]
            inf_str = ""
            for coup in inf:
                inf_str += "\t: ".join(coup)
                inf_str += "\n"
            f.write(inf_str)
            return True
    except:
        return False

#default header
defaultHeader = ("Id", "Username", "E-mail", "App Name", "Password", "Creation date", "Category", "Save date", "Last update date", "Mobile number", "Password rate", "Note")

def generate_excel(file_name, save_location, lst_of_data_lst, header=defaultHeader):
    df = pd.DataFrame(lst_of_data_lst, columns=header)
    try:
        path = os.path.join(save_location, file_name)+".xlsx"
        #check file not exist
        if not os.path.exists(path):
            writer = pd.ExcelWriter(f"{path}", engine="xlsxwriter")
            df.to_excel(writer, index=False)
            writer.save()
            return True
        #file exist
        else:
            return False
    except:
        return False

def generate_csv(file_name, save_location, lst_of_data_lst, header=defaultHeader):
    try:
        with open(f"{os.path.join(save_location, file_name)}.csv", "x") as f:
            f.write(",".join(header))
            f.write("\n")
            for data_lst in lst_of_data_lst:
                f.write(",".join(map(str, data_lst)))
                f.write("\n")
            return True
    except Exception as e:
        print(e)
        return False