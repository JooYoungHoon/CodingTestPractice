import java.io.*;
import java.util.*;

public class BOJ1475 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = br.readLine();
        int[] numList = new int[10];
        for(char c : N.toCharArray()) {
            int num = c - '0';
            if(num==9) {
                num = 6;
            }
            numList[num]++;
        }

        numList[6] = numList[6]/2 + numList[6]%2;
        Arrays.sort(numList);
        System.out.println(numList[9]);
    }
}
