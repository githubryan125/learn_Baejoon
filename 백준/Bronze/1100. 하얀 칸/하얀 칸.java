import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int answer = 0;
        for(int i=0;i<8;i++){
            String chess = sc.nextLine();
            if(i%2==0){
                for(int j=0;j<chess.length();j=j+2){
                    if(chess.charAt(j)=='F'){
                        answer += 1;
                    }
                }
            }
            else{
                for(int j=1;j<chess.length();j=j+2){
                    if(chess.charAt(j)=='F'){
                        answer += 1;
                        }
                }
            }
        
        }
        System.out.println(answer);
    }
}