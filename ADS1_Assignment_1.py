# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:35:22 2023

@author: aishw
"""

import pandas as pd
import matplotlib.pyplot as plt

#Visualisation 1 (Line Plot): Seasonal rainfall in UK from 2000 to 2022/ 
#Max and Min seasonal rainfall in UK from 2000 to 2022. 

def read_and_process_data(file_path):
    # Read file into dataframe
    df_UK = pd.read_excel(file_path)
    
    # Filter data for the years 2000-2022
    df_seasonal = pd.DataFrame(df_UK[(df_UK["year"] >= 2000) & (df_UK["year"] <= 2022)],
                                columns=["year", "win", "spr", "sum", "aut"])
    
    # Calculate max and min rainfall during the seasons over the years (2000-2022)
    df_seasonal["max"] = df_seasonal[["win", "spr", "sum", "aut"]].max(axis=1)
    df_seasonal["min"] = df_seasonal[["win", "spr", "sum", "aut"]].min(axis=1)
    
    # Rename the columns
    df_seasonal.rename(columns={"year": "Year",
                                "win": "Winter",
                                "spr": "Spring",
                                "sum": "Summer",
                                "aut": "Autumn",
                                "max": "Maximum_rainfall",
                                "min": "Minimum_rainfall"}, inplace=True)
    
    return df_seasonal

def plot_max_min_rainfall(df_seasonal):
    # Line plots
    plt.figure(figsize=(30, 8))

    # Plot the max and min rainfall during seasons with labels and customizing visualization
    plt.subplot(1, 2, 1)
    plt.plot(df_seasonal["Year"], df_seasonal["Maximum_rainfall"], marker="o", 
             label="Maximum rainfall", color="green")
    plt.plot(df_seasonal["Year"], df_seasonal["Minimum_rainfall"], marker="o", 
             label="Minimum rainfall", color="red")

    # Set title & labels and show the legend for lineplot1
    plt.legend(title="Max and Min rainfall", borderpad=0.5, fontsize=9)
    plt.title("Max and Min seasonal rainfall in UK")
    plt.xlabel("Years")
    plt.ylabel("Rainfall precipitation in millimetres (mm)")
    plt.xticks(df_seasonal["Year"])

def plot_seasonal_rainfall(df_seasonal):
    # Plot the four seasons with labels and customizing visualization
    plt.subplot(1, 2, 2)
    plt.plot(df_seasonal["Year"], df_seasonal["Winter"], 
             label="winter", color="green")
    plt.plot(df_seasonal["Year"], df_seasonal["Spring"], 
             label="spring", color="red")
    plt.plot(df_seasonal["Year"], df_seasonal["Summer"], 
             label="summer", color="orange")
    plt.plot(df_seasonal["Year"], df_seasonal["Autumn"], 
             label="autumn", color="brown")

    # Set title & labels and show the legend for lineplot2
    plt.legend(title="Seasonal Rainfall", borderpad=0.5, fontsize=9)
    plt.title("Seasonal rainfall in UK")
    plt.xlabel("Years")
    plt.ylabel("Rainfall precipitation in millimetres (mm)")
    plt.xticks(df_seasonal["Year"])

    # Save as png
    plt.savefig("UK_seasonal_rainfall.png")

    # Show the plot
    plt.show()

# Main program:
file_path = "UK_rainfall.xlsx"
df_seasonal_data = read_and_process_data(file_path)
print(df_seasonal_data)
plot_max_min_rainfall(df_seasonal_data)
plot_seasonal_rainfall(df_seasonal_data)


#Visualisation 2(Pie chart): Ethnicity Percentage of Asians in England and Wales Regions

def read_and_print_data(file_path):
    # Read file into dataframe
    df_diversity = pd.read_csv(file_path)
    print(df_diversity)

def plot_ethnicity_percentage(df_diversity, ethnicity="Asian"):
    # Filter data based on ethnicity
    df_ethnicity = pd.DataFrame(df_diversity[df_diversity["Ethnicity"] == ethnicity], 
                                columns=["Ethnicity", 
                                         "Region", 
                                         "percentage of ethnic group"])
    print(df_ethnicity)
    
    # Extract region and percentage of ethnic group
    region = df_ethnicity["Region"] 
    per_ethnic = df_ethnicity["percentage of ethnic group"]
    
    # Pie Plot
    plt.figure(figsize=(40, 20))
    explode = (0,) * len(region)  # Set explode values
    plt.pie(per_ethnic, explode=explode, labels=region, startangle=45, autopct='%1.1f%%')

    # Set title and show the legend
    plt.legend(region, title="Region", borderpad=1, fontsize=11)
    plt.title(f"Ethnicity Percentage of {ethnicity}s in England and Wales Regions", 
              fontsize=25)

    # Save as png
    plt.savefig(f"Ethnicity_Percentage_{ethnicity}.png")

    # Show the plot
    plt.show()

# Main program:
file_path = "Diversity.csv"
read_and_print_data(file_path)
plot_ethnicity_percentage(pd.read_csv(file_path), ethnicity="Asian")


#Visualisation 3 (Bar chart): Average rainfall per year (2000 – 2022) 

def read_and_process_data(file_path, start_year, end_year):
    # Read file into dataframe
    df_UK = pd.read_excel(file_path)
    
    # Filter data for the specified years
    df_yearly = pd.DataFrame(df_UK[(df_UK["year"] >= start_year) & (df_UK["year"] <= end_year)],
                             columns=["year", "jan", "feb", 
                                      "mar", "apr", "may", 
                                      "jun", "jul", "aug", 
                                      "sep", "oct", "nov", "dec"])
    
    # Calculate average precipitation per year
    df_yearly["Average"] = df_yearly[["jan", "feb", "mar", 
                                      "apr", "may", "jun", 
                                      "jul", "aug", "sep", 
                                      "oct", "nov", "dec"]].mean(axis=1)
    
    # Rename the columns
    df_yearly.rename(columns={"year": "Year",
                              "jan": "January",
                              "feb": "February",
                              "mar": "March",
                              "apr": "April",
                              "may": "May",
                              "jun": "June",
                              "jul": "July",
                              "aug": "August",
                              "sep": "September",
                              "oct": "October",
                              "nov": "November",
                              "dec": "December",
                              "Average": "Average"}, inplace=True)
    
    return df_yearly

def plot_average_rainfall(df_yearly):
    # Bar Plot
    plt.figure(figsize=(20, 8))
    plt.bar(df_yearly["Year"], df_yearly["Average"])

    # Set title
    plt.title("Average precipitation of rainfall per years (2000 - 2022)", 
              fontweight='bold', fontsize=10)

    # Set labels and legend
    plt.xlabel("Years (2000-2022)", fontweight='bold', fontsize=13) 
    plt.ylabel("Rainfall precipitation (mm)", fontweight='bold', fontsize=13)
    plt.xticks(df_yearly["Year"])
    plt.legend(df_yearly["Year"], title="Max Average rainfall", borderpad=1, fontsize=11)
    

    # Save as png
    plt.savefig("Average_rainfall_per_year.png")

    # Show the plot
    plt.show()

# Main program
file_path = "UK_rainfall.xlsx"
start_year = 2000
end_year = 2022

df_yearly_data = read_and_process_data(file_path, start_year, end_year)
print(df_yearly_data)
plot_average_rainfall(df_yearly_data)

