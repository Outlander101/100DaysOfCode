import os
import pandas

CENSUS_FILE_CSV = "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
PRIM_FUR_COLOR = "Primary Fur Color"

def squirrel_count(series, color):
    return len(series[series[PRIM_FUR_COLOR] == color])

def main():
    if os.path.isfile(CENSUS_FILE_CSV):
        census_data = pandas.read_csv(CENSUS_FILE_CSV)
        count_grey_squirrels = squirrel_count(census_data, "Gray")
        count_red_squirrels = squirrel_count(census_data, "Cinnamon")
        count_black_squirrels = squirrel_count(census_data, "Black")

        color_dict = {
            "Primary Fur Color": ["Grey", "Cinnamon", "Black"],
            "Count": [count_grey_squirrels, count_red_squirrels, count_black_squirrels]
        }

        df = pandas.DataFrame(color_dict)
        df.to_csv("./Primary_Fur_color.csv")

if __name__ == "__main__":
    main()
