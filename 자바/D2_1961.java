package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_1961 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int[][] arr = new int[N][N];
			for(int i=0;i<N;i++) {
				for(int j=0;j<N;j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			System.out.println("#"+test_case);
			
			StringBuilder sb;
			
			//for문을 내부에 여러개 만들지 않고 sb를 여러개 만들어 처리 가능
			for(int i=0;i<N;i++) {
				sb = new StringBuilder();
				for(int j=N-1;j>=0;j--) {
					sb.append(arr[j][i]);
				}
				sb.append(" ");
				for(int j=N-1;j>=0;j--) {
					sb.append(arr[N-i-1][j]);
				}
				sb.append(" ");
				for(int j=0;j<N;j++) {
					sb.append(arr[j][N-i-1]);
				}
				
				System.out.println(sb);
				
			}
		}
	}
}
