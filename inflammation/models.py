"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single
    patient across all days).

    :returns: An array of mean values of measurements for each day.
   """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across
    all days).

    :returns: An array of max values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.
    
    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across
    all days).

    :returns: An array of minimum values of measurements for each day.
    """
    return np.min(data, axis=0)

def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative.')

    max_data = np.max(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    #print(normalised)
    return normalised

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Doctor(Person):
    def __init__(self, name, patients=None, hospital=None):
        super().__init__(name)

        if patients is None:
            self.patients = []
        else:
            self.patients = patients

        self.hospital = hospital
    def add_patient(self, patient):
        self.patients.append(patient)

    def add_hospital(self, hospital):
        """Add the hospital where the dr is working"""
        self.hospital = hospital

    def __str__(self):
        return self.name


class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if (other.day == self.day) and (other.value == self.value):
            return True
        else:
            return False

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name, observations=None):
        super().__init__(name)

        if observations is None:
            self.observations = []
        else:
            self.observations = observations

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation

    def __eq__(self, other):
        if self.name == other.name:
            for obs_new, obs in zip(other.observations, self.observations):
                if obs_new != obs:
                    return False
            return True
        else:
            return False


if __name__ == '__main__':
    alice = Patient('Alice')
    print(alice)

    obs = alice.add_observation(3)
    print(obs)

    bob = Person('Bob')
    print(bob)

