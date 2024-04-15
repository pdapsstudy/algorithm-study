import java.io.*;
import java.util.*;

public class BOJ22233 {
	static int N, M;
	static TreeSet<String> set = new TreeSet<>();
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		String[] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]);
		M = Integer.parseInt(input[1]);
		
		for(int i=0; i<N; ++i) {
			String s = br.readLine();
			set.add(s);
		}
		
		for(int i=0; i<M; ++i) {
			String[] candidate = br.readLine().split(",");
			for(int j=0; j<candidate.length; ++j) {
				if(set.contains(candidate[j])==false) continue;
				set.remove(candidate[j]);
			}
			sb.append(set.size());
			sb.append('\n');
		}
		
		bw.write(sb.toString());
		bw.close();
		br.close();
		
	}

}
