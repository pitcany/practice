import java.util.Scanner;

public class GenomeInput {
	
	static Scanner sc = new Scanner(System.in);
	
	public static HumanGenome input(){
		//
		int numGenes, numChromosomes, numCells;
		String name;
		
		System.out.printf("Genome name: ");
		name = sc.nextLine();
		
		System.out.printf("Number of genes: ");
		numGenes = sc.nextInt();
		
		System.out.printf("Number of chromosomes: ");
		numChromosomes = sc.nextInt();
		
		System.out.printf("Number of cells in the trillions: ");
		numCells = sc.nextInt();
		
		sc.nextLine();
		
		return new HumanGenome(name,numGenes,numChromosomes,numCells);
		
	}

	public static void main(String[] args) {
		HumanGenome Cinderella = input();
		HumanGenome Mufasa = input();
		HumanGenome Maleficent = input();
		
		Cinderella.print();
		Mufasa.print();
		Maleficent.print();

	}

}
