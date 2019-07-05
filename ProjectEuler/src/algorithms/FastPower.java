package algorithms;

public class FastPower {

	public static double fastPow(double x, long n){
		if (n == 0) {
			return 1.0;
		}
		
		if (n < 0){
			return 1/fastPow(x, -n);
		}
		double half = fastPow(x, n/2);
		if (n % 2 == 0){
			return half*half;
		} else {
			return half*half*x;
		}
	}
	
	public static void main(String[] args) {
		System.out.println(fastPow(2.0,12));
	}

}