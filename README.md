Given an array of integers, nums,  return the maximum difference, nums[j] - nums[i], for all pairs nums[i] = nums[j] where i < j. Return -1 if there is not a pair that satisfies this condition.

 

For example, given the array nums = [7, 1, 2, 5], the largest difference is 5 - 1 = 4.

 

Function Description 

 

Complete the function maxDifference in the editor below. The function must return the maximum difference between two elements as described.

 

maxDifference has  the following parameters:

    nums: an array of integers. 

 

Constraints

1 = N = 105
-105 = nums[i] = 105
Input Format For Custom Testing
Locked stub code reads input from stdin and passes it to the function.

 

The first line contains an integer, n, denoting the number of elements in the array nums.

Each of the next n lines contains an integer, nums[i].

Sample Case 0
Sample Input For Custom Testing

7
2
3
10
2
4
8
1
Sample Output

8
Explanation

10 is the largest number in the array and 1 is the lowest number in the array. However, the index of 10 is lower than the lowest index that contains a 1 so the condition of the problem is not satisfied. Using zero-based index notation, the correct answer is a[2] - a[0] = 10 - 2 = 8, This satisfies the condition the larger number in the pair, should be positioned at a higher index in the array than 
