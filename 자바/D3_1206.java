package 자바;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class D3_1206 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("자바/res/sample_input.txt")); // 입력 파일 경로

        Scanner sc = new Scanner(System.in);
        int T = 10; // 테스트 케이스 수
        int[] buildings = new int[1000];

        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt(); // 건물 개수
            
            for (int i = 0; i < N; i++) {
                buildings[i] = sc.nextInt(); // 건물 높이 입력
            }

            int answer = 0;
            if(N>=5) {
	            for (int i = 2; i < N - 2; i++) {
	                if (buildings[i - 2] < buildings[i] && buildings[i - 1] < buildings[i] &&
	                    buildings[i + 1] < buildings[i] && buildings[i + 2] < buildings[i]) {
	
	                	int maxNeighbor = Math.max(
	                		    Math.max(buildings[i - 2], buildings[i - 1]),
	                		    Math.max(buildings[i + 1], buildings[i + 2])
	                		);
	                    answer += buildings[i] - maxNeighbor;
	                }
	            }
            }

            System.out.println("#" + test_case + " " + answer);
        }
    }
}
