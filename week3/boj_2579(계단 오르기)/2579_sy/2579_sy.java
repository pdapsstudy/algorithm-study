import java.io.*;
import java.util.*;

public class Main {

	static int N;
	static int[] stairs;
	static int[][] dp;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		N = Integer.parseInt(br.readLine());
		stairs = new int[N+2];
		dp = new int[N+2][3];
		for(int i=1; i<=N; ++i) {
			stairs[i] = Integer.parseInt(br.readLine());
		}
		
		dp[1][1] = dp[1][2] = stairs[1];
		dp[2][1] = dp[2][2] = stairs[2];
		
		for(int k=1; k<=N; ++k) {
			if(k-2>=0) {
				dp[k][1] = Math.max(dp[k-2][2]+stairs[k], dp[k][1]);
				dp[k][2] = Math.max(dp[k][2], dp[k-2][2]+stairs[k]);
			}
			dp[k][2] = Math.max(dp[k-1][1]+stairs[k], dp[k][2]);
		}
		
		System.out.println(Math.max(dp[N][1], dp[N][2]));
	}
}