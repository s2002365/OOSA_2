import numpy as np

class sortArray(object):
    def __init__(self,arr):
        self.array = arr

    def sort_array(self):

        '''This function loops through the random array, comparing the values at index [i] and index [i+j]. If the value at i is smaller than i+j, then a temporary variable is used to store the value at i, the smaller value in [i=j] is moved to index [i] and the temp variable replaces the value at index [i+j]. By using nested loops this sorts the entire array into ascending order.'''

        for i in range(0, len(self.array)):
            for j in range(0, len(self.array[i:])):
                temp = 0
                if self.array[i] > self.array[j+i]:
                    temp = self.array[i]
                    self.array[i] = self.array[j+i]
                    self.array[j+i] = temp


if __name__ == '__main__':

    '''if this script is run, this tests whether it is working. Creates a random array of 100 values (x) and then uses that to create an instance of the class (y), which is then sorted using the sort_array() method. '''
    x=np.random.random(100)
    y=sortArray(x) #creates an instance of this class
    y.sort_array() #runs the sort algorithm, and overwrites the self.array (already stored as y, simply adjusting the values inside y)
    print(y.array) #prints the sorted array
