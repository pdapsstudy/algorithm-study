import java.io.*;
import java.util.*;
import java.util.stream.Stream;

public class BOJ22502 {
	static int T;
	static int[] cost; 
	static int maxProfit = -1;
	static long ans = 0;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		T = Integer.parseInt(br.readLine());
		
		for(int t=0; t<T; ++t) {
			int N = Integer.parseInt(br.readLine());
			init(N);
			String[] input = br.readLine().split(" ");
			cost = Stream.of(input).mapToInt(Integer::parseInt).toArray();
			findMaxProfit(N);
			sb.append(ans).append('\n');
		}
		bw.write(sb.toString());
		bw.close();
		br.close();
	}	

	private static void findMaxProfit(int n) {
		maxProfit = cost[n-1];
		for(int i=n-2; i>=0; i--) {
			if(cost[i] >= maxProfit) {
				maxProfit = cost[i];
			}else {
				ans += maxProfit - cost[i];
			}
		}
		
	}

	private static void init(int n) {
		cost = new int[n];
		maxProfit = -1;
		ans = 0;
	}

}
