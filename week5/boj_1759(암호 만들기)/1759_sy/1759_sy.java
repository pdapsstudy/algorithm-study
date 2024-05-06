import java.io.*;
import java.util.*;

public class BOJ1759 {
	static char[] vowel = new char[]{'a', 'e', 'i', 'o', 'u'};
	static int N, M;
	static char[] chars;
	static ArrayList<Character> selected = new ArrayList<>();
	static StringBuilder sb = new StringBuilder();
    
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] input = br.readLine().split(" ");
		M = Integer.parseInt(input[0]);
		N = Integer.parseInt(input[1]);
		
		input = br.readLine().split(" ");
		chars = String.join("", input).toCharArray();
		Arrays.sort(chars);
		
		comb(0, 0);
		
		bw.write(sb.toString());
		bw.close();
		br.close();
	}

	private static void comb(int idx, int cnt) {
		if(cnt == M) {
			if(isPossiblePW()) {
				sb.append(getPossiblePW()).append('\n');
			}
			return;
		}
		
		for(int i=idx; i<N; ++i) {
			selected.add(chars[i]);
			comb(i+1, cnt+1);
			selected.remove(selected.size()-1);
		}
		
	}

	private static StringBuilder getPossiblePW() {
		StringBuilder ret = new StringBuilder();
		for(char s:selected) {
			ret.append(s);
		}
		return ret;
	}

	private static boolean isPossiblePW() {
		int wLen = selected.size();
		int vCnt = 0;
		int cCnt = 0;
		for(char s:selected) {
			for(int i=0; i<5; ++i) {
				if(vowel[i] == s) {
					++vCnt;
					break;
				}
			}
		}

		cCnt = wLen - vCnt;
		return vCnt >=1 && cCnt >=2 ? true: false;
	}

}
