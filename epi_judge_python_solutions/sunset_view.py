import unittest

def examine_buildings_with_sunset(sequence):
    current_max = sequence[0]
    current_count = 1
    for i in range(1, len(sequence)):
        if sequence[i] > current_max:
            current_max = sequence[i]
            current_count += 1
    return current_count

class TestSunset(unittest.TestCase):

    def test_case_1(self):
        skyline = [1,2,3,4,5]
        result = examine_buildings_with_sunset(skyline)
        self.assertEqual(result, 5)

    def test_case_2(self):
        skyline = [5,4,3,2,1]
        result = examine_buildings_with_sunset(skyline)
        self.assertEqual(result, 1)

    def test_case_3(self):
        skyline = [2,1,3,2,5]
        result = examine_buildings_with_sunset(skyline)
        self.assertEqual(result, 3)

    def test_case_4(self):
        skyline = [1,3,5,7,2,4]
        result = examine_buildings_with_sunset(skyline)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
