package algorithms;

// import java.lang.Math.*;

public class Knapsack {
	
	static int max(int a, int b) { return (a > b)? a : b; } 
	
	// returns maximum value that can be put in a knapsack of capacity W
	static int knapsack(int W, int wt[], int val[], int n)
	{
		// base case
		if (n==0 || W==0)
			return 0;
		
		// If weight of nth item is more than knapsack capacity W, then
		// this item cannot be included in optimal solution
		if (wt[n-1] > W)
			return knapsack(W, wt, val, n-1);
		
		// return maximum of two cases
		// nth item included
		// not included
		else return max(val[n-1] + knapsack(W-wt[n-1],wt,val,n-1),
				knapsack(W,wt,val,n-1)
				);
	}
	
	public static void main(String[] args) {
		int val[] = new int[]{60, 100, 120};
		int wt[] = new int[]{10, 20, 30};
		
		int W=50;
		int n=val.length;
		System.out.println(knapsack(W,wt,val,n));
	}

	}
