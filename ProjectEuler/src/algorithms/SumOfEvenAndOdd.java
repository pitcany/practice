package algorithms;

import java.util.Scanner;

public class SumOfEvenAndOdd {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		int num = s.nextInt();
		
		int evenSum = 0, oddSum = 0;
		
		while(num > 0){
			int last = num % 10;
			if (last % 2 == 0) {
				evenSum += last;
			}
			else {
				oddSum += last;
			}
			num = num / 10;
		}
		System.out.println(evenSum + " " + oddSum);
	}

}
