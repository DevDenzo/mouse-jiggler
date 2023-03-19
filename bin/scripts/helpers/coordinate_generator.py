from random import randrange

class CoordinateGenerator():

    def find_maximum_horizontal_and_minimum_vertical(self, screensize):

        #Figure out the maximum horizontal as horizontal coordinates will add
        #Figure out the smallest screen vertical so we remain within that limit for all movement
        maximum_horizontal = 0
        minimum_vertical = screensize[0][1]

        for screen in screensize:
            #Add the horizontal coordinates for all screens
            maximum_horizontal = screen[0] + maximum_horizontal

            #Find the smallest screens vertical
            if screen[1] < minimum_vertical:
                minimum_vertical = screen[1]

        return (maximum_horizontal, minimum_vertical)


    def generate_random_coordinates_by_screensize(self, screensize, quantity):

        generated_data = []
        
        coordinates = self.find_maximum_horizontal_and_minimum_vertical(screensize)
        maximum_horizontal = coordinates[0]
        minimum_vertical = coordinates[1]

        for n in range(0, quantity):
            for screen in screensize:
                
                generated_data.append((randrange(0, maximum_horizontal), randrange(0, minimum_vertical)))

        return generated_data
    
    def generate_zig_zag_coordinates_by_screensize(self, screensize, quantity):

        generated_data = []


        coordinates = self.find_maximum_horizontal_and_minimum_vertical(screensize)
        maximum_horizontal = coordinates[0]
        minimum_vertical = coordinates[1]

        start_coordinate = (maximum_horizontal / 20, minimum_vertical / 8)
        first_peak_coordinate = ((maximum_horizontal / 20) * 3.25, (minimum_vertical / 8) * 7)

        first_line = []
        first_line.append(start_coordinate)
        for n in range(0, quantity):
            change_in_x = (first_peak_coordinate[0]-start_coordinate[0]) / quantity
            change_in_y = (first_peak_coordinate[1]-start_coordinate[1]) / quantity
            next_coordinate = ( change_in_x * (n+1) + start_coordinate[0], change_in_y * (n+1) + start_coordinate[1])
            first_line.append(next_coordinate)

        second_line = []
        #Use the first line and plot the reverse line
        for n in range(0, quantity):
            change_in_x = first_line[1][0] - first_line[0][0]
            change_in_y = first_line[1][1] - first_line[0][1]
            next_coordinate = (first_line[-1][0] + (change_in_x*(n+1)), first_line[-1][1] - (change_in_y*(n+1)))
            second_line.append(next_coordinate)

        first_spike = first_line + second_line

        second_spike = []
        third_spike = []
        fourth_spike = []

        for n in range(0, len(first_spike)):
            change_in_x = first_spike[-1][0]-first_spike[0][0]
            second_spike_coord = (first_spike[n][0] + change_in_x, first_spike[n][1])
            third_spike_coord = (second_spike_coord[0] + change_in_x, second_spike_coord[1])
            fourth_spike_coord = (third_spike_coord[0] + change_in_x, third_spike_coord[1])

            second_spike.append(second_spike_coord)
            third_spike.append(third_spike_coord)
            fourth_spike.append(fourth_spike_coord)

        generated_data = first_spike + second_spike + third_spike + fourth_spike
        
        return generated_data

def generate_coordinates_on_line(self, coordinate_start, coordinate_end, number_of_points):
    generated_data = []

    #Using Y=MX+C find the gradient of the line, divide it by number of points. Keep adding the dy/dx and append each coordinate.
    return generated_data