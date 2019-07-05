package algorithms;

public class PerfectSquares {

	public static void main(String[] args) {	
		System.out.println(numSquares(28));
	}

    public static int numSquares(int n) {
        int[] table = new int[n+1];
        for( int i=0; i<n+1; i++){
        	table[i]=Integer.MAX_VALUE;
        }
        table[0] = 0;
        for( int i=1; i<(int)Math.sqrt(n)+1; i++){
        	table[i*i]=1;
        }
        
        for( int j=0; j<n; j++){
        	for( int k=0; k<(int)Math.sqrt(n-j)+1; k++){
        		table[j+k*k]=Math.min(table[j+k*k], 1+table[j]);
        	}      		
        }
        
        return table[n];
    }
}