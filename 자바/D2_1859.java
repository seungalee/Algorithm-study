package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class D2_1859 {
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("자바/res/input.txt")); // 입력 파일 경로
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int[] list = new int[N];
			int[] sorted_list = new int[N];
			for(int i=0;i<N;i++) {
				list[i] = sc.nextInt();
				sorted_list[i] = list[i];
			}
			
			//기본 처리 완료
			Arrays.sort(sorted_list);
			
			long answer = 0;
			long max = sorted_list[N-1];
			
			for(int i=0;i<N-1;i++) {
				if(list[i]<=max) {
					answer = answer + (max - list[i]);
				} else {
					int[] remain_arr = Arrays.copyOfRange(list, i+1, N);
					Arrays.sort(remain_arr);
					max = remain_arr[N-i-2];
				
				}
			}
			
			System.out.println("#" + test_case + " " + answer);
		}
		
	}

}
