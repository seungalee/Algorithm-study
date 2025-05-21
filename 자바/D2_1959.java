package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_1959 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
	

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			int larger;
			int smaller;
			int[] largerList;
			int[] smallerList;
			if(N>M) {
				larger = N;
				smaller = M;
				largerList = new int[N];
				smallerList = new int[M];
				for(int i=0;i<N;i++) {
					largerList[i] = sc.nextInt();
				}
				for(int i=0;i<M;i++) {
					smallerList[i] = sc.nextInt();
				}
			} else {
				larger = M;
				smaller = N;
				largerList = new int[M];
				smallerList = new int[N];
				for(int i=0;i<N;i++) {
					smallerList[i] = sc.nextInt();
				}
				for(int i=0;i<M;i++) {
					largerList[i] = sc.nextInt();
				}
				
			
			}
			
			
			//읽기 완료
			
			int maxNum = Integer.MIN_VALUE;
			int nowNum;
			for(int i=0;i<larger-smaller+1;i++) {
				nowNum = 0;
				for(int j=0;j<smaller;j++) {
					nowNum+= smallerList[j]*largerList[j+i];
				}
				maxNum = Math.max(maxNum, nowNum);
			}
			
			System.out.println("#"+test_case+" "+maxNum);
		}
	}
}
