package 자바;

import java.util.*;

public class D3_1244 {
	static int max;
	static HashSet<String> visited;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			String numString = sc.next();
			int cnt = sc.nextInt();
			//next
			char[] numArr = numString.toCharArray();
			max = 0;
			//미리 선언 이유?
			
			visited = new HashSet<>();
			dfs(numArr, cnt, 0);
			System.out.println("#"+test_case+" "+max);
			
		}
	}
	
	private static void dfs(char[] arr, int cnt, int depth) {
		if(depth == cnt) {
			int value = Integer.parseInt(new String(arr));
			max = Math.max(max, value);
			return;
		} 
		
		String state = new String(arr) + "-" + depth;
		if(visited.contains(state)) return;
		visited.add(state);
		
		int len = arr.length;
		
		for(int i=0;i<len-1;i++) {
			for(int j=i+1;j<len;j++) {
					swap(arr, i, j);
					dfs(arr, cnt, depth+1);
					swap(arr, i, j);
				
			}
		}
		
		if(depth < cnt) {
			if(!hasDuplicate(arr)) {
				swap(arr, len-1, len-2);
				dfs(arr, cnt, cnt);
				swap(arr, len-1, len-2);
			}
		}
	}
	
	private static boolean hasDuplicate(char[] arr) {
		Set<Character> set = new HashSet<>();
		for(char c: arr) {
			if(set.contains(c)) return true;
			set.add(c);
		}
		return false;
	}
	
	private static void swap(char[] arr, int i, int j) {
		char temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
}
