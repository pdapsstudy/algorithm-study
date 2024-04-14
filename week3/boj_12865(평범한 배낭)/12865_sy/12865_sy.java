import java.io.*;
import java.util.*;

public class Main {
	static int N, K;
	static int[][] dp;
	static int[] w;
	static int[] v;
	public static void main(String[] args) throws Exception{
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String[] input = reader.readLine().split(" ");
		N = Integer.parseInt(input[0]);
		K = Integer.parseInt(input[1]);
		
		dp = new int[N+1][K+1];
		w = new int[N+1];
		v = new int[N+1];
		for(int i=1; i<=N; ++i) {
			input = reader.readLine().split(" ");
			w[i] = Integer.parseInt(input[0]);
			v[i] = Integer.parseInt(input[1]);
		}
		
		for(int i=1; i<=N; ++i) {
			for(int j=1; j<=K; ++j) {
				if(j - w[i] >= 0) {
					dp[i][j] = Math.max(dp[i-1][j-w[i]]+v[i], dp[i-1][j]);
				}else {
					dp[i][j] = dp[i-1][j];
				}
			}
		}

		System.out.println(dp[N][K]);
	}

}
