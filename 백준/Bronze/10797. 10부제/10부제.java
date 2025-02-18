import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;
        for(int i=0;i<5;i++){
            int k = sc.nextInt();
            if(k==n){
                answer+=1;
            }
        }
        System.out.println(answer);
    }
}