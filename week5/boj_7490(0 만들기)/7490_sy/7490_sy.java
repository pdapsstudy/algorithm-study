import java.io.*;
import java.util.*;
/*

계산을 하면서, 처리를 했다면 더 빨리 풀 수 있었을 듯. isZero() 작성에서 deque를 써보고 싶어서 조금 오래걸렸다. 결국에는 못 썼음

각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 모든 수식을 출력한다. 각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.
라는 조건에 의해 출력 순서가 있었음

1+2-3

1+2-3+4-5-6+7
1+2-3-4+5+6-7
1-2+3+4-5+6-7
1-2-3-4-5+6+7
1-2 3+4+5+6+7
1-2 3-4 5+6 7

1+2-3

1+2-3+4-5-6+7
1+2-3-4+5+6-7
1-2 3+4+5+6+7
1-2 3-4 5+6 7
1-2+3+4-5+6-7
1-2-3-4-5+6+7
 * */

 
 * */
public class BOJ7490 {
	static int T;
	static int N;
	static char[] ops = new char[] {' ', '+', '-'};
	static StringBuilder sb = new StringBuilder();
	static char[] selected = new char[10];
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		T = Integer.parseInt(br.readLine());
		for(int t=0; t<T; ++t) {
			N = Integer.parseInt(br.readLine());

			func(0);
			sb.append('\n');
		}

		bw.write(sb.toString());
		bw.close();
		br.close();
	}
	private static void func(int cnt) {
		if(cnt == N-1) {
			isZero();
			return;
		}
		for(int i=0; i<3; i++) {
			selected[cnt] = ops[i];
			func(cnt + 1);
		}
	}

	private static void isZero() {
		StringBuilder temp = new StringBuilder();
		
		for(int i=1; i<N; ++i) {
			temp.append(i).append(selected[i-1]);
		}

		temp.append(N);

		int lenth = temp.length();
		int sum = 0;
		int prev = 0;
		int op = 0;
		for(int i=lenth-1; i>=0; --i) {
			if(temp.charAt(i)=='+') {
				sum += prev;
			}else if(temp.charAt(i)=='-') {
				sum -= prev;
			}else if(temp.charAt(i)==' ') {
				op = 1;
			}else {
				if(op == 1) {
					prev = (int) ((temp.charAt(i)-'0') * (Math.pow(10, String.valueOf(prev).length())) + prev);
					op = 0;
				}else {
					prev = temp.charAt(i)-'0';
				}
			}
		}
		sum += prev; 

		if(sum == 0)
			sb.append(temp).append('\n');
		
	}
}

