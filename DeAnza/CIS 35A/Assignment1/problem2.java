import java.util.Scanner;

public class problem2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter a temperature in Centigrade: ");
		float centigrade = sc.nextFloat();
		float fahrenheit_convert = 32.0f+centigrade*1.80f;
		System.out.printf("Degrees in Fahrenheit is %3.2f%n",fahrenheit_convert);
		
		System.out.print("Enter a temperature in Fahrenheit: ");
		float fahrenheit = sc.nextFloat();
		float centigrade_convert = (fahrenheit-32.0f) / 1.80f;
		System.out.printf("Degrees in Centigrade is %3.2f%n",centigrade_convert);
		sc.close();
	}

}

//Enter a temperature in Centigrade: 32
//Degrees in Fahrenheit is 89.60
//Enter a temperature in Fahrenheit: 100
//Degrees in Centigrade is 37.78

//Enter a temperature in Centigrade: 0
//Degrees in Fahrenheit is 32.00
//Enter a temperature in Fahrenheit: 0
//Degrees in Centigrade is -17.78

//Enter a temperature in Centigrade: -10
//Degrees in Fahrenheit is 14.00
//Enter a temperature in Fahrenheit: -1
//Degrees in Centigrade is -18.33