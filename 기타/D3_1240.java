package 기타;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class D3_1240 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		HashMap<String, Integer> codeHashMap = new HashMap<String, Integer>();
		codeHashMap.put("0001101", 0);
		codeHashMap.put("0011001", 1);
		codeHashMap.put("0010011", 2);
		codeHashMap.put("0111101", 3);
		codeHashMap.put("0100011", 4);
		codeHashMap.put("0110001", 5);
		codeHashMap.put("0101111", 6);
		codeHashMap.put("0111011", 7);
		codeHashMap.put("0110111", 8);
		codeHashMap.put("0001011", 9);
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int M = sc.nextInt();
			sc.nextLine();
			
			char[][] arr = new char[N][M];
			
			for(int i=0;i<N;i++) {
				String string = sc.nextLine();
				char[] chars = string.toCharArray();
				for(int j=0;j<M;j++) {
					arr[i][j] = chars[j];
				}
			}
			int answer = 0;
			Boolean foundAnswer = false;
			int gotI = 0;
			int gotJ = 0;
			
			for(int i=0;i<N;i++) {
				for(int j=M-1;j>=0;j--) {
					if(arr[i][j]=='1') {
						gotI = i;
						gotJ = j;
						break;
					}
				}
				if(gotJ!=0) break;
			}
			
			int[] code = new int[8];
			
			int start = gotJ-55;
			

			for(int k=0;k<8;k++) {
				StringBuilder sb = new StringBuilder();
				for(int l=0;l<7;l++) {
					int nowJ = start+k*8+l;
					sb.append(arr[gotI][start+k*7+l]);
				}
				code[k] = codeHashMap.get(sb.toString());
			}
			
			int IsValidNum = (code[0]+code[2]+code[4]+code[6])*3;
			IsValidNum+=(code[1]+code[3]+code[5]+code[7]);
			
			if(IsValidNum!=0 && IsValidNum %10==0) {
				for(int k=0;k<8;k++) {
					answer+=code[k];
				}
			}
			
			System.out.println("#"+test_case+" "+answer);
			
		}
	}
}
