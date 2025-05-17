package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_1954 {

	public static void main(String[] args) throws Exception {
		
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int[][] arr = new int[N][N];
			
			int bitnum = 0;
			int idx_x = 0;
			int idx_y = 0;
			
			for(int i=1;i<=N*N;i++) {
				if(bitnum == 0) {
					arr[idx_x][idx_y] = i;
					if(idx_y==N-1 || arr[idx_x][idx_y+1]!=0) {
						bitnum = 1;
						idx_x++;
					} else {
						idx_y++;
					}
				}
					else if (bitnum == 1) {
						arr[idx_x][idx_y] = i;
						if(idx_x==N-1 || arr[idx_x+1][idx_y]!=0) {
							bitnum = 2;
							idx_y--;
						}else {
							idx_x++;
						}
					} else if (bitnum == 2) {
						arr[idx_x][idx_y] = i;
						if(idx_y==0 || arr[idx_x][idx_y-1]!=0) {
							bitnum = 3;
							idx_x--;
						} else {
							idx_y--;
						}
					} else if(bitnum == 3) {
						arr[idx_x][idx_y] = i;
						if(idx_x==0 || arr[idx_x-1][idx_y]!=0) {
							bitnum = 0;
							idx_y++;
						} else {
							idx_x--;
						}
					}
			}
			System.out.println("#"+test_case);
			for(int i=0;i<N;i++) {
				String s = "";
				for(int j=0;j<N;j++) {
					s += String.valueOf(arr[i][j]) + " ";
				}
				System.out.println(s);
			}
		
		}
	}
}
