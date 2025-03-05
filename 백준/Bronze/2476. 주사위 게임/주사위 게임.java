import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;
        for(int i=0;i<n;i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int result = 0;
            if(a==b && b==c){
                result = 10000+a*1000;
                if(result>answer){ answer = result;}
            } else if(a==b || a==c || b==c){
                if(a==b){
                    result = 1000+a*100;
                    if(result>answer){ answer = result;}
                }else if(b==c){
                    result = 1000+b*100;
                    if(result>answer){ answer = result;}
                }else{
                    result = 1000+c*100;
                    if(result>answer){ answer = result;}
                }
                
            } else{ 
                result  = Math.max(a,Math.max(b,c))*100;
                if(result>answer){
                      answer = result;
                      }
                  }
            
        }
        System.out.println(answer);
    }
}