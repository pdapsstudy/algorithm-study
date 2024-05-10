import java.io.*;
import java.util.*;

public class Main {

	static int T;
	static Deque<Character> d1 = new ArrayDeque<>();
	static Deque<Character> d2 = new ArrayDeque<>();

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();	
		
		T = Integer.parseInt(br.readLine());
		
		for(int t=0; t<T; ++t) {
			d1.clear();
			d2.clear();
			String input = br.readLine();
			for(int i=0; i<input.length(); ++i) {
				switch(input.charAt(i)) {
				case '<':
					if(d1.isEmpty()) break;
					d2.offerFirst(d1.pollFirst());
					break;
				case '>':
					if(d2.isEmpty()) break;
					d1.offerFirst(d2.pollFirst());
					break;
				case '-':
					if(d1.isEmpty()) break;
					d1.removeFirst();
					break;
				default:
					d1.offerFirst(input.charAt(i));
				}
			}

			while(!d2.isEmpty()) {
				d1.offerFirst(d2.pollFirst());
			}

			StringBuilder temp = new StringBuilder();
			for (Character elem : d1) {
				  temp.append(elem);
			}

			temp.reverse();
			sb.append(temp).append('\n');
		}

		bw.write(sb.toString());
		bw.close();
		br.close();

	}

}