from gaussian_class import Gaussian


gaussian_one = Gaussian()
gaussian_one.read_data_file('test.txt', True)
print(gaussian_one.mean())
print(gaussian_one.stdev())