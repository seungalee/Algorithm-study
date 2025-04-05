package 자바;

import java.util.Arrays;
import java.util.Scanner;

public class p1546 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        String testScores = sc.nextLine();
        int[] scoresArr = Arrays.stream(testScores.split(" ")).mapToInt(Integer::parseInt).toArray();

        int maxScore = 0;

        for(int i=0; i<scoresArr.length; i++){
            if(scoresArr[i]>maxScore){
                maxScore = scoresArr[i];
            }
        }

        double scoreTotal = 0;

        for(int i=0; i<scoresArr.length;i++){
            scoreTotal += ((double)scoresArr[i]/maxScore*100);
        }

        double answer = scoreTotal / scoresArr.length;
        System.out.print(answer);

    }
}
