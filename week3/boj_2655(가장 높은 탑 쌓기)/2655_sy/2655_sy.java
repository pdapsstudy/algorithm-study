import java.io.*;
import java.util.*;

class Wall implements Comparable<Wall>{
	int num, s, h, w;
	Wall(int num, int s, int h, int w){
		this.num = num;
		this.s = s;
		this.h = h;
		this.w = w;
	}
	
	@Override
	public int compareTo(Wall w) {
		return w.s - this.s;
	}
	
}
public class Main {
	static int N;
	static int[][] dp;
	static int idx, max, cnt;
	static ArrayList<Wall> walls = new ArrayList<>();
	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(br.readLine());
		dp = new int[N+5][2];
		
		for(int i=1; i<=N; ++i) {
			String[] input = br.readLine().split(" ");
			walls.add(new Wall(i, Integer.parseInt(input[0]), Integer.parseInt(input[1]), Integer.parseInt(input[2])));
		}
		
		walls.add(new Wall(0, 10000, 0, 10000));
		Collections.sort(walls);
		idx = 0;
		dp[0][1] = 0;
		max = 0;
		
		for(int i=1; i<=N; ++i) {
			Wall cur = walls.get(i);
			dp[i][0] = cur.h;
			for(int j=i; j>=0; --j) {
				Wall prev = walls.get(j);
				if(prev.w > cur.w && dp[i][0] < dp[j][0] + cur.h) {
					dp[i][0] = dp[j][0] + cur.h;
					dp[i][1] = j; 
				}
				max = max < dp[i][0] ? dp[i][0] : max;
			}
		}
		
		for(int i=N; i>=0; --i) {
			if(dp[i][0] == max) {
				idx = i;
				break;
			}
		}
		
		while(idx!=0) {
			sb.append(walls.get(idx).num).append('\n'); 
			++cnt;
			idx = dp[idx][1];
		}
		
		bw.write(Integer.toString(cnt));
		bw.write('\n');
		bw.write(sb.toString());
		bw.close();
		br.close();
	}
}