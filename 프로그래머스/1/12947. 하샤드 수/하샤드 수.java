class Solution {
    public boolean solution(int x) {
        boolean answer = false;
        int com = 0;
        int fir_x=x;
        while(x>10){
            com+=x%10;
            x/=10;
        }
        com+=x;
        if(fir_x % com ==0){
            answer=true;
        }
        return answer;
    }
}