package 자바;

import java.util.Scanner;

public class p2018 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        long N = Long.valueOf(sc.nextLine());
 
        int count = 0;
        int i = 1;
        while(i*(i-1)/2 < N){
            long num =( N - (long)i*(i-1)/2 );
            if(num % i ==0){
                long a = num / i;
                if( a>= 1){
                    count++;
                }
            }
            i++;
        }
        System.out.println(count);
    }
}