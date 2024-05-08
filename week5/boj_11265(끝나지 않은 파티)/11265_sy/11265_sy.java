import java.io.*;
import java.util.*;
/*
 
N개의 파티장 1부터 시
모든 파티장은 연결되어 있음
한 파티장에서 다른 파티장으로 가는 것을 구함

모든 지점을 돌아야 하고, 
a지점에서 k지점을 거쳐서 b지점을 가는게 더 빠를 경우,

dist[a][b] = Math.min(dist[a][b], dist[a][k] + dist[k][b]);
 1번 ~ 1, 2, 3, 4, 5
 2번 
 * */
public class Main {
	static final String ENJOY = "Enjoy other party";
	static final String STAY = "Stay here";
	static final int INF = (int)1e8;
	static int N;
	static int M;
	static int[][] graph;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		String[] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]);
		M = Integer.parseInt(input[1]);
		
		graph = new int[N][N];
		
		for(int i=0; i<N; ++i) {
			input = br.readLine().split(" ");
			for(int j=0; j<N; ++j) {
				graph[i][j] = Integer.parseInt(input[j]);
			}
		}
		
		for(int k=0; k<N; ++k) {
			for(int a=0; a<N; ++a) {
				for(int b=0; b<N; ++b) {
					if(a == b) continue; // 일방통행으로 모두 연결되어 있으니까, 여기서는 자기 자신일 경우에만 pass
					graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
				}
			}
		}

		int s=0, e=0, time=0;
		for(int i=0; i<M; ++i) {
			input = br.readLine().split(" ");
			s = Integer.parseInt(input[0])-1;
			e = Integer.parseInt(input[1])-1;
			time = Integer.parseInt(input[2]);
			sb.append(canEnjoy(s, e, time) ? ENJOY : STAY).append('\n'); 
			
		}
		bw.write(sb.toString());
		bw.close();
		br.close();
	}
	private static boolean canEnjoy(int s, int e, int time) {
		return graph[s][e] <= time;
	}

}