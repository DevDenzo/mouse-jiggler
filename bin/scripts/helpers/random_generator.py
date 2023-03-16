from random import randrange

class RandomGenerator():

    def generate_coordinates_by_screensize(self, screensize, quantity):

        generated_data = []

        for n in range(0, quantity):
            for screen in screensize:
                
                generated_data.append((randrange(0,screen[0]),randrange(0,screen[1])))

        return generated_data

