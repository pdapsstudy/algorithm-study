import java.io.*;
import java.util.*;

class Main {
    
    static class Node {
		int idx, dist;
		Node(int idx, int dist){
			this.idx = idx;
			this.dist = dist;
		}
	}

	static class Element implements Comparable<Element>{
		int idx, dist;
		Element(int idx, int dist){
			this.idx = idx;
			this.dist = dist;
		}
		@Override
		public int compareTo(Element e) {
			return this.dist - e.dist;
		}
	}
    
	static final int INF = (int)1e8;
	static final int MN = 1005;
	static final int MM = 10005;
	static ArrayList<Node>[] graph = new ArrayList[MN];
	static ArrayList<Node>[] regraph = new ArrayList[MN];
	static PriorityQueue<Element> pq = new PriorityQueue<>();
	static int dist[] = new int[MM];
	static int redist[] = new int[MM];
	static int N, M, K;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		for(int i=1; i<=N; ++i) {
			graph[i] = new ArrayList<>();
			regraph[i] = new ArrayList<>();
			dist[i] = INF;
			redist[i] = INF;
		}
		
		for(int i=0; i<M; ++i) {
			st = new StringTokenizer(br.readLine(), " ");
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			graph[s].add(new Node(e, w));
			regraph[e].add(new Node(s, w));
		}
		
		dist[K]=0;
		redist[K]=0;
		dist = dijkstra(dist, graph);
		redist = dijkstra(redist, regraph);

		int ans = 0;
		for(int i=1; i<=N; ++i) {
			ans = Math.max(ans, dist[i]+redist[i]);
		}
		
		sb.append(ans);
		bw.write(sb.toString());
		bw.close();
		br.close();
	}
	static int[] dijkstra(int[] dist, ArrayList<Node>[] graph) {
		
		pq.clear();
		
		pq.add(new Element(K, dist[K]));

		while(!pq.isEmpty()) {
			Element cur = pq.poll();
			int curIdx = cur.idx;
			int curDst = cur.dist;
            
            if(dist[curIdx] != curDst) continue;
            
			for(Node nx:graph[curIdx]) {
				int nxIdx = nx.idx;
				int nxDst = nx.dist;
				int newDst = dist[curIdx] + nxDst;
				if(dist[nxIdx] <= newDst) continue;
				dist[nxIdx] = newDst;
				pq.add(new Element(nxIdx, dist[nxIdx]));
			}
		}
		return dist;
	}
}