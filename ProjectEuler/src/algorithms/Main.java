package algorithms;

// import java.util.Scanner;
public class Main {
//	private static Scanner s;
	
	public static void printTable(int start, int end, int step) {
		int currentVal = start;
		while (currentVal <= end){
			int convertedVal = (int)((5.0/9)*(currentVal - 32));
			System.out.println(currentVal + "\t" + convertedVal);
			currentVal += step;
		}
	}

	static boolean CheckFib(int n)
	{
		int a = 0;
		int b = 1;
		int c;
		while (a < n){
			c = a+b;
			a = b;
			b = c;
		}
		if (a==n){
			return true;
		} else {
			return false;
		}
	}
	
	public static void tripleSum(int[] input, int x) {
		int[] ordered = new int[3];
		for (int i = 0; i < input.length; i++) {
			for (int j = i+1; j < input.length; j++) {
				for (int k = j+1; k < input.length; k++) {
					if (input[i]+input[j]+input[k] == x) {
						ordered = ordering(input[i],input[j],input[k]);
						System.out.println(ordered[0] + " " + ordered[1] + " " + ordered[2]);
					}
				}
			}
		}
	}

	public static int[] ordering(int a, int b, int c) {
		int[] res = new int[3];
		res[0]=Math.min(Math.min(a, b), c);
		res[2]=Math.max(Math.max(a, b), c);
		res[1]=a+b+c-res[0]-res[2];
		return res;
	}

	
	static int[] arrange(int n) {
		int[] arr = new int[n];
		int midpt = (n+1)/2;
		for (int i=1; i<=midpt; i++) {
			arr[i-1]=2*i-1;
		}
		int b;
		if (n%2==0) {
			b = n;
		} else {
			b = n-1;
		}
		for (int i=1; i<=n/2; i++) {
			arr[midpt+i-1]=b-2*(i-1);
		}
		return arr;
	}
	
    static int findDuplicate(int arr[]) {
	    for (int i=0; i < arr.length; i++) {
		    int j;
		    for (j = i+1; j < arr.length; j++) {
		    	if (arr[i]==arr[j]) {
		    		return arr[i];
		    	}
		    }
	    }
        return -1;
    }
	
	static int find(int[] arr, int x) {
		for (int i=0; i<arr.length; i++){
			if (arr[i]==x) {
				return i;
			}
		}
		return -1;
	}
	
	public static void main(String[] args) {
		// s = new Scanner(System.in);
        // int num = s.nextInt();
		int arr[] = {3,1,4,2,5,9,9};
		tripleSum(arr, 8);
	    // System.out.println(findDuplicate(arr));
		// int[] arr = arrange(6);
		// for (int i = 0; i<arr.length; i++) {
		// 	System.out.print(arr[i] + " ");
		// }
        // printTable(0,100,20);
        // System.out.println(CheckFib(num));
	}
}