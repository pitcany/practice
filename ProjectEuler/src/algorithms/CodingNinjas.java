package algorithms;

import java.util.Scanner;

public class CodingNinjas {
	
	private static Scanner in;
	
	public static String minLengthWord(String input) {
		char[] ch = input.toCharArray();
		int min_length = Integer.MAX_VALUE;
        String shortest_word = "";
		for (int i = 0; i < ch.length; i++) {
			String s = "";

			while (i < ch.length && ch[i] != ' ') {
				s = s+ch[i];
				i++;
			}

			if (s.length() < min_length && s.length() > 0) {
				min_length = s.length();
                shortest_word = new String(s);
			}

		}
		return shortest_word;
	}
	
	public static void print2Darray(int n, int m, int[][] arr){
		for (int i = 0; i<n; i++) {
			for (int j = 0; j<n-i; j++){
				for (int k = 0; k<m; k++) {
					System.out.print(arr[i][k]);
				}
				System.out.println();
			}
		}
	}
	public static int countWords(String input) {
		if (input == null || input.isEmpty()) {
			return 0;
		}
		
		String[] words = input.split("\\s+");
		return words.length;
	}
	
	public static void subString(String input) {
		int n = input.length();
		// pick starting point
		for (int i=0; i <= n; i++) {
			// pick ending point
			for (int j=i+1; j <= n; j++) {
				System.out.println(input.substring(i, j));
			}
		}
	}

	public static String wordReverse(String input) {
		String ans = "";
		String s[] = input.split(" ");
		for (int i = s.length-1; i >= 0; i--) {
			ans += s[i] + " ";
		}
		return ans;
	}
	
	public static String reverseWordWise(String input) {
		// Write your code here
        String output = "";
        int index = 0;
        
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == ' ') {
                index = i+1;
                output += input.charAt(i);
            } else {
                output = output.substring(0,index) + input.charAt(i) + output.substring(index);
            }
        }
        return output;

	}
	
	public static void findLargest(int input[][]){
		
		/* Your class should be named Solution.
		* Don't write main() function.
	 	* Don't read input, it is passed as function argument.
	 	* Print output as specified in the question
		*/
        int numRows = input.length;
		int numCols = input[0].length;
        int num = 0;
        
        int ans = Integer.MIN_VALUE;
        String row_or_col = "NA";

		for (int i = 0; i < numRows; i++) {
			int sum = 0;
			for (int j = 0; j < numCols; j++) {
				sum += input[i][j];
			}
            if (sum > ans) {
                ans = sum;
                num = i;
                row_or_col = "row";
            }
		}
        
        for (int i = 0; i < numCols; i++) {
			int sum = 0;
			for (int j = 0; j < numRows; j++) {
				sum += input[i][j];
			}
            if (sum > ans) {
                ans = sum;
                num = i;
                row_or_col = "column";
            }
		}
        
        System.out.println(row_or_col+" "+num+" "+ans);
	}
	
	public static void count(String str) {
		char[] ch = str.toCharArray();
		int max_length = 0;
		for (int i = 0; i < ch.length; i++) {
			String s = "";

			while (i < ch.length && ch[i] != ' ') {
				s = s+ch[i];
				i++;
			}

			if (s.length() > max_length) {
				max_length = s.length();
			}

		}
		System.out.println(max_length);
	}
	
	public static void leaders(int[] input) {
		/* Your class should be named Solution 
		 * Don't write main(). 
		 * Don't read input, it is passed as function argument. 
		 * Print output and don't return it. 
		 * Taking input is handled automatically. 
		 */

		for (int i=0; i < input.length; i++) {
            boolean leader = true;
            int candidate = input[i];
            // check if it's a leader
            int j = i+1;
            while (j<input.length) {
                if (input[j] > input[i]) {
                    leader = false;
                    break;
                }
                j++;
            }
            if (leader==true) {
                System.out.print(candidate+" ");
            }
        }
	}
	
	public static void main(String[] args) {
		int[] intArray = new int[]{3,12,34,2,0,-1};
		leaders(intArray);
	}
}