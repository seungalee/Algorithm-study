package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_2007 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		sc.nextLine();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			String line = sc.nextLine();
			
			for(int i = 1;i<=10;i++) {
				Boolean isAnswer = true;
				String subString = line.substring(0, i);
				for(int j=0;j<(30/i)-1;j++) {
					if(!subString.equals(line.substring(i+j*i,i+(j+1)*i))){
						isAnswer = false;
						break;
					}
				}
				if(isAnswer) {
					System.out.println("#"+test_case+" "+i);
					break;
				}
			}
		}
	}
}
