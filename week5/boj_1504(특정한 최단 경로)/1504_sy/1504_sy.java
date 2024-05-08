import java.io.*;
import java.util.*;
/*
 1번에서 N번으로 가는 최단 경로
 이 때 A, B 정점을 무조건 가야함
 
 정점을 연결한 그래프는  양방향 그래프
 그러므로, A-B == B-A
 1 A, A B, B N
 1 B, A B, A N
 둘 중 짧은 것을 고르면 됨
 
 함수 func(A, B) => A에서 B로 가는 최단 경로 리턴
 없으면 -1
 * */
public class Main {
	static class Node implements Comparable<Node>{
		int idx, dist;
		Node(int idx, int dist){
			this.idx = idx;
			this.dist = dist;
		}
		
		@Override
		public int compareTo(Node n) {
			if(this.dist == n.dist) return this.idx - n.idx;
			return this.dist - n.dist;
		}
	}
	
	
	static final int INF = (int)1e7;
	static int N, M;
	static int A, B;
	static ArrayList<Node>[] graph;
	static PriorityQueue<Node> pq = new PriorityQueue<>();
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		String[] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]);
		M = Integer.parseInt(input[1]);
		
		graph = new ArrayList[N+1];
		for(int i=1; i<=N; ++i) graph[i] = new ArrayList<>();
		
		for(int i=0; i<M; ++i) {
			input = br.readLine().split(" ");
			int s = Integer.parseInt(input[0]);
			int e = Integer.parseInt(input[1]);
			int w = Integer.parseInt(input[2]);
			
			graph[s].add(new Node(e, w));
			graph[e].add(new Node(s, w));
		}
		
		input = br.readLine().split(" ");
		A = Integer.parseInt(input[0]);
		B = Integer.parseInt(input[1]);
		
		int[] dist1 = getMinDist(1);
		int[] distA = getMinDist(A);
		int[] distN = getMinDist(N);
		
		int path1 = dist1[A] + distA[B] + distN[B];
		int path2 = dist1[B] + distA[B] + distN[A];
		int ans = path1 < path2 ? path1 : path2;
		ans = ans >= INF ? -1 : ans;
		
		sb.append(ans);
		bw.write(sb.toString());
		bw.close();
		br.close();
		
	}
	private static int[] getMinDist(int n) {
		int[] dist = new int[N+1];
		pq.clear();
		
		Arrays.fill(dist, INF);
		dist[n] = 0;
		pq.add(new Node(n, 0));
		
		while(!pq.isEmpty()) {
			Node cur = pq.poll();
			int curIdx = cur.idx;
			int curDist = cur.dist;
			
			if(dist[curIdx] != curDist) continue;
			
			for(Node nx : graph[curIdx]) {
				int nxIdx = nx.idx;
				int nxDist = nx.dist;
				int newDist = dist[curIdx] + nxDist;
				if(dist[nxIdx] <= newDist) continue;
				dist[nxIdx] = newDist;
				pq.offer(new Node(nxIdx, newDist));
			}
		}
		return dist;
	}

}