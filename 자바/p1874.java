package 자바;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1874 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] wanted = new int[n];
        int[] stack = new int[n];
        int top = -1;
        StringBuilder answer = new StringBuilder();
        
        for(int i=0; i<n;i++){
            wanted[i] = Integer.parseInt(br.readLine());
        }
        int num = 1;
        for(int i=0;i<n;i++){
            int target = wanted[i];
            while(num<=target){
                stack[++top] = num++;
                answer.append("+");
            }
            if(stack[top]==target){
                top--;
                answer.append("-");
                continue;
            }
            else{
                System.out.println("NO");
                return;
            }
        }
        for(int i=0; i<answer.length();i++){
            System.out.println(answer.charAt(i));
        }

    }
}
