import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[][] grid = new int[30][2];
	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

		N = Integer.parseInt(br.readLine());
		for(int i=0; i<N; ++i) {
			String[] input = br.readLine().split(" ");
			char parent = input[0].charAt(0);
			char lChild = input[1].charAt(0);
			char rChild = input[2].charAt(0);
			
			int idx = parent - 'A';
			if(lChild != '.') {
				grid[idx][0] = lChild - 'A';
			}else {
				grid[idx][0] = -1;
			}
			
			if(rChild != '.') {
				grid[idx][1] = rChild - 'A';
			}else {
				grid[idx][1] = -1;
			}
		}
			
        preOrder(0);
        sb.append('\n');
        inOrder(0);
        sb.append('\n');
        postOrder(0);

        bw.write(sb.toString());
        bw.close();
        br.close();
	}
	
	static void preOrder(int nodeIdx) {
		char node = (char)(nodeIdx + 'A');

		sb.append(node);
		if(grid[nodeIdx][0] != -1) preOrder(grid[nodeIdx][0]);
		if(grid[nodeIdx][1] != -1) preOrder(grid[nodeIdx][1]);
		return;
	}
	static void inOrder(int nodeIdx) {
		char node = (char)(nodeIdx + 'A');
		
		if(grid[nodeIdx][0] != -1) inOrder(grid[nodeIdx][0]);
		sb.append(node);
		if(grid[nodeIdx][1] != -1) inOrder(grid[nodeIdx][1]);
		return;
	}
	static void postOrder(int nodeIdx) {
		char node = (char)(nodeIdx + 'A');
		
		if(grid[nodeIdx][0] != -1) postOrder(grid[nodeIdx][0]);
		if(grid[nodeIdx][1] != -1) postOrder(grid[nodeIdx][1]);
		sb.append(node);
		return;
	}

}