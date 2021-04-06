import matplotlib.pyplot as plt

# Create some data
x = range(0,50)
y = range(50,100)

# Make plot and save it
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(x,y) # Plot the data
ax.set_title('I made this with a script')
fig.savefig('My_plot_with_script.png', bbox_inches='tight') # save it
