# There are two sorted arrays A and B of sizes N and M respectively.

# Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

# NOTE:

# The overall run time complexity should be O(log(m+n)).
# IF the number of elements in the merged array is even, then the median is the average of (n/2)th and (n/2+1)th element. For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5.


# Problem Constraints
# 1 <= N + M <= 2*106



# Input Format
# The first argument is an integer array A of size N.
# The second argument is an integer array B of size M.



# Output Format
# Return a decimal value denoting the median of two sorted arrays.



# Example Input
# Input 1:

#  A = [1, 4, 5]
#  B = [2, 3]
# Input 2:

#  A = [1, 2, 3]
#  B = [4]


# Example Output
# Output 1:

#  3.0
# Output 2:

#  2.5


# Example Explanation
# Explanation 1:

#  The median of both the sorted arrays will be 3.0.
# Explanation 2:

#  The median of both the sorted arrays will be (2+3)/2 = 2.5.

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, a,b):
        if len(a)>len(b):
            a,b=b,a
        n1=len(a)
        n2=len(b)
        left,right=0,n1
        while(left<=right):
            cut1=(left+right)//2
            cut2=(n1+n2)//2 -cut1
            l1=float('-inf') if cut1==0 else a[cut1-1]
            l2=float('-inf') if cut2==0 else b[cut2-1]
            r1=float('inf') if cut1==n1 else a[cut1]
            r2=float('inf') if cut2==n2 else b[cut2]

            if l1>r2:
                right=cut1-1
            elif l2>r1:
                left=cut1+1
            else:
                return (max(l1,l2)+min(r1,r2))/2 if (n1+n2)%2==0 else min(r1,r2)
#Time complexity - O(log(min(n1,n2)))
#Space complexity - O(1)