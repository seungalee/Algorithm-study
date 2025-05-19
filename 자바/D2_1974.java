package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_1974 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int[][] arr = new int[9][9];
			
			for(int i=0;i<9;i++) {
				for(int j=0;j<9;j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			int[] numChecklist;
			Boolean isValid = true;
			
			//가로 방향으로 체크
			for(int i=0;i<9;i++) {
				numChecklist = new int[10];
				for(int j=0;j<9;j++) {
					if(numChecklist[arr[i][j]]!=0) {
						isValid = false;
						break;
					} else {
						numChecklist[arr[i][j]] = 1;
					}
				}
			}
			
			//세로 방향으로 체크
			for(int j=0;j<9;j++) {
				numChecklist = new int[10];
				for(int i=0;i<9;i++) {
					if(numChecklist[arr[i][j]]!=0) {
						isValid = false;
						break;
					} else {
						numChecklist[arr[i][j]] = 1;
					}
				}
			}
			
			//3x3 체크
			//더 좋은 방법..?
			for(int i=0;i<9;i+=3) {
				for(int j=0;j<9;j+=3) {
					numChecklist = new int[10];
					numChecklist[arr[i][j]] +=1;
					numChecklist[arr[i][j+1]] +=1;
					numChecklist[arr[i][j+2]] +=1;
					numChecklist[arr[i+1][j]] +=1;
					numChecklist[arr[i+1][j+1]] +=1;
					numChecklist[arr[i+1][j+2]] +=1;
					numChecklist[arr[i+2][j]] +=1;
					numChecklist[arr[i+2][j+1]] +=1;
					numChecklist[arr[i+2][j+2]] +=1;
					
					for(int k=1;k<10;k++) {
						if(numChecklist[k]!=1) {
							isValid = false;
							break;
						}
					}
				}
			}
			if(isValid) {
				System.out.println("#"+test_case+" "+1);
			} else {
				System.out.println("#"+test_case+" "+0);
			}
			
		}
	}
		
}
