package boj;
import java.io.*;
import java.util.*;
public class BOJ4949 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		Deque<Character> st = new ArrayDeque<>();
		
		String input = "";
		
		while((input = br.readLine()).length() != 1) {
			
			for(int i=0;i<input.length(); ++i) {
				char cur = input.charAt(i);
				if(cur == '(' || cur == '[') {
					st.offerFirst(cur);
				}else if(cur == ')') {
					if(!st.isEmpty() && st.peekFirst()=='(') {
						st.poll();
						continue;
					}
					st.offerFirst(cur);
					break;
				}else if(cur == ']') {
					if(!st.isEmpty() && st.peekFirst()=='[') {
						st.poll();
						continue;
					}
					st.offerFirst(cur);
					break;
				}
			}
			sb.append(st.isEmpty() ? "yes" : "no").append('\n');
			st.clear();
		}
		
		bw.write(sb.toString());
		bw.close();
		br.close();
	}

}
