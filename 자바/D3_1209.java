package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class D3_1209 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		for(int test_case = 1; test_case <= 10; test_case++)
		{
			sc.nextInt();
			int[][] arr = new int[100][100];
			ArrayList<Integer> sums = new ArrayList<>();
			for(int i=0;i<100;i++) {
				int sum = 0;
				for(int j=0;j<100;j++) {
					int num = sc.nextInt();
					arr[i][j] = num;
					sum+=num;
				}
				sums.add(sum);
			}
			
			for(int j=0;j<100;j++) {
				int sum = 0;
				for(int i=0;i<100;i++) {
					sum+=arr[i][j];
				}
				sums.add(sum);
			}
			int sum1 = 0;
			int sum2 = 0;
			for(int i=0;i<100;i++) {
				sum1+=arr[i][i];
				sum2+=arr[i][99-i];
			}
			sums.add(sum1);
			sums.add(sum2);
			
			Collections.sort(sums, Collections.reverseOrder());
			
			System.out.println("#"+test_case+" "+sums.get(0));
		}
		
		
	}
}
