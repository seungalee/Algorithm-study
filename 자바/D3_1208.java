package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class D3_1208 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));

		Scanner sc = new Scanner(System.in);
		for(int test_case = 1; test_case <= 10; test_case++)
		{
			int dumpNum = sc.nextInt();
			int[] boxes = new int[100];
			for(int i=0;i<100;i++) {
				boxes[i] = sc.nextInt();
			}
			
			Arrays.sort(boxes);

			
			for(int i=0;i<dumpNum;i++) {
				boxes[0]+=1;
				boxes[99]-=1;
				Arrays.sort(boxes);
				if(boxes[99]-boxes[0]<=1) {
					break;
				}
			}
			
			System.out.println("#"+test_case+" "+(boxes[99]-boxes[0]));
		}
	}
}
