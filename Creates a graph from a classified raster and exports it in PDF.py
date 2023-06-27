import matplotlib.pyplot as plt
import numpy as np
import rasterio

# Specify the path to your raster layer
raster_path = "C:/Users/gis/Desktop/Raster/Windfarm_Location_Raster_Suitiability.tif"

# Define the class labels and ranges
class_labels = ["Inconvenient", "Poorly suited", "Suitable"]
class_ranges = [(0, 55), (56, 110), (111, 165)]
class_colors = ["red", "yellow", "blue"]

# Open the raster layer
with rasterio.open(raster_path) as src:
    # Read the raster data
    raster_data = src.read(1)

    # Calculate the histogram of raster values within the valid class ranges
    histogram = np.histogram(raster_data, bins=np.arange(0, np.max(raster_data) + 2), range=(0, np.max(raster_data) + 1))

    # Get the bin edges and counts
    bin_edges = histogram[1]
    bin_counts = histogram[0]

    # Calculate the total number of pixels within the valid class ranges
    total_pixels = bin_counts[class_ranges[0][0]:class_ranges[-1][1]+1].sum()

    # Calculate the class percentages
    class_percentages = []

    for class_range in class_ranges:
        class_start, class_end = class_range
        range_counts = bin_counts[class_start:class_end+1]
        class_percentage = (range_counts.sum() / total_pixels) * 100
        class_percentages.append(class_percentage)

# Manually rearrange the class percentages
class_percentages = [class_percentages[2], class_percentages[0], class_percentages[1]]

# Generate class indices for the bar plot
class_indices = range(len(class_labels))

# Create a vertical bar plot to visualize the class percentages with assigned colors
plt.bar(class_indices, class_percentages, color=class_colors)
plt.xlabel('Class')
plt.ylabel('Percentage')
plt.title('Class Percentage in Raster')
plt.xticks(class_indices, class_labels)

# Save the plot as a PDF file
plt.savefig('graph_without_map_background.pdf')

plt.show()















