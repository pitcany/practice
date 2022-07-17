
public class NucleicAcid {
	
	private String Name;
	private String ChemicalFormula;
	private float Molarmass;
	private float Density;
	
	public NucleicAcid(String name, String chemicalFormula, float molarmass, float density) {
		Name = name;
		ChemicalFormula = chemicalFormula;
		Molarmass = molarmass;
		Density = density;
		}

	public String getName() {
	return Name;
	}

	public void setName(String name) {
	Name = name;
	}

	public String getChemicalFormula() {
	return ChemicalFormula;
	}

	public void setChemicalFormula(String chemicalFormula) {
	ChemicalFormula = chemicalFormula;
	}

	public float getMolarmass() {
	return Molarmass;
	}

	public void setMolarmass(float molarmass) {
	Molarmass = molarmass;
	}

	public float getDensity() {
	return Density;
	}

	public void setDensity(float density) {
	Density = density;
	}

	public void print(){

	System.out.printf("\n" + getName() + "\n");
	System.out.printf("Chemical formula - " + getChemicalFormula() + "\n");
	System.out.printf("Molar mass - " + getMolarmass() + "g/mol \n");
	System.out.printf("Density - " + getDensity() + "g/cm3 \n");
	}
}