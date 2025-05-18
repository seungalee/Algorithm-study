package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_1928 {
	
	private static final Map<Character, Integer> BASE64_MAP = new HashMap<>();
	static {
	    String table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
	    for (int i = 0; i < table.length(); i++) {
	        BASE64_MAP.put(table.charAt(i), i);
	    }
	}
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		sc.nextLine();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			String line = sc.nextLine();
			StringBuilder sbString = new StringBuilder();
			
			//int->char 방법
			
			 char[] arr = line.toCharArray();
			 for(int i=0;i<line.length();i+=4) {
				 String binaryNum1 = String.format("%6s",Integer.toBinaryString(BASE64_MAP.get(arr[i]))).replace(' ', '0');
				 String binaryNum2 = String.format("%6s",Integer.toBinaryString(BASE64_MAP.get(arr[i+1]))).replace(' ', '0');
				 String binaryNum3 = String.format("%6s",Integer.toBinaryString(BASE64_MAP.get(arr[i+2]))).replace(' ', '0');
				 String binaryNum4 = String.format("%6s",Integer.toBinaryString(BASE64_MAP.get(arr[i+3]))).replace(' ', '0');
				 
				 StringBuilder sb = new StringBuilder();
				 sb.append(binaryNum1);
				 sb.append(binaryNum2);
				 sb.append(binaryNum3);
				 sb.append(binaryNum4);
				 
				 String c1 = sb.substring(0, 8);
				 String c2 = sb.substring(8, 16);
				 String c3 = sb.substring(16, 24);
				 
				 char c1Num = (char) Integer.parseInt(c1, 2);
				 char c2Num = (char) Integer.parseInt(c2, 2);
				 char c3Num = (char) Integer.parseInt(c3, 2);
				 
				 sbString.append(c1Num);
				 sbString.append(c2Num);
				 sbString.append(c3Num);	 
			 }
			 
			 System.out.println("#"+test_case+" "+sbString.toString());
			 

		}
	}
}
