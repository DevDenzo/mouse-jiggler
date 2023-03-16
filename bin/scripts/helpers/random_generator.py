class RandomGenerator():

    def init(self, data_type, data):
        self.data_type = data_type
        self.data = data

    def generate_coordinates(self):
        if self.data_type == "LIST":

            for item in self.data:

                if len(item) == 2:



