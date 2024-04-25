import java.io.*;
import java.util.*;

public class Main {
	static class Line implements Comparable<Line>{
		int a, b;
		Line(int a, int b){
			this.a = a;
			this.b = b;
		}
		@Override
		public int compareTo(Line l) {
			return this.a - l.a;
		}
		
	}
	static int N;
	static int[] dp;
	static int ans;
	static Line[] lines;
	public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
        StringTokenizer st = null;
        
        N = Integer.parseInt(br.readLine());
        lines = new Line[N];
        dp = new int[N+1];
        
        for(int i=0; i<N; ++i) {
        	st = new StringTokenizer(br.readLine());
        	lines[i] = new Line(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        
        Arrays.sort(lines);

        for(int i=0; i<N; ++i) {
        	dp[i+1] = 1;
        	for(int j=0; j<i; ++j) {
        		if(lines[j].b >= lines[i].b) continue;
        		dp[i+1] = Math.max(dp[i+1], dp[j+1]+1);
        	}
        }
        
    
        for(int i=1; i<=N; ++i)
        	ans = Math.max(ans,  dp[i]);
        
        sb.append(N - ans);
        bw.write(sb.toString());
        bw.close();
        br.close();
    }

}
