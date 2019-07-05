package algorithms;

public class GCD {
	public static int gcd(int p, int q) {
		if (q == 0) {
			return p;
		}
		return gcd(q, p % q);
	}

	public static void main(String[] args) {
		System.out.println(gcd(100,625));
	}

}
