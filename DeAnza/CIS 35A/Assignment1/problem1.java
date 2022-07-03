import java.util.Scanner;

public class problem1 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.print("How many TVs were sold? ");
		int tvs = sc.nextInt();
		System.out.print("How many VCRs were sold? ");
		int vcrs = sc.nextInt();
		System.out.print("How many remote controllers were sold? ");
		int remotes = sc.nextInt();
		System.out.print("How many CDs were sold? ");
		int cds = sc.nextInt();
		System.out.print("How many tape recorders were sold? ");
		int tape_recorders = sc.nextInt();
		sc.close();
		
		System.out.printf("%5s", "QTY"); 
		System.out.printf("%20s", "DESCRIPTION"); 
		System.out.printf("%13s", "UNIT PRICE"); 
		System.out.printf("%14s", "TOTAL PRICE"); 
		System.out.println();
		
		System.out.printf("%5d",tvs);
		System.out.printf("%20s","TV");
		System.out.printf("%13.2f",400.00);
		System.out.printf("%14.2f%n",tvs*400.00);
		
		System.out.printf("%5d",vcrs);
		System.out.printf("%20s","VCR");
		System.out.printf("%13.2f",220.00);
		System.out.printf("%14.2f%n",vcrs*220.00);
		
		System.out.printf("%5d",remotes);
		System.out.printf("%20s","Remote Controller");
		System.out.printf("%13.2f",35.20);
		System.out.printf("%14.2f%n",remotes*35.20);
		
		System.out.printf("%5d",cds);
		System.out.printf("%20s","CD Player");
		System.out.printf("%13.2f",300.00);
		System.out.printf("%14.2f%n",cds*300.00);
		
		System.out.printf("%5d",tape_recorders);
		System.out.printf("%20s","Tape Recorder");
		System.out.printf("%13.2f",150.00);
		System.out.printf("%14.2f%n",tape_recorders*150.00);
		System.out.println();

		double subtotal = tvs*400.00+vcrs*220.00+remotes*35.20
				+cds*300.00+tape_recorders*150.00;
		double tax = subtotal*.0825;
		double total = subtotal+tax;
		System.out.printf("%25s", "SUBTOTAL");
		System.out.printf("%13.2f%n", subtotal);
		System.out.printf("%25s", "TAX");
		System.out.printf("%13.2f%n", tax);
		System.out.printf("%25s", "TOTAL");
		System.out.printf("%13.2f%n", total);
	}

}


//Set 1 -> 2 1 4 1 2 
//QTY         DESCRIPTION   UNIT PRICE   TOTAL PRICE
//2                  TV       400.00        800.00
//1                 VCR       220.00        220.00
//4   Remote Controller        35.20        140.80
//1           CD Player       300.00        300.00
//2       Tape Recorder       150.00        300.00
//
//             SUBTOTAL      1760.80
//                  TAX       145.27
//                TOTAL      1906.07

//Set 2 -> 3 0 2 0 21 
//QTY         DESCRIPTION   UNIT PRICE   TOTAL PRICE
//3                  TV       400.00       1200.00
//0                 VCR       220.00          0.00
//2   Remote Controller        35.20         70.40
//0           CD Player       300.00          0.00
//21       Tape Recorder       150.00       3150.00
//
//             SUBTOTAL      4420.40
//                  TAX       364.68
//                TOTAL      4785.08

