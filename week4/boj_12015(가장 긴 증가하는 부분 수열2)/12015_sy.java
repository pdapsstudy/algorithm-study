
import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[] arr;
	static ArrayList<Integer> lis;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		N = Integer.parseInt(br.readLine());
		lis = new ArrayList<>();
		arr = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; ++i) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		
		lis.add(arr[0]);
		for(int i=1; i<N; ++i) {
			if(lis.get(lis.size()-1) < arr[i]) {
				lis.add(arr[i]);
			}else {
				int idx = binarySearch(0, lis.size(), arr[i]);
				lis.set(idx, arr[i]);
				
			}
		}
		sb.append(lis.size());
        bw.write(sb.toString());
        bw.close();
        br.close();
	}
	private static int binarySearch(int left, int right, int target) {
		int mid = 0;
		
		while(left < right) {
			mid = left + (right - left)/2;
			if(lis.get(mid) == target) {
				return mid;
			}
			if(lis.get(mid) < target) {
				left = mid + 1;
			}else {
				right = mid;
			}
		}
		return right;
	}

}