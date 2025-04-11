package 자바;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p12891 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        
        String dnaString = br.readLine();

        int[] letNum = new int[4];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<4;i++){
            letNum[i] = Integer.parseInt(st.nextToken());
        }

        int count = 0;
        String password = dnaString.substring(0, P); 
        long ACount = password.chars()
                                .filter(ch->ch == 'A').count();
        long CCount = password.chars()
                                .filter(ch->ch == 'C').count();
        long GCount = password.chars()
                                .filter(ch->ch == 'G').count();
        long TCount = password.chars()
                                .filter(ch->ch == 'T').count();
        if(ACount>=letNum[0]&&CCount>=letNum[1]&&GCount>=letNum[2]&&TCount>=letNum[3]){
            count++;
        }
        for(int i=1;i<=S-P;i++){
            char OldLet = dnaString.charAt(i-1);
            char NewLet = dnaString.charAt(i+P-1);
            if(OldLet == 'A'){
                ACount--;
            } else if(OldLet == 'C'){
                CCount--;
            } else if(OldLet == 'G'){
                GCount--;
            } else if(OldLet == 'T'){
                TCount--;
            }

            if(NewLet == 'A'){
                ACount++;
            } else if(NewLet == 'C'){
                CCount++;
            } else if(NewLet == 'G'){
                GCount++;
            } else if(NewLet == 'T'){
                TCount++;
            }

            if(ACount>=letNum[0]&&CCount>=letNum[1]&&GCount>=letNum[2]&&TCount>=letNum[3]){
                count++;
            }
        }
        
        System.out.println(count);
    }
}
