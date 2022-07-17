
public class Driver {

public static void main(String[] args) {

// --- Instantiating the nucleic acids

NucleicAcid cytosine = new NucleicAcid("Cytosine", "C4H5N3O", 111.10f, 1.55f);
NucleicAcid adenine = new NucleicAcid("Adenine", "C5H5N5", 135.13f, 1.6f);
NucleicAcid guanine = new NucleicAcid("Guanine", "C5H5N5O", 151.13f, 2.200f);
NucleicAcid thymine = new NucleicAcid("Thymine", "C5H6N2O2", 126.115f, 1.223f);
NucleicAcid uracil = new NucleicAcid("Uracil", "C4H4N2O2", 112.08676f, 1.32f);

// --- calling all print methods to print details of nucleic acids

cytosine.print();
adenine.print();
guanine.print();
thymine.print();
uracil.print();

}
}