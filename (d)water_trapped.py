#I have referred this from google
#To calculate the amount of water that will be trapped on a roof structure, given an array of integers representing the elevation of the roof structure at various positions, you can use the following algorithm:

#Initialize two pointers left and right to the start and end of the array respectively.
#Initialize two variables left_max and right_max to 0.
#Initialize a variable water to 0.
#While left is less than or equal to right, do the following:
#If arr[left] is less than or equal to arr[right], do the following:
#If arr[left] is greater than left_max, set left_max to arr[left].
#Otherwise, increment water by left_max - arr[left].
#Increment left by 1.
#Otherwise, do the following:
#If arr[right] is greater than right_max, set right_max to arr[right].
#Otherwise, increment water by right_max - arr[right].
#Decrement right by 1.
#Return water.



def maxWater(arr, n):
    # To store the maximum water that can be stored
    res = 0

    # For every element of the array
    for i in range(1, n - 1):

        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # Find the maximum element on its right
        right = arr[i]
        for j in range(i + 1, n):
            right = max(right, arr[j])

        # Update the maximum water
        res = res + (min(left, right) - arr[i])

    return res

# Driver code
if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    n = len(arr)

    print(maxWater(arr, n))
