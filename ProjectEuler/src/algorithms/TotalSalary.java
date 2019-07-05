package algorithms;

import java.util.Scanner;
import java.lang.Math;

public class TotalSalary {
	
	private static Scanner s;
	
	public static long SalaryCompute(int basic, String grade){
		double hradapf = 1.59*basic;
		int allow;
		switch(grade) {
			case "A":
				allow = 1700;
				break;
			case "B":
				allow = 1500;
				break;
			default:
				allow = 1300;
				break;
		}
		double sum = hradapf + (double) allow;
		
		return Math.round(sum);
	}
	
	public static void main(String[] args) {
		s = new Scanner(System.in);
		
		int basic = s.nextInt();
		String grade = s.nextLine().trim();
		
		System.out.println(SalaryCompute(basic,grade));
	}

}