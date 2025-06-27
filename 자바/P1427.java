package 자바;

import java.util.Arrays;
import java.util.Scanner;

public class P1427 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String NString = Integer.toString(N);
        int len = NString.length();
        int[] nums = new int[len];
        for(int i=0;i<len;i++){
            nums[i]=(int) NString.charAt(i) - 48;
        }

        Arrays.sort(nums);

        for(int i=0;i<len/2;i++){
            int temp = nums[i];
            nums[i] = nums[len-1-i];
            nums[len-1-i] = temp;
        }

        for(int i=0;i<len;i++){
            System.out.print(nums[i]);
        }
    }
}
