package 자바;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class D2_1983 {
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("자바/res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int K = sc.nextInt();
			
			
			double[] scores = new double[N+1];
			double midScore;
			double finScore;
			double asgScore;
			String[] grades = {"D0", "C-", "C0", "C+", "B-", "B0", "B+", "A-", "A0", "A+"};
			
			for(int i=1; i<=N;i++) {
				midScore = sc.nextDouble();
				finScore = sc.nextDouble();
				asgScore = sc.nextDouble();
				scores[i] = midScore*0.35 + finScore*0.45 + asgScore*0.2;
			}
			
			//K-1을 기억
			double wantScore = scores[K];
			Arrays.sort(scores);
			int perGrade = N/10;
			
			for(int i=0;i<N/perGrade;i++) {
				if(wantScore>=scores[i*perGrade+1] && wantScore <= scores[i*perGrade+perGrade]) {
					System.out.println("#"+test_case+" "+grades[i]);
					break;
				}
			}
		}
	}

}
