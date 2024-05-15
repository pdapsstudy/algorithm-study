import java.io.*;
import java.util.*;

public class Main {
	static final int NO = -1000;
	static int N;
	static int[] nums;
	static int X, X2, Y;
	public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = null;
        
        N = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        nums = Arrays.stream(input).mapToInt(Integer::parseInt).toArray();
        
        
        switch(N) {
        case 1:
        	sb.append('A');
        	break;
        case 2:
//        	sb.append(nums[0] == nums[1] ? nums[0] : "A");
        	if(nums[0] == nums[1]) {
        		sb.append(nums[0]);
        	}else {
        		sb.append("A");
        	}
        	break;
        default :
        	if(nums[0]==nums[1]) {
//        		sb.append(isCorrect(2, nums[1])? nums[0] : "B");
        		if(isCorrect(2, nums[1])){
        			sb.append(nums[0]);
        		}else {
        			sb.append("B");
        		}
        	}else {
        		if(nums[1] == nums[2]) {
//        			sb.append(isCorrect(2, nums[1]) ? nums[1] : "B");
        			if(isCorrect(2, nums[1])){
            			sb.append(nums[1]);
            		}else {
            			sb.append("B");
            		}
        		}else {
        			findXY();
        			if(X2 != 0) {
        				sb.append("B");
        			}else {
//        				sb.append(isCorrect(3, NO) ? Math.abs(nums[N-1]*X+Y)>100 ? "B" : nums[N-1]*X+Y  : "B");
        				if(isCorrect(3, NO)){
//        					if(Math.abs(nums[N-1]*X+Y)>100) {
//        						sb.append("B");
//        					}else {
//        						
        						sb.append(nums[N-1]*X+Y);
//        					}
                			
                		}else {
                			sb.append("B");
                		}
        			}
        		}
        	}
        }
        
        bw.write(sb.toString());
        bw.close();
        br.close();
	}

	private static boolean isCorrect(int idx, int num) {
		if(num == NO) {
			for(int i=idx; i<N; ++i) {
				if(nums[i] != (nums[i-1] * (X) + Y)) return false;
			}
		}else {
			for(int i=idx; i<N; ++i) {
				if(nums[i] != num) return false;
			}
		}

		return true;
	}
    
	private static void findXY() {
		
		int a = nums[0];
		int b = nums[1];
		int c = nums[2];
		
		if(a == b && b == c) {
			X = 1;
			Y = 0;
			return;
		}else if(a==b){
			 X=200;
			 Y=200;
			 return;
		}
			
		X = (b-c)/(a-b);
		X2 = (b-c)%(a-b);
		Y = -1 * a *(X + X2) + b;
	}
        
}