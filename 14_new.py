# Scatter Plot
# Steps involved in data visualization
# Step.1: import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# set a theme
sns.set_theme(style="ticks",color_codes=True)

# Import Data set OR You can import your own data
titanic=sns.load_dataset("titanic")

# Plot basic Graph
print(titanic)

# g=sns.FacetGrid(titanic, row="sex", hue="alone")
# g=(g.map(plt.scatter,"age", "fare").add_legend())
# plt.show()
