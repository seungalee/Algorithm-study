package 자바;

import java.util.Scanner;

public class P2750 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int N = sc.nextInt();
        int[] list = new int[N];

        for(int i=0;i<N;i++){
            list[i] = sc.nextInt();
        }

        for(int i=N-1;i>=0;i--){
            for(int j=0;j<i;j++){
                if(list[j]>list[j+1]){
                    int temp = list[j];
                    list[j] = list[j+1];
                    list[j+1] = temp;
                }
            }
        }

        for(int i=0;i<N;i++){
            System.out.println(list[i]);
        }
    }
}
