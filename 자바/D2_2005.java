package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class D2_2005 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int[][] triangle = new int[N][N];
			
			triangle[0][0] = 1;
			for(int i=1;i<N;i++) {
				triangle[i][0] = 1;
				triangle[i][i] = 1;
			}
			
			for(int i=2;i<N;i++) {
				for(int j=1;j<i;j++) {
					triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
				}
			}
			System.out.println("#"+test_case);
			
			for(int i=0;i<N;i++) {
				for(int j=0;j<=i;j++) {
					System.out.print(triangle[i][j]);
					if(j!=i) {
						 System.out.print(" ");
					} else {
						if(test_case!=T || i!=N-1) {
							System.out.println("");
						}
						
					}
				}
				
				
			}
		}
	}
}
