import numpy as np
from scipy import stats

class Statistics:
    def __init__(self, service_temps, real_temps):
        self.diff_array = np.array([x for x in abs(service_temps - real_temps).flatten() if x < 200])


    def count_service_correctness(self):
        values_sum = 0
        for diff in self.diff_array:
            if diff < 2:
                values_sum += 1
            elif diff < 4:
                values_sum += 0.5

        return (values_sum / len(self.diff_array) * 100)


    def count_avg_temp_diff(self):
        return np.average(self.diff_array)


    def count_std(self):
        return np.std(self.diff_array)


    def count_mode(self):
        return stats.mode(self.diff_array, axis=None)[0][0]


    def count_median(self):
        return np.median(self.diff_array)