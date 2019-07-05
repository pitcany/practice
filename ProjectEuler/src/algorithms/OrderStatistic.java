package algorithms;

//import java.lang.Math.*;

public class OrderStatistic {
	
	public static double findMedianSortedArrays(int A[], int B[]) {
		int m = A.length;
		int n = B.length;

		if ((m + n) % 2 != 0) // odd
			return (double) findKth(A,0, m - 1, B, 0, n - 1, (m + n) / 2);
		else { // even
			return (findKth(A, 0, m - 1, B, 0, n - 1, (m + n) / 2) 
				+ findKth(A, 0, m - 1, B, 0, n - 1, (m + n) / 2 - 1)) * 0.5;
		}
	}

	public static int findKth(int A[], int p1, int r1, int B[], int p2, int r2, int k) {
		int n1 = r1-p1+1;
		int n2 = r2-p2+1;
		
		//base cases
		if(n1 == 0){
			return B[p2+k];
		}
		if(n2 == 0){
			return A[p1+k];
		}
		//
		if(k == 0){
			return Math.min(A[p1], B[p2]);
		}
		
		//select two index i,j from A and B respectively such that If A[i] is between B[j] and B[j-1] 
		//Then A[i] would be the i+j+1 smallest element because.
		//Therefore, if we choose i and j such that i+j = k-1, we are able to find the k-th smallest element.
		int i = n1/(n1+n2)*k;//let's try to chose a middle element close to kth element in A 
		int j = k-1 -i;
		
		//add the offset
		int mid1 = Math.min(p1+i, r1);
		int mid2 = Math.min(p2+j, r2);
		
		//mid1 is greater than mid2. So, median is either in A[p1...mid1] or in B[mid2+1...r2].
		//we have already see B[p2..mid2] elements smaller than kth smallest
		if(A[mid1] > B[mid2]){
			k = k - (mid2-p2+1);
			r1 = mid1;
			p2 = mid2+1;
		}
		//mid2 is greater than or equal mid1. So, median is either in A[mid1+1...r1] or in B[p2...mid2].
		//we have already see A[p1..mid1] elements smaller than kth smallest
		else{
			k = k - (mid1-p1+1);
			p1 = mid1+1;
			r2 = mid2;
		}
		
		return findKth(A, p1, r1, B, p2, r2, k);
	}

	public static void main(String[] args) {
		int A[] = new int[]{60, 100, 120};
		int B[] = new int[]{10, 20, 30};
		
		System.out.println(findMedianSortedArrays(A,B));

	}

}