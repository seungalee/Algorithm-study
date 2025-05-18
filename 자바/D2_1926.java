package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_1926 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));

		/*
		   표준입력 System.in 으로부터 스캐너를 만들어 데이터를 읽어옵니다.
		 */
		Scanner sc = new Scanner(System.in);
		int N;
		N=sc.nextInt();
		
		int howMany = 0;
		System.out.print("1");
		
		for(int i=2;i<=N;i++) {
			howMany = 0;
			String numString = Integer.toString(i);
			char[] numChar = numString.toCharArray();
			for(int j=0;j<numChar.length;j++) {
				if(numChar[j]=='3'||numChar[j]=='6'||numChar[j]=='9') {
					howMany++;
				}
			}
			if(howMany==0) {
				System.out.print(" "+ i);
			}else {
				System.out.print(" ");
				for(int k=0;k<howMany;k++) {
					System.out.print("-");
				}
			}
		}
	}
}
