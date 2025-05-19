package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_1979 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int K = sc.nextInt();
			int[][] puzzle = new int[N][N];
			
			for(int i=0; i<N;i++) {
				for(int j=0;j<N;j++) {
					puzzle[i][j] = sc.nextInt();
				}
			}
			int nowNum = 0;
			int answer = 0;
			
			//dfs로 푸는거같은데
			//가로로 한번 쭉 세기
			for(int i=0;i<N;i++) {
				if(puzzle[i][0]==1) {
					nowNum++;
				}
				for(int j=1;j<N;j++) {
					if(puzzle[i][j-1]!=0 && puzzle[i][j]==0) {
						if(nowNum == K) {
							answer+=1;
						}
						nowNum = 0;
					}
					else {
						if(puzzle[i][j]==1) {
							nowNum++;
						}
					}
				}
				if(nowNum == K) {
					answer+=1;
				}
				nowNum = 0;
			}
			//세로로 한번 쭉 세기
			for(int i=0;i<N;i++) {
				if(puzzle[0][i]==1) {
					nowNum++;
				}
				for(int j=1;j<N;j++) {
					if(puzzle[j-1][i]!=0 && puzzle[j][i]==0) {
						if(nowNum == K) {
							answer+=1;
						}
						nowNum = 0;
					}
					else {
						if(puzzle[j][i]==1) {
							nowNum++;
						}
					}
				}
				if(nowNum == K) {
					answer+=1;
				}
				nowNum = 0;
			}
			
			System.out.println("#"+test_case+" "+answer);
		}
	}

}
