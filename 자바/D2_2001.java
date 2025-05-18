package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_2001 {
	public static void main(String[] args) throws FileNotFoundException {
		
		//System.setIn(new FileInputStream("자바/res/input.txt"));

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int M = sc.nextInt();
			int[][] arr = new int[N][N];
			
			for(int i=0;i<N;i++) {
				for(int j=0;j<N;j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			int maxNum = 0;
			int nowNum = 0;
			int[] maxNums = new int[N-M+1];
			for(int i=0;i<N-M+1;i++) {
				nowNum = 0;
				for(int k=0;k<M;k++) {
					for(int l=0;l<M;l++) {
						nowNum += arr[i+k][l];
					}
				}
				maxNum = nowNum;
				for(int j=0;j<N-M;j++) {
					for(int k=0;k<M;k++) {
						nowNum -= arr[i+k][j];
						nowNum += arr[i+k][j+M];
					}
					if(maxNum < nowNum) {
						maxNum = nowNum;
					}
				}
				maxNums[i] = maxNum;
			}
			Arrays.sort(maxNums);
			
			System.out.println("#"+test_case+" "+maxNums[N-M]);
		}
	}
}
