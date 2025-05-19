package 자바;

import java.util.Scanner;

public class D2_1979_dfs {
	static int N, K;
	static int[][] map;
	static boolean[][] visited;
	static int answer;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int test_case=1;test_case<=T;test_case++) {
			N = sc.nextInt();
			K = sc.nextInt();
			map = new int[N][N];
			visited = new boolean[N][N];
			answer = 0;
			
			for(int i=0;i<N;i++) {
				for(int j=0;j<N;j++) {
					map[i][j] = sc.nextInt();
				}
			}
			
			for(int i=0;i<N;i++) {
				for(int j=0;j<N;j++) {
					if(!visited[i][j] && map[i][j]==1) {
						int len = dfs(i, j, 0, 1);
						if(len==K) answer++;
					}
				}
			}
			visited = new boolean[N][N];
			for(int j=0;j<N;j++) {
				for(int i=0;i<N;i++) {
					if(!visited[i][j] && map[i][j]==1) {
						int len = dfs(i, j, 1, 0);
						if(len==K) answer++;
					}
				}
			}
			
			System.out.println("#" + test_case + " " + answer);
			
		}
	}
	
	private static int dfs(int x, int y, int dx, int dy) {
		visited[x][y] = true;
		int len = 1;
		
		int nx = x + dx;
		int ny = x + dy;
		
		if(nx>=0 &&  nx <N &&ny>=0&&ny<N) {
			if(!visited[nx][ny]&& map[nx][ny]==1) {
				len += dfs(nx, ny, dx, dy);
			}
		}
		return len;
	}
}
