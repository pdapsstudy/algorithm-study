import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
/*

1. 문제 재정의
뱀이 벽에 부딪히거나, 자기 자신의 몸에 부딪혀서 게임이 끝날 때까지의 시간을 구하는 문제

2. 상세풀이
N+2 * N+2 로 2차원 배열을 만들어, 테두리에 WALL(-1)을 지정해놓음
뱀의 몸 좌표를 관리하기 위해, y, x, dir 을 저장하고 있는 class 생성
머리는 map[][] 에서 뱀이라는 것을 알리기 위해 SANKE(-1)을 찍음
뱀의 꼬리는 머리가 남긴 dirs[][] 배열을 따라가며 몸의 길이를 줄여나가며 SNAKE(-1)을 BLANK(0)으로 바꿈


머리가 부딪히면 끝나는 것

*/
import java.io.*;
import java.util.*;
public class Main {
	static class Snake{
		int y, x, dir;
		Snake(int y, int x, int dir){
			this.y = y;
			this.x = x;
			this.dir = dir;
		}
	}
	static final int APPLE = 1;
	static final int WALL = -2;
	static final int SNAKE = -1;
	static final int BLANK = 0;
	static int[] dy = {0, 1, 0, -1};
	static int[] dx = {1, 0, -1, 0};
	static Snake head = new Snake(1, 1, 0);
	static Snake tail = new Snake(1, 1, 0);
	static int N, K, L;
	static int time = 0;
	static int[][] map;
	static int[][] dirs;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = null;
        
        N = Integer.parseInt(br.readLine());
        map = new int[N+2][N+2];
        dirs = new int[N+2][N+2];
        
        
        Arrays.fill(map[0], WALL);
        Arrays.fill(map[N+1], WALL);
        for(int i=0; i<N+2; i++) {
        	map[i][0] = WALL;
        	map[i][N+1] = WALL;
        }
        for(int i=0; i<N+1; ++i)
        	Arrays.fill(dirs[i], -1);
        
        
        K = Integer.parseInt(br.readLine());
        for(int i=0; i<K; ++i) {
        	st = new StringTokenizer(br.readLine());
        	map[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())]=APPLE;
        }
        
        ArrayList<int[]> pos = new ArrayList<>();
        K = Integer.parseInt(br.readLine());
        for(int i=0; i<K; ++i) {
        	st = new StringTokenizer(br.readLine());
        	pos.add(new int[] {Integer.parseInt(st.nextToken()), st.nextToken().equals("D") ? 1 : -1});
        }
        

        Collections.sort(pos, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        map[head.y][head.x] = SNAKE;
        dirs[head.y][head.x] = head.dir;
        int idx = 0;
        
        while(true) {
 
        	time++;
            
        	int ny = head.y + dy[head.dir];
        	int nx = head.x + dx[head.dir];
        	
        	head = new Snake(ny, nx, head.dir);
        	dirs[head.y][head.x] = head.dir;
        	if(map[head.y][head.x] == WALL || map[head.y][head.x] == SNAKE) break;
        	
        	if(map[head.y][head.x] == APPLE) {
        		map[head.y][head.x] = SNAKE;
        	}else {
        		map[head.y][head.x] = SNAKE;
        		map[tail.y][tail.x] = BLANK;
        		int d = dirs[tail.y][tail.x];
        		int tny = tail.y+dy[d];
        		int tnx = tail.x+dx[d];
        		tail = new Snake(tny, tnx, d);
        	}
        	
        	if(idx < pos.size() && time == pos.get(idx)[0]) {
        		head.dir = (head.dir + pos.get(idx)[1]+4) % 4;
        		dirs[head.y][head.x] = head.dir;
        		idx++;

        	}
        	
     	
        }
        sb.append(time);
        bw.write(sb.toString());
        bw.close();
        br.close();
	}

}
