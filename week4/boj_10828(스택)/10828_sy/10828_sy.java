import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static Deque<Integer> stack = new ArrayDeque<>();
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		N = Integer.parseInt(br.readLine());
		
		for(int i=0; i<N; ++i) {
			String[] input = br.readLine().split(" ");
			if(input.length == 2) {
				exePush(input);
			}else {
				exeCmd(input);
			}
		}
		bw.write(sb.toString());
		bw.close();
		br.close();

	}
	private static void exeCmd(String[] input) {
		String cmd = input[0];
		
		
		if(cmd.equals("empty")) {
			sb.append(exeIsEmpty()?1:0).append('\n');
		}else if(cmd.equals("top")) {
			sb.append(exeGetTop()).append('\n');
		}else if(cmd.equals("size")) {
			sb.append(exeGetSize()).append('\n');
		}else if(cmd.equals("pop")) {
			sb.append(exeGetPop()).append('\n');
		}
	}
	
	
	
	private static int exeGetSize() {
		return stack.size();
	}
	private static int exeGetPop() {
		return !exeIsEmpty() ? stack.pollFirst() : -1;
	}
	private static int exeGetTop() {
		return !exeIsEmpty() ? stack.peekFirst() : -1; 
	}
	private static boolean exeIsEmpty() {
		return stack.isEmpty();
	}
	private static void exePush(String[] input) {
		
		int num = Integer.parseInt(input[1]);
		stack.addFirst(num);
	}

}
