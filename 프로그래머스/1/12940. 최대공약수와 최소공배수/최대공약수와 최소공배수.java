class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int [2];
        int big =0;
        int max = 0;
        int min = 0;
        if(n>m){
            big =n;
        }
        else{ big = m; }
        for(int i=1;i<big;i++){
            if(n%i==0 && m%i==0){
                if(i>max){
                    max = i;
                }
            }
        }
        min = (n*m)/max;
        answer[0] = max;
        answer[1] = min;
        return answer;
    }
}