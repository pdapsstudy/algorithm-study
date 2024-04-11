import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N, C;
		int[] home;
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		home = new int[N];
		for(int i=0; i<N; ++i) {
			home[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(home);
		int left = 0;
		int right = home[N-1]-home[0];
		int ans = 0;
		while(left <= right) {
            int mid = left + (right - left) / 2;
            int count = 1;
            int prev = home[0];

            for(int i=1; i<N; ++i) {
                if(home[i] - prev >= mid) {
                    ++count;
                    prev = home[i];
                }
            }

            if(count < C) {
                right = mid - 1;
            }else {
                left = mid + 1;
                ans = mid;
            }
        }
        System.out.println(ans);
	}

}