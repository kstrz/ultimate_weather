import numpy as np
from scipy import stats


class Statistics:
    def __init__(self, service_temps, real_temps):
        service_temps_flat = service_temps.flatten()
        real_temps_flat = real_temps.flatten()
        self.diff_array = []
        for x in range(len(service_temps)):
            if service_temps_flat[x] != -300 and real_temps_flat[x] != -300:
                self.diff_array.append(abs(service_temps_flat[x] - real_temps_flat[x]))

    def count_service_correctness(self):
        values_sum = 0
        for diff in self.diff_array:
            if diff < 2:
                values_sum += 1
            elif diff < 4:
                values_sum += 0.5

        return round((values_sum / len(self.diff_array) * 100), 2)

    def count_avg_temp_diff(self):
        return np.average(self.diff_array)

    def count_std(self):
        return np.std(self.diff_array)

    def count_mode(self):
        return stats.mode(self.diff_array, axis=None)[0][0]

    def count_median(self):
        return np.median(self.diff_array)

    def are_statistics_available(self):
        return bool(len(self.diff_array))
