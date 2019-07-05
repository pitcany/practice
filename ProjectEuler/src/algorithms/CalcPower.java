package algorithms;

import java.util.Scanner;

public class CalcPower {

	private static Scanner s;

	public static void main(String[] args) {
		s = new Scanner(System.in);
		int x = s.nextInt();
		int n = s.nextInt();
		int res = 1;
		
		while (n > 0){
			res *= x;
			n -= 1;
		}
		
		System.out.println(res);

	}

}