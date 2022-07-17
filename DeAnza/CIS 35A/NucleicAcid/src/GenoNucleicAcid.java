
import java.util.Scanner;

public class GenoNucleicAcid {
	
	static Scanner sc = new Scanner(System.in);
	
	public static NucleicAcid input() {
		
		String name, chemicalFormula;
		float molarmass, density;
		
		System.out.printf("Nucleic acid name: ");
		name = sc.nextLine();
		
		System.out.printf("Chemical formula: ");
		chemicalFormula = sc.nextLine();
		
		System.out.printf("Molar mass: ");
		molarmass = (float) sc.nextDouble();
		
		System.out.printf("Density: ");
		density = (float) sc.nextDouble();
		
		sc.nextLine();
		
		return new NucleicAcid(name, chemicalFormula, molarmass, density);
	}
	
	public static void main(String[] args) {
		NucleicAcid YKP = input();
		YKP.print();
	}

}