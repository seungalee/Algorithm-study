package 자바;

import java.util.Arrays;
import java.util.Scanner;

public class p11659 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String firstLine = sc.nextLine();
        int[] NandM = Arrays.stream(firstLine.split(" ")).mapToInt(Integer::parseInt).toArray();
        int N = NandM[0];
        int M = NandM[1];
        int sums[] = new int[N+1];
        int sum = 0;
        sums[0] = 0;

        for(int i=0;i<N;i++){
            sum += sc.nextInt();
            sums[i+1] = sum;
        }
//0 5 9 12 14 15
        for(int j=0; j<M; j++){
            int numI = sc.nextInt();
            int numJ = sc.nextInt();
            System.out.println(sums[numJ] - sums[numI-1]);
        }
    }
}
