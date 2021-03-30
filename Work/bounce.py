# bounce.py
#
# Exercise 1.5

def get_new_height(height):
    return height * 3 / 5.0

start_height = 100.0
end_height = 0.0
height = start_height
no_of_iterations = 10
for i in range(no_of_iterations):
    height = get_new_height(height)
    print(i+1, round(height,4))