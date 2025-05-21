package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_1989 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			String str = sc.next();
			char[] strArr = str.toCharArray();
			int isTrue = 1;
			
			for(int i=0;i<str.length()/2+1;i++) {
				if(strArr[i]!=strArr[str.length()-1-i]) {
					isTrue = 0;
				}
			}
			
			System.out.println("#"+test_case+" "+isTrue);
			
		}
	}
}
