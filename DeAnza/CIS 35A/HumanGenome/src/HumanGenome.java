
public class HumanGenome {
	
	private String GenomeName;
	private int NumberofGenes, NumberofChromosomes, NumberofCells;

	public HumanGenome(String name, int numGenes, int numChromosomes, int numCells) {
		GenomeName = name;
		NumberofGenes = numGenes;
		NumberofChromosomes = numChromosomes;
		NumberofCells = numCells;
	}
	
	public String getGenomeName() {
		return GenomeName;
	}
	
	public int getNumberofCells() {
		return NumberofCells;
	}
	
	public int getNumberofGenes() {
		return NumberofGenes;
	}
	
	public int getNumberofChromosomes() {
		return NumberofChromosomes;
	}
	
	public void setGenomeName(String name) {
		GenomeName = name;
	}
	
	public void setNumberofCells(int numCells) {
		NumberofCells = numCells;
	}
	
	public void setNumberofGenes(int numGenes) {
		NumberofGenes = numGenes;
	}
	
	public void setNumberofChromosomes(int numChromosomes) {
		NumberofChromosomes = numChromosomes;
	}
	
	public void print() {
		System.out.println("Human genome details");
		System.out.printf("Genome Name : %s\n", GenomeName);
		System.out.printf("Number of genes : %d\n", NumberofGenes);
		System.out.printf("Number of chromosomes : %d\n", NumberofChromosomes);
		System.out.printf("Number of cells in trillions: %d\n", NumberofCells);
	}

}
