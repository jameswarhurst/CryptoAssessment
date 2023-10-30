# Define the size of the table
table_size = 10

# Create a 2D list for the table
table = []

# Create the x-axis values "1 2 0 1 2 0 1 2 0 1 2"
x_axis = "123456789"

# Fill in the table with the modulo results
for i in range(1, table_size + 1):
    row = [x_axis[(i+j-2) % len(x_axis)] for j in range(1, table_size + 1)]
    table.append([str(i)] + row)

# Calculate the maximum length of any element in the table
max_length = len(str(table_size))

# Display the table
for row in table:
    for item in row:
        print(item.rjust(max_length + 1), end="")
    print()
